getTempCoefficient = lambda minTemp,maxTemp: abs((minTemp+maxTemp)/2) if minTemp+maxTemp !=0 else 1
getRainCoefficient = lambda rain: rain/10 if (rain != 0) else 1
getUviCoefficient = lambda uvi: uvi + 1
getWindCoefficient = lambda wind: wind + 1
getHumidCofficient = lambda humid: (100-humid)/100

baseVolumeOfIrrigation = 100 #(in mm)
irrigationRunCount = 3