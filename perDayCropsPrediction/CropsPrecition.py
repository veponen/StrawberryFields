import datetime
def givenDaysCropsForCustomer(seasonStartday, seasonStartmonth, currentcropsKG, CurrentDay, currentmonth, CustomerOrderDay, CustomerOrderMonth, MaxCropsKG):
    increment = MaxCropsKG/15 #The increment of how much the amount of crops increases or decrases daily
    daycounter = 0 #To determine Ascent or Decline
    day = seasonStartday
    month = seasonStartmonth
    date = datetime.date(2020, seasonStartmonth, seasonStartday)#An incremental date to count the days
    Neededdate = datetime.date(2020, CustomerOrderMonth, CustomerOrderDay)
    while date < Neededdate:
        if day == 30 and month == 6:
            day = 1
            month = month + 1
        elif day == 31:
            day = 1
            month = month + 1
        else:
            day = day + 1
        date = datetime.date(2020, month, day)
        daycounter = daycounter + 1
    if daycounter <= 15:
        estimatenumber = increment * daycounter
        return estimatenumber
    elif daycounter > 15:
        estimatenumber = increment * ((daycounter - 15) - 15)
        return estimatenumber

a = givenDaysCropsForCustomer(17, 6, 124, 27, 6, 29, 6, 170)
print(a)