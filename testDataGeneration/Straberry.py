
class MainProgram():

    def cropsGenerator(self):
        import sqlite3
        from datetime import date, timedelta
        import random
        import math
        import unittest
        conn = sqlite3.connect('generator.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE dates
                    (Day, Harvest)''')

        start_date = date(2020, 7, 1) 
        end_date = date(2021, 8, 1) 
        numDays = end_date-start_date

        for i in range(numDays.days + 1):
            n1 = float(((math.sin(2 * math.pi * (numDays.days - 1/4)) + 1) / 2) * 1000)
            harvest = n1
            day = start_date + timedelta(days=i)
            randomNumber = random.randint(-20,+20)
            harvest= harvest-randomNumber
            if harvest<0:
                harvest=0
            c.execute("INSERT INTO dates VALUES (?, ?);", (day, harvest))
        conn.commit()


p1=MainProgram()
p1.cropsGenerator()
