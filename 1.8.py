# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:38:00 2022

@author: bl4an
"""

import pandas as pd

exam_data = {'수학' : [90, 80, 70], '영어' : [98, 89, 95],
             '음악' : [85, 95, 100], '체육' : [100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print()

df4 = df[:]
df4.drop('수학', axis = 1, inplace = True)
print(df4)
print()

df5 = df[:]
df5.drop(['영어', '음악'], axis = 1, inplace = True)
print(df5)
print()