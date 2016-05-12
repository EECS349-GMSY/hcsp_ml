
import math, time
from datetime import datetime, date, timedelta
import csv
import os
import glob

# parse a single file of spac times
def parse_spac(filename, date_times):
    start = time.clock()

    f = open(filename, 'r')
    #date_times = []
    spac_data = csv.reader(f)
    #first_line = spac_data.readline()
    i = 0
    for row in spac_data:
        if i > 0:
            [location, date_t, qty] = row
            [month_day, year_time] = date_t.split(",")
            # month_day = month_day[1:]
            [month_word, day] = month_day.split(" ")
            day = int(day)
            year_time = year_time[1:]
            [year, time_hm, ampm]  = year_time.split(" ")
            year = int(year)
            month = 0
            #print month_word

            if month_word == 'Jan':
                month = 1
            elif month_word == 'Feb':
                month = 2
            elif month_word == 'Mar':
                month = 3
            elif month_word == 'Apr':
                month = 4
            elif month_word == 'May':
                month = 5
            elif month_word == 'Jun':
                month = 6
            elif month_word == 'Jul':
                month = 7
            elif month_word == 'Aug':
                month = 8
            elif month_word == 'Sep':
                month = 9
            elif month_word == 'Oct':
                month = 10
            elif month_word == 'Nov':
                month = 11
            elif month_word == 'Dec':
                month = 12
            else:
                print "ERROR IN MONTH"

            [t_hour, t_min] = time_hm.split(":")
            if ampm == 'PM':
                if t_hour != '12':
                    t_hour = int(t_hour) + 12
            #print "HOUR" + str(t_hour)
            t_hour = int(t_hour)
            t_min = int(t_min)
            curr_dt = datetime(year, month, day, t_hour, t_min)
            date_times.append(curr_dt)
        i = i + 1

    end = time.clock()
    print "PARSED IN " + str(end - start) + " SECONDS. "

    return date_times

# returns a list of filenames to be parsed
def get_filenames():
    curr_dir = os.getcwd()
    #print curr_dir
    spac_dir = str(curr_dir) + '/spac_rev/*.csv'
    spac_files = glob.glob(spac_dir)
    #print spac_dir
    spac_date_times = []
    for f_name in spac_files:
        spac_date_times = parse_spac(f_name, spac_date_times)

    return spac_date_times

def round_time(date_time):
	if date_time.minute == 0 or date_time.minute == 30:
		return (date_time, None)
	elif date_time.minute < 30:
		new1 = date_time.replace(minute = 0)
		new2 = date_time.replace(minute = 30)
		return (new1, new2)
	else:
		new1 = date_time.replace(minute = 30)
		new2 = date_time.replace(minute = 0)
		new2 = new2 + timedelta(hours = 1)
		return (new1, new2)

def get_gym_numbers(date_times):
	td = timedelta(minutes = 30)
	start = datetime(2015, 1, 1)
	end = datetime(2016, 1, 1)
	curr = start
	gym_times = {}
	while (curr != end):
		gym_times[curr] = [0]
		curr = curr + td
	for i in range(0, len(date_times)):
		(date_time1, date_time2) = round_time(date_times[i])
		gym_times[date_time1][0] = gym_times[date_time1][0] +1
		if date_time2:
			gym_times[date_time2][0] = gym_times[date_time2][0] + 1
	return gym_times

def print_gym_times(gym_times):
	for key in gym_times.keys():
		print 'Date/Time: ' + str(key) + ', Number: ' + str(gym_times[key])

#if __name__ == '__main__':
    #s_data = get_filenames()
    #print str(s_data[0])
    #print "SIZE OF DATASET" + str(len(s_data))
