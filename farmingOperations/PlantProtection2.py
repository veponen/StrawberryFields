from wwo_hist import retrieve_hist_data
import os
import urllib.request
from datetime import date
from datetime import datetime
from datetime import timedelta
city = input ("Put youre city: ")
#date1 = date.today()
#date2 = date.today() + timedelta(5)

def actualWeather():
    os.chdir(".")
    frequency=24
    start_date = '01-MAY-2019'
    end_date = '10-MAY-2019'
    api_key = '4a6f862204ea4ff4962120500200405'
    location_list = [city]
    hist_weather_data = retrieve_hist_data(api_key,location_list,start_date,end_date,frequency,location_label = False,export_csv = True,store_df = True)

def currentThermalSum():
    import csv
    x = city
    f = open("%s.csv" % x)
    csv_f = csv.reader(f)
    TempSum=0
    aux=0
    for row in csv_f:
        if aux>0:
            TempSum = TempSum + int(row[1])
        aux=aux+1
    return TempSum


def SumRainPerDay():
    import csv
    x = city
    f = open("%s.csv" % x)
    csv_f = csv.reader(f)
    RainPerDay = 0
    aux=0
    for row in csv_f:
        if aux>0:
            RainPerDay = RainPerDay + round(float(row[19]),2)
        aux=aux+1
    return RainPerDay


def predictedPestAppearances(): 
    if SumRainPerDay() < 50:
        print("Low posibility of having pests.")
        return 1
    elif SumRainPerDay() >=50 and SumRainPerDay() <=80:
        print("Medium posibility of having pests.")
        return 2
    elif SumRainPerDay() >80:
        print("High posibility of having pests.")
        return 3


def predictDiseaseAppearance(): #currentThermalSum,SumRainPerDay
    risk = predictedPestAppearances()
    TermalSum = currentThermalSum()
    if TermalSum < 300 and  risk == 1:
        print ("Low posibility to have Disease.")
    elif TermalSum >=300 and risk ==2:
        print ("Medium posibility to have Disease.")
    elif TermalSum >=300 and risk ==3:
        print("High posibility to have Disease")








actualWeather()
print ("Sum rain per day (in 10 days): " + str(SumRainPerDay()))
print ("Current Thermal Sum (in 10 days): " + str(currentThermalSum()))
predictedPestAppearances()
predictDiseaseAppearance()
