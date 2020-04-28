import sqlite3
import random
import string
import datetime
import math
import os
# Please assure your path is correct to the derired directory and in the correct database file #
Path = 'c:\\Users\\Andreas\\Desktop\\Uni\\Farm'
conn = sqlite3.connect('auto.db')
c = conn.cursor()
# parameter maxDailyKg is actually an atribute of row, should be read from db #
# Current harvesting day and current harvested kg are mandatory parameter.
def predict_day(seasonStartDay, currentHarvestingDay,currentHarvestingKg, maxDailyKg):
    crop_row = 1
    x = 0
    os.getcwd()
    os.chdir(Path)
    absoluteCurrentHarvestingDay = currentHarvestingDay
    daycount = (currentHarvestingDay - seasonStartDay).days
    while currentHarvestingDay <= (seasonStartDay + datetime.timedelta(days=+29)):
        weight = ((math.sin(2 * math.pi * (15/30 - 1/4)) + 1)/ 2 )
        fx = ((math.sin(2 * math.pi * (daycount/30 - 1/4)) + 1)/ 2 ) * (crop_row * 0.00484) 
        Kg = weight * fx * maxDailyKg
        if currentHarvestingKg <= Kg or (x > 1):
            x = 2
            absoluteCurrentHarvestingDay = absoluteCurrentHarvestingDay + datetime.timedelta(days=+1)
            c.execute("INSERT INTO Crops (Row, Kg  , Date) VALUES (?, ?, ?)",
            (crop_row, Kg, absoluteCurrentHarvestingDay))    
        currentHarvestingDay = currentHarvestingDay + datetime.timedelta(days=+1)
        daycount = daycount + 1
        conn.commit()