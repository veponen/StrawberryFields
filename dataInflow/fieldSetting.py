import datetime as dt

def unix_to_UTC_time(time_survey):
    time_in_string=dt.datetime.utcfromtimestamp(time_survey).strftime('%Y-%m-%d %H:%M:%S')
    return dt.datetime.strptime(time_in_string,'%Y-%m-%d %H:%M:%S')

CelciusToFahrenheit = lambda Cel: Cel*1.8 +32

UviToSolarGrad = lambda uvi,time_light: uvi*0.025*time_light/1000

MilimetToInch = lambda ml: ml*0.03937

InchToMilimet = lambda inch: inch*25.4

ms_To_mph = lambda ms: ms*2.23693629