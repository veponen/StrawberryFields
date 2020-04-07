import sqlite3
conn = sqlite3.connect('generator.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE dates
             (Nr crt, Random)''')

conn.commit()