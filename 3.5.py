# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 10:09:08 2022

@author: bl4an
"""

import pandas as pd

df = pd.read_excel('./남북한발전전력량.xlsx')

df_ns = df.iloc[[0, 5], 3:]
df_ns.index = ['South', 'North']
df_ns.columns = df_ns.columns.map(int)

df_ns.T.plot(kind='bar')