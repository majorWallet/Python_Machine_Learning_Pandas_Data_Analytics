# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 13:20:13 2022

@author: bl4an
"""

import pandas as pd

dict_data = {'c0' : [1,2,3], 'c1' : [4,5,6], 'c2' : [7,8,9], 'c3' : [10,11,12], 'c4' : [13,14,15]}

df = pd.DataFrame(dict_data, index = ['r0', 'r1', 'r2'])
print(df)
print()

ndf = df.sort_values(by = 'c1', ascending = False)
print(ndf)