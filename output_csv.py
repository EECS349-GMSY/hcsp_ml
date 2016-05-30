
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

def compile_data(output_nom = False, rem_0 = False):
    gym_nums = get_gym_numbers()
    #convert attendence to nominal if output_nom == True
    if output_nom:
        gym_nums = gym_num_to_nom(gym_nums)

    if rem_0:
        gym_nums = remove_zeros(gym_nums)

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

def output_to_csv(filename = 'output/hcsp_big.csv', output_nom = False, rem_0 = False):
    swq_data = {}
    #GET THE DATA IF PICKLED
    pickle_path = 'pickled_data.dat'
    if output_nom:
        if rem_0:
            pickle_path = 'pickled_data_nom_no_zeros.dat'
        else:
            pickle_path = 'pickled_data_nom.dat'
    elif not output_nom and rem_0:
        pickle_path = 'pickled_data_no_zeros.dat'

    if os.path.isfile(pickle_path):
        print "Fetching dictionary from pickled_data.dat"
        swq_data = load(pickle_path)
    #Otherwise parse the data
    else:
        print "Parsing data to make dictionary"
        swq_data = compile_data(output_nom, rem_0)
        s = save(swq_data,pickle_path)
        print "DATA COMPILED "
    f = open(filename, 'wb')
    out_f = csv.writer(f)

    start = time.clock()
    header_row = ['Datetime', 'Attendence', 'Place in Quarter', 'W1', 'W2','W3','W4','W5','W6','W7', 'W8']
    out_f.writerow(header_row)
    for key in swq_data.keys():
        curr_row = swq_data[key]
        #print "CURR ROW LENGTH: " + str(len(curr_row))
        if len(curr_row) == 10:
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
    output_to_csv(filename = 'output/hcsp_big_nom.csv', output_nom = True, rem_0 = False)

    #this one will run the standard output to csv
    output_to_csv()

    #this one will run numeric attendence without zeros
    output_to_csv(filename = 'output/hcsp_big_no_zeros.csv', output_nom = False, rem_0 = True)

    #this one will run nominal attendence without zeros
    output_to_csv(filename = 'output/hcsp_big_nom_no_zeros.csv', output_nom = True, rem_0 = True)
