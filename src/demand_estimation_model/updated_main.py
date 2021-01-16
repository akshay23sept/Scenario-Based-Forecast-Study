#OASyS Project (Nov 2019 to Nov 2020)

#Author: Akshay Anand

import pandas as pd
import numpy as np
from keras.models import Sequential
import tensorflow as tf
import csv
import concurrent.futures

from est_uam_pkt import est_uam_pkt
from get_results_summary import get_results_summary


#### README starting at "if __name__..." ####

def main(cases_list, input_data, trip_distance_step_size,
         income_step_size, detail_flag):
    i = 0
    j = 0
    for case in cases_list:
        print('Running case ' + str((i + 1)) + '/' + str(len(cases_list)))
        uam_ticket_cost = float(case[0])
        vertiport_density = float(case[1])

        out_df = pd.DataFrame()

        # This for-loop evaluates each city one by one, then records the
        # 	results to out_df. After each iteration, the df is updated.
        with concurrent.futures.ProcessPoolExecutor() as executor:
            future_to_city_df = { executor.submit(est_uam_pkt,
                    row, uam_ticket_cost, vertiport_density,
                    trip_distance_step_size, income_step_size, detail_flag): index for index,row in input_data.iterrows() }

            for future in concurrent.futures.as_completed(future_to_city_df):
                out_df = out_df.append(future.result(), ignore_index=True)

                j += 1
                pct_done = (
                    round(j / (len(input_data.index)) * 100 / len(cases_list), 1))
                print(str(pct_done) + ' percent complete')

        # Output dataframe to the results folder
        outfilename = (
                'results/out_' + str(uam_ticket_cost) + '_'
                + str(vertiport_density) + '.csv')
        out_df.to_csv(outfilename)
        print('case ' + str(i + 1) + ' written to ' + outfilename)
        i += 1


if __name__ == '__main__':
    # Specify filename of cases list
    # each case is a different cost figure and vertiport density
    # for OASYS, this case definition file will likely need to be
    # 	reworked to evaluate the OASYS scenarios/years
    with open('scenario_cases_small.csv') as f:
        cases_list = [tuple(line) for line in csv.reader(f)]
        cases_list = cases_list[1:]

    # Specify the step sizes
    # The code uses this step size for the first half of the range and
    # 	doubles the step size for the second half of the range
    ###########################################################################
    trip_distance_step_size = 22  # km
    income_step_size = 26000 # $
############################ THOUGHTS ###############################################

    # detail_flag indicates if the PKM associated with ALL points is to
    # 	be evaluated or if only those that pass the WTP condition should
    # 	be evaluated. Keep false unless you need to troubleshoot
    # 	something.
    detail_flag = False

    # Specify the filename which contains the list of cities and their
    # 	attributes. This is the primary input file.
    input_data = pd.read_excel('543_cities.xlsx')

    # Then, run this file. By running this file, you execute main().
    main(cases_list, input_data,
         trip_distance_step_size, income_step_size, detail_flag)

    # Once all cases and cities have been run, calculate the results
    #	summary. This will spit out another file in the results folder
    #	which contains the total pkm, pax trips, utilization, and
    #	vehicle trips by case (uam ticket cost and vertiport density)
    get_results_summary()
