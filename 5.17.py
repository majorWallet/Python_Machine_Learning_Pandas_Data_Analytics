# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 13:45:15 2022

@author: bl4an
"""

import pandas as pd

ts_ms = pd.date_range(start = '2019-01-01',
                      end = None,
                      periods = 6,
                      freq = 'MS',
                      tz = 'Asia/Seoul')
print(ts_ms)

ts_me = pd.date_range('2019-01-01', periods = 6,
                      freq = 'M',
                      tz = 'Asia/Seoul')

print(ts_me)
print('\n')

ts_3m = pd.date_range('2019-01-01', periods = 6,
                      freq = '3M',
                      tz = 'Asia/Seoul')

print(ts_3m)
print('\n')