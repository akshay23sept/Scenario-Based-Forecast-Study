 #OASyS Project (Nov 2019 to Nov 2020)

  #Author: Akshay Anand
 




import pandas as pd
import numpy as np

input_data = pd.read_csv(
	'TripBulkReport-tripBulk_SYDNEY/metrics/data/TripDistanceMetrics.csv')
out_vec = ['trip_distance_km']

for index, row in input_data.iterrows():
	count = row['trip_count'].astype(np.int64)
	dist_value = row['trip_distance_m'].astype(np.int64)/1000
	for x in range(count):
		out_vec.append(dist_value)
out_data = pd.Series(out_vec)
out_data.to_csv(
	'TripBulkReport-tripBulk_SYDNEY/metrics/data/TD_hist.csv',
	index=False)
