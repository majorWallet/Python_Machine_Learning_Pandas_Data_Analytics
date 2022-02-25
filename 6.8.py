# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 11:52:29 2022

@author: bl4an
"""

import pandas as pd

df = pd.read_excel('./주가데이터.xlsx')
print(df.head(), '\n')
print(df.dtypes, '\n')

df['연월일'] = df['연월일'].astype('str')
dates = df['연월일'].str.split('-')
print(dates.head(), '\n')

df['연'] = dates.str.get(0)
df['월'] = dates.str.get(1)
df['일'] = dates.str.get(2)
print(df.head())