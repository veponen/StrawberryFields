from mock import Mock
import unittest
import irrigationPrediction
class TestIrrigationPrediction(unittest.TestCase):
    final=irrigationPrediction.FinalWeatherData()

    def testCoefficent(self):
        coef=irrigationPrediction.df.loc['Cofficient']
        self.assertAlmostEqual(coef.loc['maxTemp'],coef.loc['minTemp'],delta=0.01)
        self.assertAlmostEqual(coef.loc['wind_3AM'],coef.loc['wind_3PM'],delta=0.01)
        self.assertLessEqual(coef.loc['rain'],0)
        self.assertGreaterEqual(coef.loc['solarGrad'],0)
        print('test 1 passed')
    def testLoad1(self):
        temp_rain_uv=self.final.load_and_read_from_API_1()
        self.assertTrue(all([each_day['temp_max'] > each_day['temp_min'] for each_day in temp_rain_uv]))
        self.assertTrue(all([each_day['uvi_index'] >= 0 for each_day in temp_rain_uv]))
        self.assertTrue(all([each_day['sunrise']<each_day['sunset'] for each_day in temp_rain_uv]))
        print('test 2 passed')

    def testLoad2(self):
        self.final.load_and_read_from_API_2()
        self.assertEqual(len(self.final.jsfile_2['list']),40)
        self.assertTrue([(each_day['min_humid'] <=100 and each_day['min_humid'] >=0) for each_day in self.final.humid_wind_info])
        print('test 3 passed')
    def dumbTest(self):
        self.final.finalizeData()
        dim_array = self.final.weather_info_array.shape
        self.assertEqual(dim_array[1],7)
        self.assertIn(dim_array[0],(4,5))
        moc_1=Mock(return_value=(4,7))
        moc_1.shape=(4,7)
        self.assertEqual(self.final.finalizeData().shape,moc_1())
        self.not_being_called_yet=moc_1
        self.not_being_called_yet.assert_called_once()
        self.assertTrue(moc_1.called)
        time_call=moc_1()
        self.assertEqual(moc_1.call_count,2)
        print('test 4 passed')

if __name__ =='__main__':
    unittest.main()