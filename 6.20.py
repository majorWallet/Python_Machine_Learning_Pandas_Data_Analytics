# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 11:43:27 2022

@author: bl4an
"""

import pandas as pd
import seaborn as sns

pd.set_option('display.max.columns', 10)
pd.set_option('display.max.colwidth', 20)

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
print(df.head())
print('\n')

pdf1 = pd.pivot_table(df,
                      index = 'class',
                      columns = 'sex',
                      values = 'age',
                      aggfunc = 'mean')

print(pdf1.head())
print('\n')

pdf2 = pd.pivot_table(df,
                      index = 'class',
                      columns = 'sex',
                      values = 'age',
                      aggfunc = ['mean', 'sum'])

print(pdf2.head())
print('\n')

pdf3 = pd.pivot_table(df,
                      index = ['class', 'sex'],
                      columns = 'survived',
                      values = ['age', 'fare'],
                      aggfunc = ['mean', 'max'])

print(pdf3.head())
print('\n')

print(pdf3.xs('First'))
print('\n')

print(pdf3.xs(('First', 'female')))
print('\n')

print(pdf3.xs('male', level = 'sex'))
print('\n')

print(pdf3.xs(('Second', 'male'), level = ['class', 'sex']))
print('\n')

print(pdf3.xs('mean', axis = 1))
print('\n')

print(pdf3.xs(('mean', 'age'), axis = 1))
print('\n')

print(pdf3.xs(1, level = 'survived', axis = 1))
print('\n')

print(pdf3.xs(('max', 'fare', 0),
      level = [0, 1, 2], axis = 1))