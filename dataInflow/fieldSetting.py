import datetime as dt
import dataGenerate
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def unix_to_UTC_time(time_survey):
    time_in_string=dt.datetime.utcfromtimestamp(time_survey).strftime('%Y-%m-%d %H:%M:%S')
    return dt.datetime.strptime(time_in_string,'%Y-%m-%d %H:%M:%S')

CelciusToFahrenheit = lambda Cel: Cel*1.8 +32

UviToSolarGrad = lambda uvi,time_light: uvi*0.025*time_light/1000

MilimetToInch = lambda ml: ml*0.03937

InchToMilimet = lambda inch: inch*25.4

ms_To_mph = lambda ms: ms*2.23693629

Data = dataGenerate.collect_AND_structure_Data()

X,y=Data[:,1:],Data[:,0].reshape(-1,1)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=19)
model=LinearRegression(fit_intercept=False).fit(X_train,y_train)
coef = model.coef_.reshape(1,-1)