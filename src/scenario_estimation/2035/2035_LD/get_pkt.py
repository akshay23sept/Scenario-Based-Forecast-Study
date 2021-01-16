import scipy.stats
import statistics
import math


def get_pkt(mode,purpose,distance_range,income_range,city):
	# Estimates PKM for a specified trip.

	# Start with getting the total PKM in the city from the input file
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	tot_pkm = city['2035_tot_pkm']
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++	
	##################################   MODIFY THE YEAR   ####################################

	### apply mode split percent ###
	# Get the percentage of trips which are conducted for the specified
	#	mode, and multiply that to the total city pkm.
	if mode == 'personal_vehicle':
		pkm = tot_pkm * city['pct_personal_vehicle']
	elif mode == 'public_transit':
		pkm = tot_pkm * city['pct_public_transit']

	### apply trip distance percent ###
	# Get the trips distribution coefficients from the input file. The
	#	coefficients coordinate to a lognormal distribution. 
	distance_low, distance_high = (
		min(distance_range), max(distance_range))
	mu = city['trip_dist_distribution_func_coeff_mu']
	sigma = city['trip_dist_distribution_func_coeff_sigma']
	# Evaluate the cumulative distribution function to get the 
	#	percentage of traffic which occurs between this trip distance 
	#	range.
	trips_percent = (
		scipy.stats.lognorm.cdf(distance_high,sigma,scale=math.exp(mu)) 
		- scipy.stats.lognorm.cdf(distance_low,sigma,scale=math.exp(mu))
	)
	pkm *= trips_percent

	### apply income percent ###
	# Get the income distribution coefficients from the input file. The
	#	coefficients coordinate to a lognormal distribution.
	income_low, income_high = min(income_range), max(income_range)
	##################################   MODIFY THE YEAR   ####################################
	#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	mu = city['2035_income_distribution_func_coeff_mu']
	sigma = city['2035_income_distribution_func_coeff_sigma']
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	# Evaluate the cumulative distribution function to get the 
	#	percentage of traffic which occurs between this income level 
	#	range.
	income_percent = (
		scipy.stats.lognorm.cdf(income_high,sigma,scale=math.exp(mu)) 
		- scipy.stats.lognorm.cdf(income_low,sigma,scale=math.exp(mu))
		)
	pkm *= income_percent

	### apply purpose percent ###
	# purpose split is taken from the input file
	if purpose == 'business':
		purpose_percent = city['pct_business_trips']
	elif purpose == 'personal':
		purpose_percent = city['pct_personal_trips']
	pkm *= purpose_percent

	return pkm, {
		'trips_percent': trips_percent,
		'income_percent': income_percent,
		'purpose_percent': purpose_percent
	}