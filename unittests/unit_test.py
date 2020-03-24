import unittest
import sqlite3 as sql
import re 

Cu_re=sql.connect('CustomerReservation.db').cursor()
customer_table=Cu_re.execute('''select * from Customers''').fetchall()
reservation_table=Cu_re.execute('''select * from Reservation''').fetchall()
strawberrytype_table=Cu_re.execute('''select * from Strawberrytype''').fetchall()

def check_date(date):
    pattern = re.compile("^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
    if pattern.match(date):
        return True
    else:
        return False

def func(listt):
    return listt[0]

def check_time(time):
    pattern = re.compile("^[0-9]{2}:[0-9]{2}:[0-9]{2}$")
    hour=time[:2]
    minute=time[3:5]
    if pattern.match(time) and int(hour) <24 and int(minute) <60:
        return True
    else:
        return False

def check_fk_key_constraint(model_table,index1,testing_table,index2):
    primary_key_list=[]
    for row in model_table:
        primary_key=str(row[index1])
        primary_key_list.append(primary_key)
    boolean_check_list=[]
    for row in testing_table:
        foreign_key=str(row[index2])
        if foreign_key in set(primary_key_list):
            boolean_check_list.append(True)
        else:
            boolean_check_list.append(False)
    return boolean_check_list


class TestDatabase(unittest.TestCase):

    def test_Customers(self):
        self.assertTrue(check_date(customer_table[0][3]))
        self.assertEqual(customer_table[1][1],'Hien Bui')
        self.assertFalse(customer_table[0][0]==0)

    def test_reservation(self):
        self.assertGreater(sorted(reservation_table,key=func)[0][0],0)
        self.assertTrue(reservation_table[2][-1].isdigit())
        self.assertTrue(check_time(reservation_table[2][2]))
   
    def test_strawberrytype(self):
        self.assertEqual(strawberrytype_table[1][1],'Jewel')
        self.assertEqual(strawberrytype_table[-1][0],len(strawberrytype_table))

    def test_constraint(self):
        cus_res_key=check_fk_key_constraint(customer_table,0,reservation_table,3)
        self.assertTrue(all(cus_res_key))
        typ_res_key=check_fk_key_constraint(strawberrytype_table,0,reservation_table,3)
        self.assertTrue(all(typ_res_key))

if __name__=='__main__':
    unittest.main()