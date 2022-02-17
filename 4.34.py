# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 14:39:40 2022

@author: bl4an
"""

import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('whitegrid')

g = sns.FacetGrid(data = titanic, col = 'who', row = 'survived')

g = g.map(plt.hist, 'age')