 #OASyS Project (Nov 2019 to Nov 2020)

  
  #Co- Author: Akshay Anand


import numpy as np
import math

from assumptions import (time_board, time_deboard, avg_speed_uam, 
	VTTS_business, VTTS_personal, working_minutes_per_yr)


def est_trip_cost_m(city, distance, alt_travel_mode='personal_vehicle'):
	if alt_travel_mode == 'personal_vehicle':
		trip_cost_m = city['cost_per_distance_pv'] * distance
	elif alt_travel_mode == 'public_transit':
		if distance <= city['city_radius']:
			trip_cost_m = city['ticket_cost_pt_intracity']
		else:
			trip_cost_m = city['ticket_cost_pt_intercity']
	return trip_cost_m

def est_cost_uam_trip(
	city, distance, uam_cost_dollar_per_mile, 
	min_dist_between_vertiports):
	
	if distance < min_dist_between_vertiports:
		distance = min_dist_between_vertiports

	cost_per_dist = uam_cost_dollar_per_mile/1.609
	cost_per_dist*= city['cost_of_living_index']/100

	avg_dist_to_vertiport = (
		(min_dist_between_vertiports * np.sqrt(2) / 2)
		* (2/3)
	)
	access_egress_cost = (
		city['cost_per_distance_rs'] * avg_dist_to_vertiport)

	return (cost_per_dist * distance) + access_egress_cost * 2

def est_trip_time_m(city, distance, alt_travel_mode='personal_vehicle'):
	if distance < 10:
		speed_distance = 10
	elif distance > 140:
		speed_distance = 140
	else:
		speed_distance = distance

	if alt_travel_mode == 'personal_vehicle':
		if math.isnan(city['pv_speed_reg_coeff_a']):
			speed = 1.1 #avg km/hr
		else:
			a = city['pv_speed_reg_coeff_a']
			b = city['pv_speed_reg_coeff_b']
			speed = a*np.log(speed_distance) + b
		congestion_level = city['congestion_level']
		travel_time = distance / speed * (1 + congestion_level)
	elif alt_travel_mode == 'public_transit':
		if math.isnan(city['pt_speed_reg_coeff_a']):
			speed = 0.43 #avg km/hr
		else:
			a = city['pt_speed_reg_coeff_a']
			b = city['pt_speed_reg_coeff_b']
			speed = a*np.log(speed_distance) + b
		travel_time = distance / speed
	
	return travel_time

def est_value_per_time_saved(income, travel_purpose):
	if travel_purpose == 'business':
		value_per_time_saved = (
			VTTS_business * (income / working_minutes_per_yr))
	elif travel_purpose == 'personal':
		value_per_time_saved = (
			VTTS_personal * (income / working_minutes_per_yr))
	return value_per_time_saved

def est_trip_time_uam(city, distance, min_dist_between_vertiports):
	if distance < min_dist_between_vertiports:
		distance = min_dist_between_vertiports
	avg_dist_to_vertiport = (
		(min_dist_between_vertiports * np.sqrt(2) / 2)
		* (2/3)
	)
	avg_time_to_port = est_trip_time_m(city,avg_dist_to_vertiport)

	return (
		avg_time_to_port * 2
		+ time_board 
		+ distance / avg_speed_uam
		+ time_deboard 
		)