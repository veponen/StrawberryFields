
# In[44]:

import sqlite3
import pandas as pd
cnx = sqlite3.connect('C:/Users/T460s/Desktop/Crop_Generation.db')

data = pd.read_sql_query("SELECT * FROM Strawberry", cnx)
data['Date'] = pd.to_datetime(data['Date'])
data.info()
data



# In[45]:

data.index = [x for x in range(1, len(data.values)+1)]
data


# In[47]:

def Find_amount(future_date, amount):
    
    if 1 <= future_date <= 10:
        total_amount = data.iloc[1:future_date]['Crop'].sum()
        if total_amount >= amount:
            message = "We have enough {} kgs to supply for your offer because we still have {} kgs.".format(amount, total_amount)
        else:
            message = "Sorry! We don't have enough {} kgs to supply for your offer.".format(amount)
            
    elif 11 <= future_date <= 19:
        total_amount = data.iloc[1:future_date]['Crop'].sum() - data.iloc[1:10]['Crop'].sum()
        if total_amount >= amount:
            message = "We have enough {} kgs to supply for your offer because we still have {} kgs.".format(amount, total_amount)
        else:
            message = "Sorry! We don't have enough {} kgs to supply for your offer.".format(amount)
            
    elif 20 <= future_date <= 30:
        total_amount = data.iloc[1:future_date]['Crop'].sum() - data.iloc[1:20]['Crop'].sum()
        if total_amount >= amount:
            message = "We have enough {} kgs to supply for your offer because we still have {} kgs.".format(amount, total_amount)
        else:
            message = "Sorry! We don't have enough {} kgs to supply for your offer.".format(amount)     
    return message 
    
Find_amount(15, 44)


# %%
