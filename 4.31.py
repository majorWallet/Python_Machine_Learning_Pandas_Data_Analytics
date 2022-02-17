# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:45:37 2022

@author: bl4an
"""

import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('whitegrid')

fig = plt.figure(figsize = (15, 5))
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)

sns.countplot(x='class', palette = 'Set1', data = titanic, ax = ax1)
sns.countplot(x='class', hue = 'who', palette = 'Set2', data = titanic, ax=ax2)
sns.countplot(x='class', hue = 'who', palette = 'Set3', dodge = False, data = titanic, ax = ax3)

ax1.set_title('titanic Class')
ax2.set_title('titanic Class - who')
ax3.set_title('titanic Class - who(stacked)')

plt.show()