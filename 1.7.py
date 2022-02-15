# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:24:35 2022

@author: bl4an
"""

import pandas as pd

exam_data = {'수학' : [90, 80, 70], '영어' : [98, 89, 95],
             '음악' : [85, 95, 100], '체육' : [100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print()

df2 = df[:]
df2.drop('우현', inplace = True)
print(df2)
print()

df3 = df[:]
df3.drop(['우현', '인아'], inplace = True)
print(df3)
print()
