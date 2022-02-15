# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 21:04:51 2022

@author: bl4an
"""

import pandas as pd

data = {'name' : ['Jerry', 'Riah', 'Paul'],
        'algol' : ["A", "A+", "B"],
        'basic' : ["C", "B", "B+"],
        'c++' : ["B+", "C", "C+"]
        }

df = pd.DataFrame(data)
df.set_index('name', inplace = True)
print(df)

df.to_excel("./df_sample.xlsx")