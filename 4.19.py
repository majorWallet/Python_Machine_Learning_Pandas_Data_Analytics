# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 11:45:54 2022

@author: bl4an
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('classic')

df = pd.read_csv('./auto-mpg.csv', header = None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

df['mpg'].plot(kind = 'hist', bins = 10, color = 'coral', figsize = (10, 5))

plt.title("HIstogram")
plt.xlabel('mpg')
plt.show()