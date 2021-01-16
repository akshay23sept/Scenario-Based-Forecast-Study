import numpy as np
import math

from assumptions import (time_board, time_deboard, avg_speed_uam, 
	VTTS_business, VTTS_personal, working_minutes_per_yr)


def est_trip_cost_m(city, distance, alt_travel_mode='personal_vehicle'):
	# Estimates the cost of a trip when using alternate mode m. Three
	# 	options: personal vehicle (pv), public transit (pt) intracity,
	# 	and public transit (pt) intercity. Each mode has a cost per 
	# 	distance or cost per trip associated with it, which is drawn
	# 	from the input city attributes file.

	if alt_travel_mode == 'personal_vehicle':
		trip_cost_m = city['cost_per_distance_pv'] * distance + city['parking_cost']
	elif alt_travel_mode == 'public_transit':
		if distance <= city['city_radius']:
			trip_cost_m = city['ticket_cost_pt_intracity']
		else:
			trip_cost_m = city['ticket_cost_pt_intercity']
	return trip_cost_m

def est_cost_uam_trip(
	city, distance, uam_cost_dollar_per_mile, 
	min_dist_between_vertiports):
	# Estimates the cost of a UAM trip. 
	
	# If the nominal trip distance is
	# 	less than the minimum distance between vertiports, then the 
	# 	trip distance is set the the minimum distance (because that is 
	#	the minimum UAM trip distance). 
	if distance < min_dist_between_vertiports:
		distance = min_dist_between_vertiports

	# Convert form $/mi to $/km
	cost_per_dist = uam_cost_dollar_per_mile/1.609

	# The 50% of the cost is adjusted based on cost of living index, 
	# 	which comes from the input city attributes file.
	cost_per_dist = (
		cost_per_dist/2 
		+ (cost_per_dist/2 * (city['cost_of_living_index']/100)))

	# UAM trip cost also includes cost for access and egress, calculated
	#	based on rideshare costs. Rideshare costs are drawn from the 
	#	input city attributes file. The access and egress is based on
	#	an average vertiport distance, calculated as 2/3 of the max
	# 	distance to any vertiport.
	avg_dist_to_vertiport = (
		(min_dist_between_vertiports * np.sqrt(2) / 2)
		* (2/3)
	)
	access_egress_cost = (
		city['cost_per_distance_rs'] * avg_dist_to_vertiport)

	return (cost_per_dist * distance) + access_egress_cost * 2

def est_trip_time_m(city, distance, alt_travel_mode='personal_vehicle'):
	# Estimates trip time using alternate mode m.

	# Regression models which estimate the speed of the trip based on 
	# 	trip distance are used. Some of the models become inaccurate
	# 	at the edges of the regressed data, so this sets an upper and 
	# 	lower "speed distance", used only to estimate the avg speed.
	if distance < 5:
		speed_distance = 5
	elif distance > 140:
		speed_distance = 140
	else:
		speed_distance = distance

	# Two different regressions made by used, depending on if the mode
	#	is public transit or personal vehicle. Each currently assume a 
	# 	fixed average speed if there is no speed regression recorded in
	# 	the input file. Moving forward, all cities should have a 
	# 	regression (data gaps to be filled by grouping), so i suspect
	# 	this will be removed.

	# The regression is expected to be logarithmic,
	# 	and coefficients a and b are drawn from the input file.
	if alt_travel_mode == 'personal_vehicle':
		if math.isnan(city['pv_speed_reg_coeff_a']):
			speed = 0.953149 #avg km/min (all representative cities) previously 1.1 km/ min
		else:
			a = city['pv_speed_reg_coeff_a']
			b = city['pv_speed_reg_coeff_b']
			speed = a*np.log(speed_distance) + b
		# Because the regressions were recorded during free flow 
		#	conditions, the travel time is modified based on congestion
		# 	level of the city. Half the additional congested time is
		#	added because we want the avg between free flow and 
		#	congested.
	#	congestion_level = city['congestion_level']
		travel_time = distance / speed
		 #* (1 + congestion_level/2)
	elif alt_travel_mode == 'public_transit':
		# No congestion factor is added for public transit, as we assume
		#	public transit is not affected as much due to rush hour. 
		#	This might not be a valid assumption, revisit this.
		if math.isnan(city['pt_speed_reg_coeff_a']):
			speed = 0.56954 #avg km/min (all representative cities) previously 0.43 km/min
		else:
			a = city['pt_speed_reg_coeff_a']
			b = city['pt_speed_reg_coeff_b']
			speed = a*np.log(speed_distance) + b
		travel_time = distance / speed
	
	return travel_time

def est_value_per_time_saved(income, travel_purpose):
	# The value per minute saved is estimated. Two purposes are 
	#	implemented: business and personal. The earning percentage
	#	is specified in the assumptions file. VTTS is based on annual
	#	household income. The value per minute then is estimated based
	#	on working minutes per year. This figure is based on US 
	# 	wokring estimates, and might need to be revisited.

	if travel_purpose == 'business':
		value_per_time_saved = (
			VTTS_business * (income / working_minutes_per_yr))
	elif travel_purpose == 'personal':
		value_per_time_saved = (
			VTTS_personal * (income / working_minutes_per_yr))
	return value_per_time_saved

def est_trip_time_uam(city, distance, min_dist_between_vertiports):
	# Estimate the trip time using UAM. Trip time is the sum of access,
	#	egress, boarding, deboarding, and flight. 

	# The trip distance must be at least the minimum distance between 
	#	vertiports.
	if distance < min_dist_between_vertiports:
		distance = min_dist_between_vertiports
	
	#  Access and egress times are based on using a personal vehicle
	#	to travel the average distance to vertiport. Avg distance is 
	#	estimated as 2/3 of the maximum distance to any vertiport. 
	avg_dist_to_vertiport = (
		(min_dist_between_vertiports * np.sqrt(2) / 2)
		* (2/3))
	avg_time_to_port = est_trip_time_m(city,avg_dist_to_vertiport)

	# Flight time is estimated based on a constant average cruise speed
	#	across the entire nominal trip distance. Boarding and deboarding
	#	times are based on assumptions, listed in the assumptions file.
	return (
		avg_time_to_port * 2
		+ time_board 
		+ distance / avg_speed_uam
		+ time_deboard 
		)