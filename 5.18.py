# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 14:01:01 2022

@author: bl4an
"""

import pandas as pd

pr_m = pd.period_range(start = '2019-01-01',
                       end = None,
                       periods = 3,
                       freq = 'M')
print(pr_m)

pr_h = pd.period_range(start = '2019-01-01',
                       end = None,
                       periods = 3,
                       freq = 'H')
print(pr_h)

pr_3h = pd.period_range(start = '2019-01-01',
                       end = None,
                       periods = 3,
                       freq = '3H')
print(pr_3h)