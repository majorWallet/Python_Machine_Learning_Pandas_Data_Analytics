# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 13:29:07 2022

@author: bl4an
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = "./malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

df = pd.read_excel('./시도별 전출입 인구수.xlsx', header = 0)
df = df.fillna(method = 'ffill')
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis = 1)
df_seoul.rename({'전입지별' : '전입지'}, axis = 1, inplace = True)
df_seoul.set_index('전입지', inplace = True)
sr_one = df_seoul.loc['경기도']

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(1,1,1)

ax.plot(sr_one, marker = 'o', markerfacecolor = 'orange', markersize = 10, color = 'olive', linewidth=2, label = '서울->경기')
ax.legend(loc='best')

ax.set_ylim(50000, 800000)

ax.set_title('서울 -> 경기 인구 이동', size = 20)

ax.set_xlabel('기간', size=12)
ax.set_ylabel('이동 인구수', size=12)

ax.set_xticklabels(sr_one.index, rotation = 75)

ax.tick_params(axis = "x", labelsize = 10)
ax.tick_params(axis = "y", labelsize = 10)

plt.show()