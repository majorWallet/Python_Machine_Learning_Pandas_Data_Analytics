# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 14:20:18 2022

@author: bl4an
"""

import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('whitegrid')

j1 = sns.jointplot(x = 'fare', y = 'age', data = titanic)
j2 = sns.jointplot(x = 'fare', y = 'age', kind = 'reg', data = titanic)
j3 = sns.jointplot(x = 'fare', y = 'age', kind = 'hex', data = titanic)
j4 = sns.jointplot(x = 'fare', y = 'age', kind = 'kde', data = titanic)

j1.fig.suptitle('titanic fare - scatter', size = 15)
j2.fig.suptitle('titanic fare - reg', size = 15)
j2.fig.suptitle('titanic fare - hex', size = 15)
j2.fig.suptitle('titanic fare - kde', size = 15)

plt.show()