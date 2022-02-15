# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 09:27:41 2022

@author: bl4an
"""

import pandas as pd

tup_data = ('영인', '2010-05-01', '여', True)
sr = pd.Series(tup_data, index = ['이름', '생년월일', '성별', '학생여부'])

print(sr)
print()

print(sr[0])
print(sr['이름'])
print()

print(sr[[1, 2]])
print(sr[['이름', '생년월일']])
print()

print(sr[1 : 2])
print(sr['생년월일' : '성별'])