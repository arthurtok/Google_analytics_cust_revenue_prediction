#!/Applications/anaconda/bin/python
# -*- coding: utf-8 -*-
"""
Code to 
"""
from json_flatten import flatten_df
import json

if __name__ == "__main__":
	file_path = '../Data/'

	JSON_COLUMNS = ['device', 'geoNetwork', 'totals', 'trafficSource']

	filenames = ['train.csv', 'test.csv']

	for filename in filenames:
		# Output the flattened dataframe into 
		df = flatten_df(csv_path=file_path + filename, 
				   		cols=JSON_COLUMNS, 
				   		nrows=None, 
				   		export=True, 
				   		export_path=None)
