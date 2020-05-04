from mock import Mock
import unittest
import irrigationPrediction
class TestIrrigationPrediction(unittest.TestCase):
    final=irrigationPrediction.FinalWeatherData()
    def testCoefficent(self):
        coef=irrigationPrediction.df.loc['Cofficient']
        self.assertAlmostEqual(coef.loc['maxTemp'],coef.loc['minTemp'],delta=0.01)
        self.assertAlmostEqual(coef.loc['wind_3AM'],coef.loc['wind_3PM'],delta=0.001)
        self.assertLessEqual(coef.loc['rain'],0)
    def testClass(self):
        weather_array=self.final.finalizeData()
        dim_array = weather_array.shape
        self.assertEqual(dim_array[1],7)
        self.assertEqual(dim_array[0],4)
        moc_1=Mock(return_value=(4,7))
        moc_1.shape=(4,7)
        self.assertEqual(self.final.finalizeData().shape,moc_1())
        self.not_being_called_yet=moc_1
        self.not_being_called_yet.assert_called_once()
        self.assertTrue(moc_1.called)
        time_call=moc_1()
        self.assertEqual(moc_1.call_count,2)
if __name__ =='__main__':
    unittest.main()