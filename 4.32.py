# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:57:07 2022

@author: bl4an
"""

import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('whitegrid')

fig = plt.figure(figsize = (15, 10))
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

sns.boxplot(x = 'alive', y = 'age', data = titanic, ax = ax1)
sns.boxplot(x = 'alive', y = 'age', hue = 'sex', data = titanic, ax = ax2)
sns.violinplot(x='alive', y='age', data = titanic, ax = ax3)
sns.violinplot(x='alive', y='age', hue = 'sex', data = titanic, ax = ax4)

plt.show()