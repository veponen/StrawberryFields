import unittest
import datetime
from unittest.mock import MagicMock
from unnecessary_math import multiply
from cropsPotential import predict_day
import sys
import os
# some examples: 
# sys.path.append(os.getcwd() + '/..')
# c:\Users\veper\Documents\SOFTAUS\StrawberryFields
#   sys.path.insert(1, os.getcwd() + '/testDataGeneration/')
# https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure
# first import package (directory) then import module (file)
import testDataGeneration #package import
from testDataGeneration import Straberry # module import

class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_numbers_3_4(self):
        #unnecessary_math.multiply(1,3)
        Straberry.cropsGenerator()
        self.assertEqual( multiply(3,4), 12)
 
    def test_strings_a_3(self):
        rowHarvest = 100
        self.assertEqual(rowHarvest, 100)
        #strawberryCorpsGeneration()
        self.assertEqual( multiply('a',3), 'aaa')

    # mock patch, mock 
    def test_cropspotential(self):
        # c:\Users\veper\Documents\SOFTAUS\StrawberryFields
        print(os.getcwd())
        seasonStartDay =  datetime.datetime.now()
        currentHarvestingDay =  datetime.datetime.now()
        currentHarvestingKg =  20
        maxDailyKg = 100
        predict_day(seasonStartDay, currentHarvestingDay,currentHarvestingKg, maxDailyKg)
        self.assertEqual( multiply('a',3), 'aaa')
       

if __name__ == '__main__':
    print(os.getcwd())
    unittest.main()