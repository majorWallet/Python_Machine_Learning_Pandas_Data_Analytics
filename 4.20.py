# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 13:27:47 2022

@author: bl4an
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

df.plot(kind = 'scatter', x = 'weight', y = 'mpg', c = 'coral', s = 10, figsize = (10,5))
plt.title('Scatter Plot - mpg vs weight')
plt.show()
