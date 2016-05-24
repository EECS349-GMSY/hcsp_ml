
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
        if key in weath:
            curr_gq_0 = gq_data[key][0]
            curr_gq_1 = gq_data[key][1]
            curr_gq_2 = gq_data[key][2]
            curr_w = weath[key]
            curr_w.insert(0, curr_gq_2)
            curr_w.insert(0, curr_gq_1)
            curr_w.insert(0, curr_gq_0)
            gq_data[key] = curr_w
    return gq_data

def compile_data(output_nom = False):
    gym_nums = get_gym_numbers()
    #convert attendence to nominal if output_nom == True
    if output_nom:
        gym_nums = gym_num_to_nom(gym_nums)

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

def output_to_csv(filename = 'output/hcsp_big.csv', output_nom = False):
    swq_data = {}

    pickle_path = 'pickled_data.dat'
    if output_nom:
        pickle_path = 'pickled_data_nom.dat'
    if os.path.isfile(pickle_path):
        print "Fetching dictionary from pickled_data.dat"
        swq_data = load(pickle_path)

    else:
        print "Parsing data to make dictionary"
        swq_data = compile_data(output_nom)
        s = save(swq_data,pickle_path)
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

#############################################################
#### -- The following 2 functions were brought from EECS 348 Assignment 3
#### -- Credit to Prof. Sara Sood, EECS 348 TAs for the writing the following functions
def save(dObj, sFilename):
	f = open(sFilename, "w")
	p = pickle.Pickler(f)
	p.dump(dObj)
	f.close()

def load(sFilename):
	f = open(sFilename, "r")
	u = pickle.Unpickler(f)
	dObj = u.load()
	f.close()
	return dObj
################################################################

if __name__ == '__main__':
    #this one will put the attendence into a 5 nominal values
    #output_to_csv(filename = 'output/hcsp_big_nom.csv', output_nom = True)

    #this one will run the standard output to csv
    output_to_csv()
