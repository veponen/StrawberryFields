import unittest
import sqlite3
with sqlite3.connect('auto.db') as db:
    print(" Our auto database was opened  successfully")
    cursor = db.cursor()
class test_update_values(unittest.TestCase):
     def test_update(self):
        result = cursor.execute('''UPDATE Crops set Kg = 90 where Row = 1''')
        expected = cursor.execute('''SELECT * FROM Crops WHERE Row = 1''')
        self.assertEqual(result, expected)
        print("Test updated the Kg successfully")
        
class test_delete_values(unittest.TestCase):
     def test_delete(self):
        result = cursor.execute('''DELETE from Crops where Date = "2020, 7, 22" ''')
        expected = cursor.execute('''SELECT * FROM Crops WHERE Date = "2020, 7, 22" ''')
        self.assertEqual(result, expected)
        print("Test deleted requested Date successfully")

if __name__ == '__main__':
    unittest.main()