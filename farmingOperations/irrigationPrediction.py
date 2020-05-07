import json as js
import urllib.request
import datetime as dt
import fieldSetting
import numpy as np
import pandas as pd
import datetime

class WeatherCollectedData:
    url1='https://api.openweathermap.org/data/2.5/onecall?lat=64.286670&lon=27.622125&units=metric&appid=e25afeccd6e22a2e996bed2809e43452'
    url2='https://api.openweathermap.org/data/2.5/forecast?lat=64.286670&lon=27.622125&units=metric&appid=e25afeccd6e22a2e996bed2809e43452'
    def load_and_read_from_API_1(self):
        resp_1=urllib.request.urlopen(self.url1)
        self.jsfile_1=js.load(resp_1)
        
        start_num=0 if datetime.datetime.now().hour in (0,1,2) else 1 
        self.temp_rain_uv_info=[]
        for each_date in self.jsfile_1['daily'][start_num:5]:
            sunset=each_date['sunset']
            sunrise=each_date['sunrise']
            temp_max=each_date['temp']['max']
            temp_min=each_date['temp']['min']
            rain_info=each_date.get('rain',0)
            uvi_index=each_date['uvi']

            self.temp_rain_uv_info.append({
                'sunset':sunset,
                'sunrise':sunrise,
                'temp_max':temp_max,
                'temp_min':temp_min,
                'rain_info':rain_info,
                'uvi_index':uvi_index})
        return self.temp_rain_uv_info
    def load_and_read_from_API_2(self):
        resp_2=urllib.request.urlopen(self.url2)
        self.jsfile_2=js.load(resp_2)
        self.date_humid_wind={}
        for each_3_hour in self.jsfile_2['list']:
            date=dt.datetime.strftime(fieldSetting.unix_to_UTC_time(each_3_hour['dt']),'%Y-%m-%d')
            time=dt.datetime.strftime(fieldSetting.unix_to_UTC_time(each_3_hour['dt']),'%H:%M:%S')
            if date not in self.date_humid_wind:
                self.date_humid_wind[date]={time:{
                    'humidity':each_3_hour['main']['humidity'],
                    'wind_speed':each_3_hour['wind']['speed']
                    }}
            else:
                self.date_humid_wind[date][time]={
                    'humidity':each_3_hour['main']['humidity'],
                    'wind_speed':each_3_hour['wind']['speed']
                    }
        self.humid_wind_info=[]
        for each_date in self.date_humid_wind:
            date_info=self.date_humid_wind[each_date]
            if len(date_info) == 8 :
                wind_3AM=date_info['03:00:00']['wind_speed']
                wind_3PM=date_info['15:00:00']['wind_speed']
                min_humid = min([date_info[each3hour]['humidity'] for each3hour in date_info])
                self.humid_wind_info.append({
                    'min_humid':min_humid,
                    'wind_3AM':wind_3AM,
                    'wind_3PM':wind_3PM
                })
        return self.humid_wind_info

class FinalWeatherData(WeatherCollectedData):   
    def finalizeData(self): 
        '''
    in from url2 parameter, you will get data for 5 days starting from the time you access that link
    for example, if you run the irrigationPrediction at 12:00 date 05.05.2020, you will get data from 12:00 5.5.2020 to 9:00 10.5.2000
    which mean you can't get wind_speed at 3AM on day 05.05 and wind_speed at 3PM on day 10.05
    so only date 06.05, 07.05, 08.05, 09.05 have full data (which you can have minimum humidity and wind at 3AM and wind at 3PM)
    ~~~ Solution: the way to get 5 day is to run the program from 0:00AM to 3:00AM ~~~
        '''
        self.weather_info_array=np.array([0,0,0,0,0,0,0]).reshape(-1,7)
        temp_rain_uv=self.load_and_read_from_API_1()
        humid_wind=self.load_and_read_from_API_2()
        for load1, load2 in zip(temp_rain_uv,humid_wind):
            sunset_time=fieldSetting.unix_to_UTC_time(load1['sunset'])
            sunrise_time=fieldSetting.unix_to_UTC_time(load1['sunrise'])
            amount_time_light_in_seccond=(sunset_time-sunrise_time).seconds # (sec)
            maxTemp = fieldSetting.CelciusToFahrenheit(load1['temp_max']) # (*F)
            minTemp = fieldSetting.CelciusToFahrenheit(load1['temp_min']) # (*F)
            min_humid = load2['min_humid'] # humidity percetage
            solarGrad = fieldSetting.UviToSolarGrad(load1['uvi_index'],amount_time_light_in_seccond) # (MJ/m2)
            rain=fieldSetting.MilimetToInch(load1['rain_info']) # (inch)
            wind_3AM=fieldSetting.ms_To_mph(load2['wind_3AM']) # (mph)
            wind_3PM=fieldSetting.ms_To_mph(load2['wind_3PM']) # (mph)

            self.weather_info_array=np.vstack((self.weather_info_array,np.array([
                maxTemp,
                minTemp,
                min_humid,
                solarGrad,
                rain,
                wind_3AM,
                wind_3PM
            ]).reshape(-1,7)))
        return self.weather_info_array[1:]
'''
45.878000  34.682000  56.000000   4.400830  0.009843  7.650322  10.267538
45.050000  32.864000  58.000000   4.650565  0.000000  7.113457  10.960988
43.304000  33.422000  58.000000   4.680186  0.000000  4.071224   8.388511
46.202000  36.500000  67.000000   4.805775  0.413779  7.448998   4.854152
'''
np.set_printoptions(precision=5,suppress=True)
coef=fieldSetting.coef
final_data_weather=FinalWeatherData().finalizeData()
row_name=['Coefficient']
for i in range(1,final_data_weather.shape[0]+1):
    string = 'Weather_day_{}'
    row_name.append(string.format(i))

df = pd.DataFrame(data=np.vstack((coef,final_data_weather)),
                index=row_name, # row name
                columns=['maxTemp','minTemp','min_humid','solarGrad','rain','wind_3AM','wind_3PM']) # column name

next_following_irrigation=np.dot(final_data_weather,coef.reshape(7,-1))
total_irrigation=sum(next_following_irrigation)
print(df)
print('Total reference ET for coming days:',total_irrigation)