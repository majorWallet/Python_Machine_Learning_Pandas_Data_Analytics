# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 15:49:47 2022

@author: bl4an
"""

import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('darkgrid')

table = titanic.pivot_table(index = ['sex'], columns = ['class'], aggfunc = 'size')

sns.heatmap(table,
            annot=True, fmt = 'd',
            camp = 'YlGnBu',
            linewidth = 5,
            cbar = False)

plt.show()