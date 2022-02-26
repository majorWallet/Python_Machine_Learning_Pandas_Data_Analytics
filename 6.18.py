# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 23:06:37 2022

@author: bl4an
"""

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class'])

agg_grouped = grouped.apply(lambda x: x.describe())
print(agg_grouped)

def z_score(x):
    return (x - x.mean())/x.std()

age_zscore = grouped.age.apply(z_score)
print(age_zscore.head())

age_filter = grouped.apply(lambda x: x.age.mean() < 30)
print(age_filter)
print('\n')
for x in age_filter.index:
    if age_filter[x] == True:
        age_filter_df = grouped.get_group(x)
        print(age_filter_df.head())
        print('\n')