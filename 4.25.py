# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 14:48:27 2022

@author: bl4an
"""

import seaborn as sns

titanic = sns.load_dataset('titanic')

print(titanic.head())
print('\n')
print(titanic.info())