# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 14:51:47 2022

@author: bl4an
"""

import pandas as pd

url = './sample.html'

tables = pd.read_html(url)

print(len(tables))
print()

for i in range(len(tables)):
    print("tables[%s]" % i)
    print(tables[i])
    print('\n')
    
df = tables[1]

df.set_index(['name'], inplace = True)
print(df)