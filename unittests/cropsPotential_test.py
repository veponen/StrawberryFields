import unittest
import MagicMock
# import 
class TestCropsPotential(unittest.TestCase):

    def test_rowEstimate(self):
        self.assertEqual('foo'.upper(), 'FOO')
        

    def test_foo(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

'''    def test_get_db_free_perm_expects_500(self):
        db_con = MagicMock(UdaExecConnection)
        cursor = MagicMock(UdaExecCursor)
        cursor.fetchone.return_value = [500]
        db_con.cursor.return_value.__enter__.return_value = cursor
        self.dbc_instance = DBSAccess(db_con)
        self.assertEqual(self.dbc_instance.get_db_perm("dbc"), 500)
'''
if __name__ == '__main__':
    unittest.main()