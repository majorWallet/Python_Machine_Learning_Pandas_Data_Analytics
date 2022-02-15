# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 13:23:53 2022

@author: bl4an
"""

import pandas as pd

student1 = pd.Series({'국어' : 100, '영어' : 80, '수학' : 90})
print(student1)
print('\n')

percentage = student1 / 200

print(percentage)