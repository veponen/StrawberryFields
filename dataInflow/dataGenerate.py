import requests
import bs4  
import re
import numpy as np


def convertLinktoData(aNum):
    string='https://texaset.tamu.edu/DataSummary/Daily/{}?daysInSummary=14'
    getLink=lambda aNum: string.format(aNum)
    url=getLink(aNum)

    resp=requests.get(url)
    soup=bs4.BeautifulSoup(resp.text,'lxml')

    table=soup.find('table')
    table_row=table.find_all('td')
    for each_row in table_row:
        data_list=re.findall(r'<td class="etData">(.*?)</td>',str(table))
    for i,element in enumerate(data_list):
        data_list[i]=float(element)
    return np.array(data_list).reshape(-1,8)
def collect_AND_structure_Data():
    init_array=np.array([0,0,0,0,0,0,0,0]).reshape(-1,8)
    numList=[149,150,151,152,153,155,90,91,92,103,104,105,106,107,108,109,110]
    for aNum in numList:
        data_array =convertLinktoData(aNum)
        init_array=np.concatenate((init_array,data_array))
    return init_array[1:,:]