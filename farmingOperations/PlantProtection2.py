from wwo_hist import retrieve_hist_data
from csv import writer
import os
import urllib.request
from datetime import date
from datetime import datetime
from datetime import timedelta
city = input ("Put youre city: ")
#date1 = date.today()
#date2 = date.today() + timedelta(5)
humidity = 55

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
        return 1
    elif SumRainPerDay() >=50 and SumRainPerDay() <=80:
        return 2
    elif SumRainPerDay() >80:
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
    elif TermalSum <1000 and risk >= 2: 
        print ("Medium to High posibility to have Disease.")

def listOfProtectionDaysPossible():
    import csv
    x = city
    f = open("%s.csv" % x)
    csv_f = csv.reader(f)
    humidity = 77
    CloudCover = 50
    aux=0
    for row in csv_f:
        if aux>0:
            if  int(row[18]) <= humidity and int(row[17]) <= CloudCover:
                print("List of protection days possible: " + row[0])
        aux=aux+1



def newPredictions():  #write in csv file newest predictions
    #x = city
    #with open("%s.csv" % x, 'a+', newline='') as write_obj:
    #    csv_writer = writer(write_obj)
    #   csv_writer.writerow(listOfProtectionDaysPossible())
#-------------------------------------------------------------------------------------------------------

actualWeather()
print ("Sum rain per day (in 10 days): " + str(SumRainPerDay()))
print ("Current Thermal Sum (in 10 days): " + str(currentThermalSum()))
predict = predictedPestAppearances()
if predict ==1 : 
    print("Low posibility of having pests.")
elif predict == 2:
    print("Medium posibility of having pests.")
elif predict == 3: 
    print("High posibility of having pests.")
predictDiseaseAppearance()
listOfProtectionDaysPossible()
newPredictions()