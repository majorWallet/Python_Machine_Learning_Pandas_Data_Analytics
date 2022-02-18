# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 16:38:39 2022

@author: bl4an
"""

import pandas as pd

df = pd.DataFrame({'c1' : ['a', 'a', 'b', 'a', 'b'],
                   'c2' : [1, 1, 1, 2, 2],
                   'c3' : [1, 1, 2, 2, 2]})

print(df)
print('\n')

df2 = df.drop_duplicates()
print(df2)
print('\n')

df3 = df.drop_duplicates(subset=['c2', 'c3'])
print(df3)