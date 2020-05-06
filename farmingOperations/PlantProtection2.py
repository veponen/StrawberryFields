from wwo_hist import retrieve_hist_data
import os
import urllib.request
city = input ("Put youre city: ")

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
            print (row[1])
        aux=aux+1
    return print ("Current Thermal Sum: " + str(TempSum))


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
    elif SumRainPerDay() >=50 and SumRainPerDay() <=80:
        print("Medium posibility of having pests.")
    elif SumRainPerDay() >80:
        print("High posibility of having pests.")

#def pastRainPerDay():
#   print("Star date:  " + str(start_date)



actualWeather()
currentThermalSum()
print ("Sum rain per day: " + str(SumRainPerDay()))
predictedPestAppearances()
#pastRainPerDay()