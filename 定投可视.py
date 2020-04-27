#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import yfinance as yf
import numpy as np
import Correctdateformat as Cf
import datetime
from datetime import date
from matplotlib import pyplot as plt
from pandas.plotting import register_matplotlib_converters
from datetime import timedelta 

LastUpdate= "2020-04-16" #-----------------today's date or some day after you start investing
StockCode='BOX' #--------------------------give an investment target
Rawfile = 'Example.xlsx' #---------------------give a file name
Stock = pd.read_csv(
    "https://raw.githubusercontent.com/xiaolai/regular-investing-in-box/master/data/box_price_history.txt",
    sep="\t"
)

data = pd.read_excel(Rawfile,sheet_name=StockCode)
Cost = list(data.Cost)
Share = list(data.Share)
InvestTime = list(data.Time)

AccumulateCost=[] 
for i in range(len(Cost)):
    if i == 0:
        AccumulateCost.append(Cost[i])
    else:
        F = Cost[i]+AccumulateCost[i-1]
        AccumulateCost.append(F)
        
AccumulateShare=[] 
for i in range(len(Share)):
    if i == 0:
        AccumulateShare.append(Share[i])
    else:
        F = Share[i]+AccumulateShare[i-1]
        AccumulateShare.append(F)
        
InvestTime_formatted=[]
for i in InvestTime:
    InvestTime_formatted.append(Cf.Correctdateformat(i))

Xaxis_Date=[]
for i in InvestTime_formatted:
    Xaxis_Date.append(date.fromisoformat(i))
    
register_matplotlib_converters()
plt.figure(figsize=(18, 13), dpi= 80)
plt.step(Xaxis_Date,AccumulateCost,'-o',where='post')
plt.xlabel('Time')
plt.ylabel('Dollar ($)')
plt.legend(['Cost'])
plt.show()  


StartTime = InvestTime_formatted[0]    

RawDate = list(Stock["Date"])
RawPrice = list(Stock["BOX Price"])

PlotDate=[]
PriceString = []
for i in range(len(RawDate)):
    if RawDate[i] >= StartTime and RawDate[i]<= LastUpdate:
        PriceString.append(RawPrice[i])
        PlotDate.append(RawDate[i])
        
Date=[]
for i in PlotDate:
    Date.append(date.fromisoformat(i)) 
    
Price=[]
for i in PriceString:
    aa = float(i[1 :])
    Price.append(aa)

register_matplotlib_converters()
figname=StockCode + "_dailyprice.png"
plt.figure(figsize=(18, 13), dpi= 80)
plt.plot(Date,Price,'-o')
plt.xlabel('Time')
plt.ylabel('Price ($)')
plt.legend(['Price'])
plt.savefig(figname)
plt.show() 


DynamicValue=[] 
for i in range(len(Price)):
    ii=len(AccumulateShare)-1
    while Date[i] < Xaxis_Date[ii]:
        ii-=1
    DynamicValue.append(Price[i]*AccumulateShare[ii])

print(len(Xaxis_Date))
print(len(AccumulateShare))
print(len(AccumulateCost))
print(len(Date))
print(len(DynamicValue))

if Xaxis_Date[-1]< Date[-1]:
    AccumulateCost.append(AccumulateCost[-1]) 
    Xaxis_Date.append(Date[-1])

figname3=StockCode + "_RegularPlot.png"
register_matplotlib_converters()
plt.figure(figsize=(18, 13), dpi= 80)
plt.step(Xaxis_Date,AccumulateCost,'-o',where='post')
plt.plot(Date,DynamicValue,'-*')
plt.xlabel('Time')
plt.ylabel('Value ($)')
plt.legend(['Cost','Value'])
plt.savefig(figname3)
plt.show()  


# In[ ]:





# In[ ]:





# In[ ]:




