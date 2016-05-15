
import math, time
from datetime import datetime, date, timedelta
import csv
import os
import glob
from spac_parser import *
from weather_parser import *
from quarter_filler import *


def weather_to_dict(weather_list):
    w_dict = {}
    for w in weather_list:
        dt = w[0]
        w_dict[dt] = w[1:]
    return w_dict


def add_weather_to_gym(gq_data, weath):
    for key in gq_data.keys():
        if key in weath.keys():
            curr_gq_0 = gq_data[key][0]
            curr_gq_1 = gq_data[key][1]
            curr_gq_2 = gq_data[key][2]
            # if(curr_gq == None):
            #     print "GQGQGQGQGQGQGQGQGQ"
            curr_w = weath[key]
            curr_w.insert(0, curr_gq_2)
            curr_w.insert(0, curr_gq_1)
            curr_w.insert(0, curr_gq_0)
            # if(curr_w == None):
            #     print "NOTTTTTTT GOOOODDDDD"
            gq_data[key] = curr_w
    return gq_data

def compile_data():
    raw_spac_data = get_filenames()
    print "SPAC DATA PARSED"
    gym_nums = get_gym_numbers(raw_spac_data)
    #print(gym_nums)
    gym_quart = quarter_filler_func(gym_nums)
    print 'LEN ' + str(len(gym_quart.keys()))
    #print str(gym_quart)
    w_file = 'data/weather_jan2015_may2016.csv'
    w_list = weather_parser(w_file)
    w_dict = weather_to_dict(w_list)
    s_w_q_data = add_weather_to_gym(gym_quart, w_dict)
    return s_w_q_data

def check_data(swq):
    for key in swq.keys():
        if swq[key] == None:
            print 'BREAKKKKDJDJDJD'
    return 0

# def print_dict(dict):
#     for key in dict.keys():

def output_to_csv(filename = 'hcsp.csv'):
    swq_data = compile_data()
    print "DATA COMPILED "
    f = open(filename, 'wb')
    out_f = csv.writer(f)

    start = time.clock()
    for key in swq_data.keys():
        curr_row = swq_data[key]
        #print str(curr_row)
        curr_row.insert(0, str(key))
        out_f.writerow(curr_row)

    end = time.clock()
    print "COMPLETED OUTPUT TO CSV in " + str(end - start) + " seconds "
    return 0


if __name__ == '__main__':
    output_to_csv()
