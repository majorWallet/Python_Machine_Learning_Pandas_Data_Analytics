# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 20:34:03 2022

@author: bl4an
"""

import googlemaps #import API
import pandas as pd #import pandas

my_key = "AIzaSyAY_2kzhOqItGM-RjSpAHhS8_kiYTGq_Ow" #API Key

maps = googlemaps.Client(key = my_key) #API에 Key 입력 한 후에 API인스턴스를 maps에 저장

lat = [] #위도
lng = [] #경도

places = ["서울시청", "국립국악원", "해운대해수욕장"]

i = 0
for place in places:
    i += 1
    try:
        print(i, place) #횟수, 장소
        geo_location = maps.geocode(place)[0].get('geometry') #지오코딩 API 결과값 호출하여 geo_location 변수에 저장
        lat.append(geo_location['location']['lat'])
        lng.append(geo_location['location']['lng'])
        
    except:
        lat.append('')
        lng.append('')
        print(i)
        
df = pd.DataFrame({'위도' : lat, '경도' : lng}, index = places)
print('\n')
print(df)