import unittest
import sqlite3 as sql
import re
import pandas as pd
import datetime as dt

def check_data_continuity(list_check):
    bool_list=[]
    global pattern_date
    global pattern_date_time
    for i, each_element in enumerate(list_check[1:]):
        if type(each_element) == str and pattern_date.match(each_element):
            bool_val=convert_string_into_datetime_type_1(each_element)-dt.timedelta(days=1)==convert_string_into_datetime_type_1(list_check[i])
            bool_list.append(bool_val)
        elif type(each_element) == str and pattern_date_time.match(each_element):
            bool_val=convert_string_into_datetime_type_2(each_element)-dt.timedelta(days=1)==convert_string_into_datetime_type_2(list_check[i])
            bool_list.append(bool_val)
        elif type(each_element) in (int,float):
            bool_val=each_element-1==list_check[i]
            bool_list.append(bool_val)
        
    return bool_list

            
def check_date_pattern(date): 
    global pattern_date

    if pattern_date.match(date):
        return True
    else:
        return False

def check_date_time_pattern(date):
    global pattern_date_time
    if pattern_date_time.match(date):
        return True
    else:
        return False

class TestDatabase_weatherPrediction(unittest.TestCase):
    
    def test_integrity_data(self):
        self.assertTrue(all(original_table['maxTemp']>=original_table['minTemp']))
        self.assertTrue(check_date_pattern(original_table['predictionDate'][3]))
        self.assertTrue(all([i==8 for i in group_by_predictionDate_table['number_predicted_days']]))
    
    def test_data_pattern(self):
        date_list_bool=[check_date_pattern(each_date) for each_date in group_by_predictionDate_table['predictionDate']]
        self.assertTrue(all(date_list_bool))
        date_time_list_bool=[check_date_time_pattern(each_date) for each_date in original_table['date']]
        self.assertTrue(all(date_time_list_bool))

    def test_data_continuity(self):
        self.assertTrue(all(check_data_continuity(group_by_predictionDate_table['predictionDate'])))
        self.assertTrue(all(check_data_continuity(original_table['prediction_id'])))
        self.assertFalse(all(check_data_continuity(original_table['minTemp'])))
        self.assertFalse(all(check_data_continuity(original_table['date'])))
if __name__ == '__main__':

    Wea_pred=sql.connect('dataInflow\WeatherDataTest.db')

    original_table=pd.read_sql_query('''
    select * 
    from WeatherPrediction''',Wea_pred)

    group_by_predictionDate_table=pd.read_sql_query('''
    select predictionDate, count(*) as number_predicted_days
    from WeatherPrediction
    group by predictionDate''',Wea_pred)
    Wea_pred.commit()
    Wea_pred.close()
    
    pattern_date = re.compile("^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
    pattern_date_time = re.compile("^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}$")

    convert_string_into_datetime_type_1=lambda date_in_string: dt.datetime.strptime(date_in_string, '%Y-%m-%d')
    convert_string_into_datetime_type_2=lambda date_in_string: dt.datetime.strptime(date_in_string, '%Y-%m-%d %H:%M:%S')
    unittest.main()