# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 13:34:40 2022

@author: bl4an
"""

import pandas as pd
import numpy as np

student1 = pd.Series({'국어' : np.nan, '영어' : 80, '수학' : 90})
student2 = pd.Series({'수학' : 80, '국어' : 90})

print(student1)
print()
print(student2)
print()

addition = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
division = student1 / student2
print(type(division))
print()

result = pd.DataFrame([addition, subtraction, multiplication, division], index = ['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)