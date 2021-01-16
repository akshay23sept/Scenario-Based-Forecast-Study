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
	step_size_1 = step_size
	step_size_2 = step_size * 2
	max_value = 240 # range from INRIX data
	max_value = math.ceil(max_value/step_size_2)*step_size_2

	n_steps_1 = math.ceil(max_value/2 / step_size_1)
	n_steps_2 = math.ceil(max_value/2 / step_size_2)

	td_low = np.arange(0,max_value/2,step_size_1).tolist()
	td_low.extend(np.arange(td_low[-1]+step_size_2,max_value,step_size_2).tolist())
	td_high = td_low[1:]
	td_high.append(td_high[-1]+step_size_2)

	td_array = (
		np.transpose(np.stack((td_low,td_high),axis=0)))
	td_averages_array = np.mean(td_array,axis=1)

	return td_array, td_averages_array

# income design space generation
def generate_income_space_range(city, step_size):	
	##################################   MODIFY THE YEAR   ####################################
	##################################   MODIFY THE YEAR   ####################################
	mu = city['2045_income_distribution_func_coeff_mu']
	sigma = city['2045_income_distribution_func_coeff_sigma']
	max_value = scipy.stats.lognorm.ppf(0.999,sigma,scale=math.exp(mu))
##################################   MODIFY THE YEAR   ####################################
##################################   MODIFY THE YEAR   ####################################
	step_size_1 = step_size
	step_size_2 = step_size * 4  #(ideally 2)
	max_value = math.ceil(max_value/step_size_2)*step_size_2

	n_steps_1 = math.ceil(max_value/2 / step_size_1)
	n_steps_2 = math.ceil(max_value/2 / step_size_2)

	incomes_low = np.arange(0,max_value/2,step_size_1).tolist()
	incomes_low.extend(np.arange(incomes_low[-1]+step_size_2,max_value,step_size_2).tolist())
	incomes_high = incomes_low[1:]
	incomes_high.append(incomes_high[-1]+step_size_2)

	income_array = (
		np.transpose(np.stack((incomes_low,incomes_high),axis=0)))
	income_averages_array = np.mean(income_array,axis=1)

	return income_array, income_averages_array
