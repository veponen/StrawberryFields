from mock import Mock
import unittest
import sys
sys.path.insert(0,".//farmingOperations")
import irrigationPrediction

class TestIrrigationPrediction(unittest.TestCase):
    final=irrigationPrediction.FinalWeatherData()

    def testCoefficent(self):
        coef=irrigationPrediction.df.loc['Coefficient']
        self.assertAlmostEqual(coef.loc['maxTemp'],coef.loc['minTemp'],delta=0.01)
        # test if the difference between coefficient maxTemp and coefficient minTemp were no more than 0.01
        # (these two featurea represent for the same element, which is temperature)
        self.assertAlmostEqual(coef.loc['wind_3AM'],coef.loc['wind_3PM'],delta=0.01)
        # test if the difference between coefficient wind_3AM and coefficient wind_3PM were no more than 0.01 
        # (these two featurea represent for the same element, which is wind)
        self.assertLessEqual(coef.loc['rain'],0)
        # test if the rain coefficient less than or equal to 0 (the more rain, the less irrigation needed)
        self.assertGreaterEqual(coef.loc['solarGrad'],0)
        # test if the solarGrad coefficient larger than or equal to 0 (the more Solar Radiation, the more irrigation needed)

        print('test 1 passed')
    def testLoad1(self):
        temp_rain_uv=self.final.load_and_read_from_API_1()
        self.assertTrue(all([each_day['temp_max'] > each_day['temp_min'] for each_day in temp_rain_uv]))
        # test if the maximum temperature is larger than minimum temperature
        self.assertTrue(all([each_day['uvi_index'] >= 0 for each_day in temp_rain_uv]))
        # test if all the uv index larger or equal to 0
        self.assertTrue(all([each_day['sunrise']<each_day['sunset'] for each_day in temp_rain_uv]))
        # test if the sunrise time is before sunset time
        print('test 2 passed')

    def testLoad2(self):
        self.final.load_and_read_from_API_2()
        self.assertEqual(len(self.final.jsfile_2['list']),40) 
        # test if the amount of point of time is equal to 40 (5 days x 8 points of time per day)
        self.assertTrue([(each_day['min_humid'] <=100 and each_day['min_humid'] >=0) for each_day in self.final.humid_wind_info])
        # test if the humidity run from 0 to 100
        print('test 3 passed')

    def testwithMock(self):
        self.final.finalizeData()
        weather_info_array=self.final.weather_info_array
        dim_array = weather_info_array.shape
        self.assertEqual(dim_array[1],7) 
        # assert number of collumns must be equal to 7
        self.assertTrue(all([i== 0 for i in weather_info_array[0,:]])) 
        # assert number of rows must be equal to 4 or 5
        moc_1=Mock()
        moc_1.return_value=(4,5)
        self.assertIn(self.final.finalizeData().shape[0],moc_1()) 
        # assert if the number of row is equal to 5 or 4 (5 if run from 0AM to 3AM, else: 4)
        self.not_being_called_yet=moc_1
        self.not_being_called_yet.assert_called_once() 
        # check if the moc_1 were called once (moc_1 was called in the previous test) 
        self.assertTrue(moc_1.called) 
        # check if moc_1 were called
        time_call=moc_1()
        self.assertEqual(moc_1.call_count,2) 
        # check if the moc_1 were called two time (second call was in previous line time_call=moc_1() )
        print('test 4 passed')

if __name__ =='__main__':
    unittest.main()