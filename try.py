import unittest
import sqlite3
from unnecessary_math import multiply
with sqlite3.connect('weather_data_generation.db') as db:
    print("Opened database successfully")
    cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS weather_data_temperature(ID INTEGER PRIMARY KEY, 
date DATE NOT NULL, 
temperature INTERGER NOT NULL) ;''')
cursor.execute('''INSERT INTO weather_data_temperature(date,temperature)
VALUES('2020-03-17',20) ;''')
cursor.execute('''INSERT INTO weather_data_temperature(date,temperature)
VALUES('2020-03-18',27) ;''')
cursor.execute('''INSERT INTO weather_data_temperature(date,temperature)
VALUES('2020-03-19',22) ;''')
cursor.execute('''INSERT INTO weather_data_temperature(date,temperature)
VALUES('2020-03-20',26) ;''')
cursor.execute('''INSERT INTO weather_data_temperature(date,temperature)
VALUES('2020-03-21',12) ;''')
db.commit()
class test_inserted_values(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_Tan(self):
        result = cursor.execute('''INSERT INTO weather_data_temperature(date,temperature) VALUES('2020-03-17',20) ;''')
        expected = cursor.execute('''SELECT * FROM weather_data_temperature WHERE ID = 1''')
        self.assertEqual(result, expected)
        print("Test inserted record successfully")

class test_update_values(unittest.TestCase):
     def test_Tan(self):
        result = cursor.execute('''UPDATE weather_data_temperature set temperature = 30 where ID = 3''')
        expected = cursor.execute('''SELECT * FROM weather_data_temperature WHERE ID = 3''')
        self.assertEqual(result, expected)
        print("Test update record successfully")
        
class test_delete_values(unittest.TestCase):
     def test_Tan(self):
        result = cursor.execute('''DELETE from weather_data_temperature where ID = 5 ''')
        expected = cursor.execute('''SELECT * FROM weather_data_temperature WHERE ID = 5''')
        self.assertEqual(result, expected)
        print("Test delete record successfully")

if __name__ == '__main__':
    unittest.main()
