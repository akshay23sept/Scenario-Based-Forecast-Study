 #OASyS Project (Nov 2019 to Nov 2020)

 
  #Author: Akshay Anand


import pandas as pd 
from fuzzywuzzy import process
from fuzzywuzzy import fuzz

def main(primary_table_filename, secondary_table_filename, primary_table_col_name, secondary_table_col_name):
	main_table = pd.read_excel(primary_table_filename + '.xlsx')
	secondary_table = pd.read_excel(secondary_table_filename + '.xlsx')

	choices = secondary_table[secondary_table_col_name].values.tolist()

	main_table['Closest Entry'] = main_table[primary_table_col_name].apply(lambda x: process.extractOne(x, choices))
	main_table[['Closest Entry', 'Percent Match']] = main_table['Closest Entry'].apply(pd.Series)

	merged = pd.merge(main_table, secondary_table, left_on='Closest Entry', right_on=secondary_table_col_name, how='left')

	merged.to_excel(primary_table_filename + '-merged with-' + secondary_table_filename + '.xlsx')

if __name__ == '__main__':
	primary_table_filename = 'cities'
	primary_table_col_name = 'city'

	secondary_table_filename = 'masterslim'
	secondary_table_col_name = 'Urban Area'

	main(primary_table_filename, secondary_table_filename, primary_table_col_name, secondary_table_col_name)