# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 10:20:24 2022

@author: bl4an
"""

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header = None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

df.plot(x='weight', y = 'mpg', kind = 'scatter')