def Kelvin_to_celsius(k):
    return (float(k) - 273.15)
    
import apikey
import mysql.connector
import requests, json 
import mysql

def insert_weather_data(data):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="qwerty",
        port='12346',
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO weather (current_temp,min_temp,max_temp,pressure,humidity) VALUES (%s, %s, %s, %s, %s)"
    val = (data[0], data[1], data[2], data[3], data[4])
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


def get_weather_data(cityname):
    api_key = apikey.apikey
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + str(cityname)
    response = requests.get(complete_url) 
    x = response.json() 
    
    if x["cod"] != "404": 
        print(x)
        y = x["main"] 
        current_temperature = y["temp"] 
        current_pressure = y["pressure"] 
        current_humidiy = y["humidity"]   
        min_temp = y["temp_min"]   
        max_temp = y["temp_max"] 

        z = x["weather"] 
        weather_description = z[0]["description"] 
    
        print(" Temperature (in celsius unit) = " +
                        str(Kelvin_to_celsius(current_temperature)) + 
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidiy) +
            "\n description = " +
                        str(weather_description)) 
        val=(str(Kelvin_to_celsius(current_temperature)),str(Kelvin_to_celsius(min_temp)),str(Kelvin_to_celsius(max_temp)), str(current_pressure), str(current_humidiy))
        return(val)
    elif x['cod'] == "401":
        print(y)
        return(0)
    else: 
        print(" City Not Found ") 
        return(0)




values=get_weather_data("Tornio")
print(values)
insert_weather_data(values)