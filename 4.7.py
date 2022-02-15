# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 11:43:25 2022

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

plt.style.use('ggplot')

plt.figure(figsize = (14, 5))

plt.xticks(size = 10, rotation = 'vertical')


plt.plot(sr_one.index, sr_one.values, marker = 'o', markersize = 10)

plt.title('서울 -> 경기 인구 이동', size = 30)
plt.xlabel('기간', size = 20)
plt.ylabel('이동 인구수', size = 20)

plt.legend(labels = ['서울 -> 경기'], loc = 'best', fontsize = 15)

plt.ylim(50000, 800000)

plt.annotate('',
             xy = (20, 620000),     #화살표의 머리 부분(끝점)
             xytext = (2, 290000),  #화살표의 꼬리 부분(시작점)
             xycoords = 'data',     #좌표체계
             arrowprops = dict(arrowstyle = '->', color = 'skyblue', lw = 5))   #화살표 서식

plt.annotate('',
             xy = (47, 450000),     #화살표의 머리 부분(끝점)
             xytext = (30, 580000),  #화살표의 꼬리 부분(시작점)
             xycoords = 'data',     #좌표체계
             arrowprops = dict(arrowstyle = '->', color = 'olive', lw = 5))   #화살표 서식

plt.annotate('인구 이동 증가(1970-1995)', #텍스트 입력
             xy = (10, 400000), #텍스트 위치 기준점
             rotation = 25, #텍스트 회전 각도
             va = 'baseline', #텍스트 상하 정렬
             ha = 'center', #텍스트 좌우 정렬
             fontsize=15) #텍스트 크기

plt.annotate('인구 이동 감소(1995-2017)', #텍스트 입력
             xy = (40, 500000), #텍스트 위치 기준점
             rotation = -11, #텍스트 회전 각도
             va = 'baseline', #텍스트 상하 정렬
             ha = 'center', #텍스트 좌우 정렬
             fontsize=15) #텍스트 크기

plt.show()