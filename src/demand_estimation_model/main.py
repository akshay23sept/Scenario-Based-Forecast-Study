#OASyS Project (Nov 2019 to Nov 2020)

 
  #Author: Akshay Anand



import pandas as pd
import numpy as np
import csv

from est_uam_pkt import est_uam_pkt


def main(cases_list, input_data, trip_distance_step_size, 
	income_step_size, detail_flag):
	i=0
	j=0
	for case in cases_list:
		print('Running case '+str((i+1))+'/'+str(len(cases_list)))
		uam_ticket_cost = float(case[0])
		vertiport_density = float(case[1])

		out_df = pd.DataFrame()
		for index, row in input_data.iterrows():
			city_df = est_uam_pkt(row, uam_ticket_cost, vertiport_density, trip_distance_step_size, income_step_size, detail_flag)

			out_df = out_df.append(city_df,ignore_index=True)
			j+=1
			pct_done = (round(j/(len(input_data.index))*100/len(cases_list),1))
			print(str(pct_done)+' percent complete')
		
		outfilename = (
			'out_' + str(uam_ticket_cost) + '_' + str(vertiport_density) + '.csv')
		out_df.to_csv(outfilename)
		print('case '+str(i+1)+' written to '+outfilename)
		i+=1



if __name__ == '__main__':
	with open('cases_list_akshay.csv') as f:
		cases_list = [tuple(line) for line in csv.reader(f)]
		cases_list = cases_list[1:]

	trip_distance_step_size = 10
	income_step_size = 25000
	detail_flag = False
	input_data = pd.read_excel('31_cities.xlsx')
	
	main(cases_list, input_data,
		trip_distance_step_size, income_step_size, detail_flag)