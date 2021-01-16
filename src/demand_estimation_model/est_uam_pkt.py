 #OASyS Project (Nov 2019 to Nov 2020)

  
  #Author: Akshay Anand



import numpy as np
import pandas as pd

from design_space_definition import (
	available_modes_list, possible_trip_purposes_list,
	generate_trip_distance_space_range, generate_income_space_range)
from wtp_subfunctions import (
	est_cost_uam_trip, est_trip_cost_m, est_trip_time_m,
	est_value_per_time_saved, est_trip_time_uam)
from get_pkt import get_pkt
from assumptions import avg_pax_per_trip, avg_speed_uam
# To-do's:
# public transit distribution vs income level
# tune the UAM cost function
# upgrade uam trip time and distance calculation
# public transit speed should be function of metro length density
# personal vehicle speed should be clustered with trip distributions
# add alternate mode cost until vertiport to uam total cost
# incorporate utilization into cost model
# more intelligently sample the space (monte carlo)
# base discount rate on real data

# add more trip purposes for VTTS evaluation
# make distinction between metro and bus for trip time

# how many spots of interest (attractors) within representative cities? how many start and landing points? # of vertiports should be same as nuber of attractors

def est_uam_pkt(city, uam_ticket_cost, vertiport_density, trip_distance_step_size, income_step_size, detail_flag):
	city_df = pd.DataFrame()

	income_array, income_averages_array = generate_income_space_range(
		city, income_step_size)
	td_array, td_averages_array = generate_trip_distance_space_range(
		city, trip_distance_step_size)

	min_dist_between_vertiports = np.sqrt(vertiport_density)
	

	for mode in available_modes_list:
		for purpose in possible_trip_purposes_list:
			for inc_idx, income in enumerate(income_averages_array):
				for dist_idx, distance in enumerate(td_averages_array):

					inp_dict = {
						'mode': mode,
						'purpose': purpose,
						'distance':distance,
						'dist_range': td_array[dist_idx], 
						'income': income,
						'inc_range': income_array[inc_idx]
					}
					out_dict = {
						'city_ID': city['ID'],
						'city_name': city['Urban Area']
					}

					trip_cost_m = est_trip_cost_m(city, distance, mode)
					
					value_per_time_saved = est_value_per_time_saved(income, purpose)

					trip_time_m = est_trip_time_m(city, distance, mode)
					trip_time_uam = est_trip_time_uam(city, distance,
						min_dist_between_vertiports)

					willingness_to_pay = (
						trip_cost_m 
						+ value_per_time_saved 
						* (trip_time_m - trip_time_uam)
					)

					cost_uam = est_cost_uam_trip(city, distance,
						uam_ticket_cost, min_dist_between_vertiports)

					cost_delta = willingness_to_pay - cost_uam

					dsp_eval_dict = {
						'trip_cost_m ($)': trip_cost_m,
						'VTTS ($/min)': value_per_time_saved,
						'trip_time_m (min)': trip_time_m,
						'trip_time_uam (min)': trip_time_uam,
						'trip_time_saved (min)': (
							trip_time_m - trip_time_uam),
						'WTP ($)': willingness_to_pay,
						'cost_uam ($)': cost_uam,
						'cost_delta ($)': cost_delta
					}

					if detail_flag:
						pkt, percent_dict = get_pkt(
							mode, purpose,
							td_array[dist_idx], income_array[inc_idx],
							city)

					if willingness_to_pay >= cost_uam:
						if ~detail_flag:
							pkt, percent_dict = get_pkt(
								mode, purpose, td_array[dist_idx],
								income_array[inc_idx], city)

						uam_pkt = pkt
						uam_pax_trips = pkt / distance
						uam_vehicle_trips = (
							uam_pax_trips / avg_pax_per_trip)
						uam_utilization = pkt / (avg_speed_uam * 60)
					else:
						uam_pkt = 0
						uam_pax_trips = 0
						uam_vehicle_trips = 0
						uam_utilization = 0
					
					pkt_dict = {
						# 'avail_pkt': pkt,
						'uam_pkt': uam_pkt,
						'uam_pax_trips': uam_pax_trips,
						'uam_vehicle_trips': uam_vehicle_trips,
						'uam_utilization': uam_utilization
					}

					out_dict = {**out_dict, **inp_dict, **dsp_eval_dict, **pkt_dict}
					city_df = city_df.append(out_dict,ignore_index=True)

	return city_df