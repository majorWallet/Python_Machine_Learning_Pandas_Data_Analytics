# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 09:06:49 2022

@author: bl4an
"""

import pandas as pd

df = pd.read_csv("./auto-mpg.csv", header = None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horespower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print(df.head())
print(df.tail())

print(df.shape)

print(df.info())

print(df.describe())
print(df.describe(include = 'all'))