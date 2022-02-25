# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 16:23:55 2022

@author: bl4an
"""

import pandas as pd

pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 20)
pd.set_option('display.unicode.east_asian_width', True)

df1 = pd.read_excel('./stock price.xlsx', index_col = 'id')
df2 = pd.read_excel('./stock valuation.xlsx', index_col = 'id')

df3 = df1.join(df2)
print(df3)

df4 = df1.join(df2, how = 'inner')
print(df4)