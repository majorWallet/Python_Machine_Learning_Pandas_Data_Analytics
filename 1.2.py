# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 09:19:30 2022

@author: bl4an
"""

import pandas as pd

list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
print(sr)

print(sr.index)
print()
print(sr.values)