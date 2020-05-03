import json as js
import urllib.request
import datetime as dt
import fieldSetting
import numpy as np
import pandas as pd

class WeatherCollectedData:
    url1='https://api.openweathermap.org/data/2.5/onecall?lat=64.286670&lon=27.622125&units=metric&appid=e25afeccd6e22a2e996bed2809e43452'
    url2='https://api.openweathermap.org/data/2.5/forecast?lat=64.286670&lon=27.622125&units=metric&appid=e25afeccd6e22a2e996bed2809e43452'
    def load_and_read_from_API_1(self):
        resp_1=urllib.request.urlopen(self.url1)
        self.jsfile_1=js.load(resp_1)

        self.temp_rain_uv_info=[]
        for each_date in self.jsfile_1['daily'][1:5]:
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
            if len(date_info) ==8 :
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
        self.weather_info_array=np.array([0,0,0,0,0,0,0]).reshape(-1,7)
        for load1, load2 in zip(self.load_and_read_from_API_1(),self.load_and_read_from_API_2()):
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

np.set_printoptions(precision=5,suppress=True)
           
coef=fieldSetting.coef
final_data_weather=FinalWeatherData().finalizeData()
df = pd.DataFrame(data=np.vstack((coef,final_data_weather)),
                index=['Cofficient','Weather_day1','Weather_day2','Weather_day3','Weather_day4'],
                columns=['maxTemp','minTemp','min_humid','solarGrad','rain','wind_3AM','wind_3PM'])

print(df)
print('Total reference ET for coming days:',end='')
print(sum(np.dot(final_data_weather,coef.reshape(7,-1))))