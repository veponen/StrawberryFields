import datetime as dt
import json as js
import urllib.request
import sqlite3 as sql

def unix_to_UTC_time(time_survey):
    return dt.datetime.utcfromtimestamp(time_survey).strftime('%Y-%m-%d %H:%M:%S')
def load_and_read_from_API():    
    url='https://api.openweathermap.org/data/2.5/onecall?lat=64.286670&lon=27.622125&units=metric&appid=e25afeccd6e22a2e996bed2809e43452'

    resp=urllib.request.urlopen(url)
    jsfile_Tornio=js.load(resp)

    

    data_info=[]
    for each_day in jsfile_Tornio['daily']:
        date_predicted=unix_to_UTC_time(each_day['dt'])
        temp_max=each_day['temp']['max']
        temp_min=each_day['temp']['min']
        temp_avg=each_day['temp']['day']
        rain_info=each_day.get('rain',0) # if it was no rain on the surveyed day, then return value 0

        data_info.append({
            'date_predicted':date_predicted,
            'temp_max':temp_max,
            'temp_min':temp_min,
            'temp_avg':temp_avg,
            'rain_info (mm)': rain_info
        })
    return data_info

def get_k_value():
    try:
        con=sql.connect('dataInflow\WeatherDataTest.db')
        ori_table=con.execute('select * from WeatherPrediction').fetchall()
        #if there is no table named 'WeatherPrediction' in 'WeatherDataTest.db', then jump to except statement
        if len(ori_table) != 0:
            k=ori_table[-1][0]+1
        else:
            k=1
    except:
        k=1
    con.commit()
    con.close()
    return k


def final_data():
    data_list=[]
    today=dt.datetime.now().strftime('%Y-%m-%d')
    pk_start=get_k_value()
    for i in load_and_read_from_API():
        data_tuple=(pk_start,today,i['date_predicted'],i['temp_min'],i['temp_max'],i['temp_avg'],i['rain_info (mm)'])
        data_list.append(data_tuple)
        pk_start+=1
    return data_list

def update_data(data):
    Wea_pred=sql.connect('dataInflow\WeatherDataTest.db')
    try:   
        Wea_pred.execute('''
        CREATE TABLE "WeatherPrediction" (
            "prediction_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            "predictionDate"	DATE NOT NULL,
            "date"	DATE NOT NULL,
            "minTemp"	INTEGER NOT NULL DEFAULT 0,
            "maxTemp"	INTEGER NOT NULL DEFAULT 0,
            "avgTemp"	INTEGER NOT NULL DEFAULT 0,
            "rain"	INTEGER NOT NULL DEFAULT 0
        );
    ''')
    except:
        pass
    try:
        Wea_pred.execute('''
    insert into WeatherPrediction (prediction_id, predictionDate, date, minTemp, maxTemp, avgTemp, rain) 
    values (?,?, ?, ?, ?, ?, ?)''',data)
        Wea_pred.commit()
    except:
        pass
        
def excutemanytime(wea=final_data()):
    
    for i in wea:
        line_info=WeatherPrediction().date_info(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
        if update_data(line_info) == None:
            continue
        else:
            update_data(line_info)

class WeatherPrediction:
    def date_info(self,input_1,input_2,input_3,input_4,input_5,input_6,input_7):
        self.pk=input_1
        self.predictionDate=input_2
        self.date=input_3
        self.minTemp=input_4
        self.maxTemp=input_5
        self.avgTemp=input_6
        self.rain=input_7
        return self.pk,self.predictionDate,  self.date,self.minTemp,self.maxTemp, self.avgTemp,self.rain
        
def main():
    excutemanytime()

if __name__ == '__main__':
    main()