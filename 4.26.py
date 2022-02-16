# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 14:53:36 2022

@author: bl4an
"""

import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('darkgrid')

fig = plt.figure(figsize = (15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

sns.regplot(x='age',
            y='fare',
            data = titanic,
            ax=ax1)

sns.regplot(x='age',
            y='fare',
            data = titanic,
            ax=ax2,
            fit_reg=False)

plt.show()