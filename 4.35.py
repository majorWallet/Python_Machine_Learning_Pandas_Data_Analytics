# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 14:54:27 2022

@author: bl4an
"""

import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('whitegrid')

titanic_pair = titanic[['age', 'pclass', 'fare']]

g = sns.pairplot(titanic_pair)