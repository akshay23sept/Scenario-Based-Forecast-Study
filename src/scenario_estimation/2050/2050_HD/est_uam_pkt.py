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

def est_uam_pkt(city, uam_ticket_cost, vertiport_density, 
	trip_distance_step_size, income_step_size, detail_flag):

	city_df = pd.DataFrame()

	# Start by generating all the points which are to be evaluated
	# For income and distance, the range of points to be evaluated may
	# 	change. 
	income_array, income_averages_array = generate_income_space_range(
		city, income_step_size)
	td_array, td_averages_array = generate_trip_distance_space_range(
		city, trip_distance_step_size)

	min_dist_between_vertiports = np.sqrt(vertiport_density)
	
	# Run nested for-loop. Each iteration represents a different trip,
	# 	described by mode, purpose, distance, and income.
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

					# Estimate each of the values in the WTP equation
					# 	cost of this trip using mode m
					# 	value placed per unit time saved
					# 	time to complete trip using mode m
					# 	time to complete trip using UAM
					trip_cost_m = est_trip_cost_m(city, distance, mode)
					
					value_per_time_saved = est_value_per_time_saved(
						income, purpose)

					trip_time_m = est_trip_time_m(city, distance, mode)
					trip_time_uam = est_trip_time_uam(city, distance,
						min_dist_between_vertiports)

					# Finally, calculate the willingness to pay
					willingness_to_pay = (
						trip_cost_m 
						+ value_per_time_saved 
						* (trip_time_m - trip_time_uam)
					)

					# Estimate the cost of this trip when using UAM
					cost_uam = est_cost_uam_trip(city, distance,
						uam_ticket_cost, min_dist_between_vertiports)

					# Find the difference between WTP and UAM trip cost
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

					# If the WTP is greater than UAM trip cost, then 
					# 	we say that this will be a UAM trip. Now find
					# 	the PKM associated with this trip. If 
					# 	detail_flag is true, then the PKM will be
					#	evaluated for all trips, regardless of whether 
					# 	it's a UAM trip or not.

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