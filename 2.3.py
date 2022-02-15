# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 14:40:03 2022

@author: bl4an
"""

import pandas as pd

df = pd.read_json('./read_json_sample.json')
print(df)
print()
print(df.index)