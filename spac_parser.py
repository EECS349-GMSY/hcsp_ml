
import math, time
from datetime import datetime, date
import csv
# parse a single file of spac times
def parse_spac(filename, lines):
    start = time.clock()

    f = open(filename, 'r')
    date_times = []
    spac_data = csv.reader(f)
    #first_line = spac_data.readline()
    i = 0
    for row in spac_data:
    #with open(filename) as spac_data:
        #print row
        #print str(i)
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
    return []

if __name__ == '__main__':
    f_s0 = 'spac_rev/Sep01_13.csv'
    l_s0 = 1000
    dt = parse_spac(f_s0, l_s0)
    print str(dt)
