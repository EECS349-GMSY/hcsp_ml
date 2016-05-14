from datetime import datetime, date

start_summer_2015=datetime(2015, 6, 22)
end_summer_2015=datetime(2015, 8, 15)
start_fall_2015=datetime(2015, 9, 21)
end_fall_2015=datetime(2015, 12, 11)
start_winter_2015=datetime(2016, 1, 4)
end_winter_2015=datetime(2016, 3, 18)
start_spring_2015=datetime(2016, 3, 29)
end_spring_2015=datetime(2016, 6, 10)

def quarter_filler_func(attend):
	""" """
	for key in attend.keys():
		if(key>=start_summer_2015 and key<=end_summer_2015):
			attend[key].append(4)
			d0 = end_summer_2015
			d1 = start_summer_2015
			delta = d0-d1
			d2=key
			d3=start_summer_2015
			deltacurrent = d2 - d3
			attend[key].append(deltacurrent.days / delta.days)

		elif(key>=start_fall_2015 and key<=end_fall_2015):
			attend[key].append(1)
			d0=end_fall_2015
			d1=start_fall_2015
			delta=d0-d1
			d2=key
			d3=start_summer_2015
			deltacurrent = d2 - d3
			attend[key].append(deltacurrent.days/delta.days)

		elif(key>=start_winter_2015 and key<=end_winter_2015):
			attend[key].append(2)
			d0=end_winter_2015
			d1=start_winter_2015
			delta=d0-d1
			d2=key
			d3=start_summer_2015
			deltacurrent = d2 - d3
			attend[key].append(deltacurrent.days/delta.days)

		elif(key>=start_spring_2015 and key<=end_spring_2015):
			attend[key].append(3)
			d0=end_spring_2015
			d1=start_spring_2015
			delta=d0-d1
			d2=key
			d3=start_summer_2015
			deltacurrent = d2 - d3
			attend[key].append(deltacurrent.days/delta.days)

		else:
			attend[key].append(0)
			attend[key].append(0)

	return attend
