# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:45:47 2022

@author: bl4an
"""

import pandas as pd

dict_data = {'a' : 1, 'b' : 2, 'c' : 3}

sr = pd.Series(dict_data)

print(type(sr))
print('\n')
print(sr)