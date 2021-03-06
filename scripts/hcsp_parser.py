import math, time
from datetime import datetime, date, timedelta
import csv
import os
import glob
import pickle

# parse a single file of hcsp times
def parse_hcsp(filename, date_times):
	start = time.clock()

	f = open(filename, 'r')
	hcsp_data = csv.reader(f)
	i = 0
	for row in hcsp_data:
		if i > 0:
			#print str(row)
			[date_t] = row
			#print "DATE OBJECTTTTTT"
			#print str(date_t)
			[month_day, year_time] = date_t.split(",")
			[month_word, day] = month_day.split(" ")
			day = int(day)
			year_time = year_time[1:]
			[year, time_hm, ampm]  = year_time.split(" ")
			year = int(year)
			month = 0

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

			#cut times out of usual business hours
			if t_hour >= 6 and t_hour < 23:
				date_times.append(curr_dt)
		i = i + 1

	end = time.clock()
	print "PARSED " + filename + " IN " + str(end - start) + " SECONDS. "

	return date_times

# returns a list of filenames to be parsed
def get_filenames():
	curr_dir = os.getcwd()
	hcsp_dir = str(curr_dir) + '/data/hcsp/*.csv'   #full year dataset
	hcsp_files = glob.glob(hcsp_dir)
	hcsp_date_times = []
	for f_name in hcsp_files:
		hcsp_date_times = parse_hcsp(f_name, hcsp_date_times)

	return hcsp_date_times

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

def get_gym_numbers():
	gym_times = {}
	date_times = get_filenames()
	print "hcsp DATA PARSED"
	td = timedelta(minutes = 30)
	start = datetime(2015, 4, 1, 0, 0)
	end = datetime(2016, 4, 30, 23, 30)
	curr = start

	while (curr != end):
		if (curr.hour >= 6) and (curr.hour <= 23):
			gym_times[curr] = [0]
		curr = curr + td
	for i in range(0, len(date_times)):
		#print "IIIIIIIIII: " + str(i)
		(date_time1, date_time2) = round_time(date_times[i])
		#print str(date_times[i])
		gym_times[date_time1][0] = gym_times[date_time1][0] + 1
		if date_time2:
			gym_times[date_time2][0] = gym_times[date_time2][0] + 1
	return gym_times

def remove_zeros(gym_t):
	keys = gym_t.keys()
	for key in keys:
		if gym_t[key][0] == 0:
			del gym_t[key]
	return gym_t

def print_gym_times(gym_times):
	for key in gym_times.keys():
		print 'Date/Time: ' + str(key) + ', Number: ' + str(gym_times[key])

def gym_num_to_nom(gym_data):
	g_keys = gym_data.keys()
	#VALUES ARE CURRENTLY ARBITRARY AND WILL PROBABLY CHANGE
	for key in g_keys:
		if gym_data[key][0] < 50:
			gym_data[key][0] = 'Not Crowded'
		elif gym_data[key][0] < 100:
			gym_data[key][0] = 'Moderately Crowded'
		elif gym_data[key][0] < 150:
			gym_data[key][0] = 'Pretty Crowded'
		else:
			gym_data[key][0] = 'Jam Packed Very Crowded'

	return gym_data
# if __name__ == '__main__':
# 	s_data = get_filenames()
# 	print str(s_data[0])
# 	print "SIZE OF DATASET " + str(len(s_data))
