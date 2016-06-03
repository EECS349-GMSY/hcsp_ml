import math, time
from datetime import datetime, date
import csv
import os
import glob

def weather_parser(filename):
    """ """
    f = open(filename, 'r')
    weather_data = csv.reader(f)
    weather = []

    for row in weather_data:
        #station	valid	tmpf	relh	sped	p01i	skyc1	skyc2	skyc3
        [station, valid, tmpf , relh , sped , p01i , skyc1 , skyc2 , skyc3] = row
        datetime_object = datetime.strptime(valid, "%Y-%m-%d %H:%M")
        if datetime_object.hour >= 6 and datetime_object.hour <= 23:
            #cut entries between 23:00 and 06:00
            datetime_object = datetime_object.replace(minute=00)
            weather.append([datetime_object, tmpf ,  relh ,  sped ,  p01i ,  skyc1 ,  skyc2 ,  skyc3])
            datetime_object2 = datetime_object.replace(minute=30)
            weather.append([datetime_object2, tmpf ,  relh ,  sped ,  p01i ,  skyc1 ,  skyc2 ,  skyc3])
    return weather
