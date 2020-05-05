import sqlite3
conn = sqlite3.connect('StrawberryFields.db')
c = conn.cursor()
record = c.fetchone()
##### Crop Insert 
CropID = 666
Crop_Weight = 44
Field_name = "GLAND"
Good_Before = " 2020-10-01 "
##### Customer Insert
Name = "Tan Belly"
CustomerID = 13
Amount_of_orders = 8
##### Order Insert
OrderID = 23213
CustomerID = 2341234
Weight = 22
Price = 345
Pickup_Date = "2020-06-21"

def data_entry_crops():
    c.execute("INSERT INTO Crops (CropsID, Weight  , Field_name , Good_Before) VALUES (?, ?, ?, ?)",
     (CropID, Crop_Weight  , Field_name , Good_Before))
    conn.commit()
    c.close()
    conn.close()
def data_entry_customer():
    c.execute("INSERT INTO Customer (Name, Amount_of_orders , CustomerID) VALUES (?, ?, ?)",
     (Name, CustomerID  , Amount_of_orders))
    conn.commit()
    c.close()
    conn.close()    
def data_entry_orders():
    c.execute("INSERT INTO Orders (OrderID, CustomerID  , Weight , Price, Pickup_Date ) VALUES (?, ?, ?, ?, ?)",
     (OrderID, CustomerID  , Weight , Price, Pickup_Date))
    conn.commit()
    c.close()
    conn.close()
def read_from_db():
    c.execute('SELECT Weight FROM Crops ') 
    for row in c.fetchall():
        all_crops = all_crops + float(record[row])
    print(all_crops)
def read_from_db1():      
    SELECT SUM(Weight) BAROS FROM Crops
read_from_db1()
