import os
import csv
import glob
import random

if __name__ == '__main__':
    f = open('hcsp_new.csv', 'r')
    weather_data = csv.reader(f)
    training = []
    validation = []

    for row in weather_data:
        random_picked = random.randint(0,9)
        if random_picked == 0:
            validation.append(row)
        else:
            training.append(row)

    f_training = open('training.csv', 'wb')
    out_training = csv.writer(f_training)
    for row in training:
        out_training.writerow(row)

    f_validation = open('validation.csv', 'wb')
    out_validation = csv.writer(f_validation)
    for row in validation:
        out_validation.writerow(row)
