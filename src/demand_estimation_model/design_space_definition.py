 #OASyS Project (Nov 2019 to Nov 2020)


  #Author: Akshay Anand



import numpy as np
import scipy.stats
import math
from scipy.stats import chi2
from scipy.stats import norm

# travel modes and travel trip purposes
available_modes_list = ['personal_vehicle','public_transit']
possible_trip_purposes_list = ['business','personal']

# trip distance design space generation
def generate_trip_distance_space_range(city, step_size):
	max_value = 250

	n_steps = math.ceil(max_value / step_size)
	td_low = np.arange(0,step_size*(n_steps),step_size).tolist()
	td_high = (
		np.arange(step_size,step_size*(n_steps+1),step_size).tolist())

	td_low = np.linspace(0, max_value-max_value/step_size, step_size)
	td_high = np.linspace(max_value/step_size, max_value, step_size)

	td_array = (
		np.transpose(np.stack((td_low,td_high),axis=0)))
	td_averages_array = np.mean(td_array,axis=1)

	return td_array, td_averages_array

# income design space generation
def generate_income_space_range(city, step_size):	
	mu = city['income_distribution_func_coeff_mu']
	sigma = city['income_distribution_func_coeff_sigma']
	max_value = scipy.stats.lognorm.ppf(0.999,sigma,scale=math.exp(mu))

	n_steps = math.ceil(max_value / step_size)
	incomes_low = np.arange(0,step_size*(n_steps),step_size).tolist()
	incomes_high = (
		np.arange(step_size,step_size*(n_steps+1),step_size).tolist())

	income_array = (
		np.transpose(np.stack((incomes_low,incomes_high),axis=0)))
	income_averages_array = np.mean(income_array,axis=1)

	return income_array, income_averages_array
