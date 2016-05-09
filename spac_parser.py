
import math, time
from datetime import datetime, date

def parseSpac(filename, lines):
    start = time.clock()

    spac_data = open(filename, 'r')
    date_times = []
    first_line = spac_data.readline()

    for i in range(0, lines):
        print str(i)
        [location, month_day, year_time, empt, emp, em] = spac_data.readline().split(",")
        month_day = month_day[1:]
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
            t_hour = t_hour + 12

        t_hour = int(t_hour)
        t_min = int(t_min)
        curr_dt = datetime(year, month, day, t_hour, t_min)
        date_times.append(curr_dt)
    
    end = time.clock()
    print "PARSED IN " + str(end - start) + " SECONDS. "

    return date_times

