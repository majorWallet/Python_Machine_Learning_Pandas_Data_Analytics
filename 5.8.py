# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 16:43:49 2022

@author: bl4an
"""

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header = None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']
print(df.head(3))
print('\n')

mpg_to_kpl = 1.60934/3.78541

df['kpl'] = df['mpg'] * mpg_to_kpl
print(df.head(3))
print('\n')

df['kpl'] = df['kpl'].round(2)
print(df.head(3))