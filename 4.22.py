# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 13:42:57 2022

@author: bl4an
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

cylinder_size = df.cylinders/df.cylinders.max() * 300

df.plot(kind = 'scatter', x = 'weight', y = 'mpg', marker = '+', cmap = 'viridis', c = cylinder_size, figsize = (10,5), alpha = 0.3, s=50)
plt.title('Scatter Plot: mpg-weight-cylinders')
plt.show()
