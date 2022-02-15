# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 14:27:53 2022

@author: bl4an
"""

import pandas as pd

file_path = './read_csv_sample.csv'

df1 = pd.read_csv(file_path)
print(df1)
print()

df2 = pd.read_csv(file_path, header = None)
print(df2)
print()

df3 = pd.read_csv(file_path, index_col = None)
print(df3)
print()

df4 = pd.read_csv(file_path, index_col = 'c0')
print(df4)
print()