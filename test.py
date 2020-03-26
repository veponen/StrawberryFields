import sqlite3
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
print("Inserted record successfully")
cursor.execute('''UPDATE weather_data_temperature set temperature = 30 where ID = 1''')
print("Updated successfully")
cursor.execute('''DELETE from weather_data_temperature where ID = 5 ''')
print("Deleted successfully")
print(cursor.execute("SELECT * FROM weather_data_temperature WHERE ID = 1"))
db.commit()
db.close()