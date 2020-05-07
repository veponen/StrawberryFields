
# In[20]:

import os
import sqlite3
import pandas as pd
cnx = sqlite3.connect('C:/Users/T460s/Desktop/Generation.db')

data = pd.read_sql_query("SELECT * FROM Strawberries", cnx)
data['Date'] = pd.to_datetime(data['Date'])
data.info()
data


# In[21]:


data.index = [x for x in range(1, len(data.values)+1)]
data.index.name = 'Index_Date'
data


# In[25]:
from subprocess import check_output
def Find_amount(current_date, future_date, amount):
    
    if data.iloc[current_date]['Date'] <= data.iloc[future_date]['Date']:
        total_amount = data.iloc[1:future_date]['Crop'].sum() - data.iloc[1:current_date]['Crop'].sum()
        if total_amount >= amount:
            message = "We have enough {} kgs to supply for your offer because we still have {} kgs.".format(amount, total_amount)
        else:
            message = "Sorry! We don't have enough {} kgs to supply for your offer.".format(amount)
    else:
        message = 'Reject offer!'
    return message
    
Find_amount(4, 6, 11)


        

