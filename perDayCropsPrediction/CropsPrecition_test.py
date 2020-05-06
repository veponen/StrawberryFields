import unittest
import CropsPrecition
import datetime
class TestFunctions(unittest.TestCase):
    def test_CropsPrediction(self):
        self.assertEqual(CropsPrecition.givenDaysCropsForCustomer(1, 6, 10, 6, 150), 90.0)
        self.assertEqual(CropsPrecition.givenDaysCropsForCustomer(1, 6, 19, 6, 150), 120.0)
        self.assertEqual(CropsPrecition.givenDaysCropsForCustomer(15, 6, 4, 7, 150), 110.0)
        self.assertEqual(CropsPrecition.givenDaysCropsForCustomer(15, 6, 21, 7, 150), "Season over on that day")

if __name__=="__main__":
    unittest.main()