import numpy as np
import sqlite3
import pygal
import datetime
import random
import math
import os
pygal.Bar()(1, 3, 3, 7)(1, 6, 6, 4).render()
exit
max_temp=25
min_temp=-5
curr_date = datetime.datetime(2020, 3, 1) 
end_date = datetime.datetime(2020, 11, 20)
days=0
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) 

with sqlite3.connect('weather_data_generation.db') as db:
    print("Opened database successfully")
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather_data_temperature(
    date DATE NOT NULL, 
    temperature INTERGER NOT NULL) ;''')

def count_days(start_date, end_date, ):
    day_counter=0
    while (start_date != end_date): 
        start_date += datetime.timedelta(days=1)
        day_counter += 1
    day_counter += 1
    return day_counter
    
def generate_rnd_num_for_bell(count):
    rnd_nums=[]
    for x in range(0, count):
        rnd_nums.append(random.random()) 
    rnd_nums.sort()
    return rnd_nums

def rnd_nums_to_bell_nums(rnd_nums):
    bell_nums=[]
    for x in range(0,len(rnd_nums)):
        bell_nums.append(bell_equation(rnd_nums[x]))
    return bell_nums

def bell_equation(input_num):
    return (math.sin(2 * math.pi * (input_num - 1/4)) + 1) / 2

def bell_to_temp(numbers,min_temp,max_temp):
    max_temp= max_temp + (min_temp * -1)
    return_temps=[]
    for x in range(0,len(numbers)):
        return_temps.append((numbers[x]* max_temp)- (min_temp * -1))  
    return return_temps

def randomize_weather_data(original_temps):
    new_temps=[]
    for x in range(0, len(original_temps)): 
        if(random.random()>=0.5):         
            new_temps.append(original_temps[x] -5)
        else:
            new_temps.append(original_temps[x] +5)
    return new_temps


def insertVariblesIntoTable(date, temperature):
    mySql_insert_query = """INSERT INTO weather_data_temperature (date, temperature) 
                                VALUES (?, ?) """
    recordTuple = (date, temperature)
    cursor.execute(mySql_insert_query, recordTuple)
    db.commit()


all_days=count_days(curr_date,end_date) 

rnd_nums=generate_rnd_num_for_bell(all_days)

bell_nums=rnd_nums_to_bell_nums(rnd_nums)

temp_nums=bell_to_temp(bell_nums,min_temp,max_temp)

day_to_calculate=curr_date

for x in range(0, all_days):
    date1 = day_to_calculate.strftime("%d.%m.%Y") 
    temperature1 = str(temp_nums[x])
    day_to_calculate += datetime.timedelta(days=1)
    insertVariblesIntoTable(date1,temperature1)
    





