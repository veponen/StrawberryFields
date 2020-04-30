import json as js
import urllib.request
import fieldSetting

def load_and_read_from_API():
    url='https://api.openweathermap.org/data/2.5/onecall?lat=64.286670&lon=27.622125&units=metric&appid=e25afeccd6e22a2e996bed2809e43452'
    resp=urllib.request.urlopen(url)
    jsfile_Tornio=js.load(resp)

    weather_info=[]
    for each_date in jsfile_Tornio['daily']:
        temp_max=each_date['temp']['max']
        temp_min=each_date['temp']['min']
        rain_info=each_date.get('rain',0)
        uvi_index=each_date['uvi']
        wind_speed=each_date['wind_speed']
        humidity=each_date['humidity']
        weather_info.append({
            'temp_max':temp_max,
            'temp_min':temp_min,
            'rain_info':rain_info,
            'uvi_index':uvi_index,
            'wind_speed':wind_speed,
            'humidity':humidity})
    return weather_info


def irrigationPrediction5Days(data=load_and_read_from_API()):
    
    totalIrrigationVolume = 0
    for everyWeatherPrediction in data:
        tempCoefficient=fieldSetting.getTempCoefficient(everyWeatherPrediction['temp_max'],everyWeatherPrediction['temp_min'])
        rainCoefficient=fieldSetting.getRainCoefficient(everyWeatherPrediction['rain_info'])
        uviCoefficient=fieldSetting.getUviCoefficient(everyWeatherPrediction['uvi_index'])
        windCoeffienct=fieldSetting.getWindCoefficient(everyWeatherPrediction['wind_speed'])
        humidCoeffienct=fieldSetting.getHumidCofficient(everyWeatherPrediction['humidity'])

        eachDayIrrigation = fieldSetting.baseVolumeOfIrrigation*tempCoefficient*rainCoefficient*uviCoefficient*windCoeffienct*humidCoeffienct
        totalIrrigationVolume += eachDayIrrigation
    return totalIrrigationVolume/fieldSetting.irrigationRunCount

print(irrigationPrediction5Days())
