#!/Applications/anaconda/bin/python
# -*- coding: utf-8 -*-
"""
Script to flatten JSON fields into a csv
"""

import json
import os
import pandas as pd
import numpy as np
import time
from pandas.io.json import json_normalize

def flatten_df(csv_path, 
			   cols, 
			   nrows=None,
			   export=False, 
			   export_path=None):
	"""
	Parameters
	----------
	csv_path: Absolute or relative path to the data.

	cols: Columns containing JSON fields to flatten.

	export: Optional argument to export 

	nrows: Specify number of rows to flatten. Defaults to None.

	Returns
	-------
	df: Dataframe of flattened Json columns

	"""
	start_time = time.time()

	JSON_COLUMNS = cols

	df = pd.read_csv(filepath_or_buffer=csv_path,
					 converters={column: json.loads for column in JSON_COLUMNS},
					 dtype={'fullVisitorId': 'str'},
					 nrows=nrows)

	for column in JSON_COLUMNS:
		column_as_df = json_normalize(df[column])
		# Set the column names
		column_as_df.columns = ["{0}_{1}".format(column, subcol) 
											for subcol in column_as_df.columns]
		df = df.drop(column, axis=1).merge(column_as_df,
										   right_index=True,
										   left_index=True)
	print("Loaded {0}. Shape: {1}".format(os.path.basename(csv_path), df.shape))
	print("="*80)
	print("Json flattening completed in time: {}s".format(time.time() - start_time))

	# Code to export the csv file
	if export and export_path is not None:
		df.to_csv(export_path, index=False)

	return df

