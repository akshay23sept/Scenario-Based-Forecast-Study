import pandas as pd
import glob


def get_results_summary():
    filenames_list = glob.glob('results/*.csv')

    out_df = pd.DataFrame()
    for filename in filenames_list:
        input_data = pd.read_csv(filename)
        file_str = filename.replace('.csv','')
        str_list = file_str.split('_')

        out_dict = {
			'uam_ticket_cost': str_list[1],
			'vertiport_density': str_list[2],
			'uam_pax_trips': input_data['uam_pax_trips'].sum(),
			'uam_pkt': input_data['uam_pkt'].sum(),
			'uam_utilization': input_data['uam_utilization'].sum(),
			'uam_vehicle_trips': input_data['uam_vehicle_trips'].sum()
		}
        out_df = out_df.append(out_dict, ignore_index=True)
		# print(filename+' done')

    out_df.to_csv('results/results_summary.csv')

if __name__ == '__main__':
	get_results_summary()
