 #OASyS Project (Nov 2019 to Nov 2020)

  
  #Author: Akshay Anand




import scipy.stats
import statistics
import math


def get_pkt(
	mode,purpose,distance_range,income_range,city):

	### apply trips percent ###
	distance_low, distance_high = (
		min(distance_range), max(distance_range))
	mu = city['trip_dist_distribution_func_coeff_mu']
	sigma = city['trip_dist_distribution_func_coeff_sigma']

	if mode == 'personal_vehicle':

		pkm_m = city['tot_pkm'] * city['pct_personal_vehicle']
		trips_percent = (
			scipy.stats.lognorm.cdf(distance_high,sigma,scale=math.exp(mu)) 
			- scipy.stats.lognorm.cdf(distance_low,sigma,scale=math.exp(mu))
		)
	elif mode == 'public_transit':

		pkm_m = city['tot_pkm'] * city['pct_public_transit']
		trips_percent = (
			scipy.stats.lognorm.cdf(distance_high,sigma,scale=math.exp(mu)) 
			- scipy.stats.lognorm.cdf(distance_low,sigma,scale=math.exp(mu))
		)
	
	pkt = pkm_m * trips_percent

	### apply income percent ###
	mu = city['income_distribution_func_coeff_mu']
	sigma = city['income_distribution_func_coeff_sigma']

	income_low, income_high = min(income_range), max(income_range)

	income_percent = (
		scipy.stats.lognorm.cdf(income_high,sigma,scale=math.exp(mu)) 
		- scipy.stats.lognorm.cdf(income_low,sigma,scale=math.exp(mu))
		)

	pkt *= income_percent

	### apply purpose percent ###
	if purpose == 'business':
		purpose_percent = city['pct_business_trips']
	elif purpose == 'personal':
		purpose_percent = city['pct_personal_trips']
	pkt *= purpose_percent

	return pkt, {
		'trips_percent': trips_percent,
		'income_percent': income_percent,
		'purpose_percent': purpose_percent
	}