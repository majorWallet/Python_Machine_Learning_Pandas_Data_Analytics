# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 15:23:44 2022

@author: bl4an
"""

import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('darkgrid')

fig = plt.figure(figsize = (15, 5))
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)

sns.distplot(titanic['fare'], ax = ax1)
sns.distplot(titanic['fare'], hist = False, ax = ax2)
sns.distplot(titanic['fare'], kde = False, ax = ax3)

ax1.set_title('titanic fare - hist/ked')
ax2.set_title('titanic fate - ked')
ax3.set_title('titanic fare - hist')