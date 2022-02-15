# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 12:02:24 2022

@author: bl4an
"""

import pandas as pd

exam_data = {'이름' : ['서준', '우현', '인아'],
             '수학' : [90, 80, 70],
             '영어' : [98, 89, 95],
             '음악' : [85, 95, 100],
             '체육' : [100, 90, 90]}
df = pd.DataFrame(exam_data)

df.set_index('이름', inplace=True)
print(df)
print()

df = df.transpose()
print(df)
print()

df = df.T
print(df)