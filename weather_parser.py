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
        [station, valid, tmpf , relh , sped , p01i , skyc1 , skyc2 , skyc3] = row
        datetime_object = datetime.strptime(valid, "%Y-%m-%d %H:%M")
        weather.append([datetime_object, tmpf ,  relh ,  sped ,  p01i ,  skyc1 ,  skyc2 ,  skyc3])

    return weather
