import unittest
import datetime
from unittest.mock import MagicMock
from unnecessary_math import multiply
from cropsPotential import predict_day
import sys
import os
sys.path.append(os.getcwd() + '/..')
# import parent.file1
# from perDayCropsPrediction.strawberry import strawberryCorpsGeneration
from config import rowHarvest
# import unnecessary_math
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_numbers_3_4(self):
        self.assertEqual( multiply(3,4), 12)
 
    def test_strings_a_3(self):
        rowHarvest = 100
        self.assertEqual(rowHarvest, 100)
        #strawberryCorpsGeneration()
        self.assertEqual( multiply('a',3), 'aaa')

    # mock patch, mock 
    def test_cropspotential(self):
        seasonStartDay =  datetime.datetime.now()
        currentHarvestingDay =  datetime.datetime.now()
        currentHarvestingKg =  20
        maxDailyKg = 100
        predict_day(seasonStartDay, currentHarvestingDay,currentHarvestingKg, maxDailyKg)
        self.assertEqual( multiply('a',3), 'aaa')
       

if __name__ == '__main__':
    unittest.main()