from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from scipy import stats
from scipy.stats import linregress
from prettytable import PrettyTable as PT
from Extracting_Info import (Mar1_CPW, Mar2_CPW, Apr1_CPW, Apr2_CPW, Apr3_CPW, Apr4_CPW,
           May1_CPW, May2_CPW, May3_CPW, May4_CPW, May5_CPW,
           Jun1_CPW, Jun2_CPW, Jun3_CPW, Jun4_CPW, Jul1_CPW, Jul2_CPW, Jul3_CPW, Jul4_CPW,
           Aug1_CPW, Aug2_CPW, Aug3_CPW, Aug4_CPW, Aug5_CPW,
           Sep1_CPW, Sep2_CPW, Sep3_CPW, Sep4_CPW, Oct1_CPW, Oct2_CPW, Oct3_CPW, Oct4_CPW,
           Nov1_CPW, Nov2_CPW, Nov3_CPW, Nov4_CPW, Nov5_CPW,
           Dec1_CPW, Dec2_CPW, Dec3_CPW, Dec4_CPW,
           Jan21_CPW, Jan22_CPW, Jan23_CPW, Jan24_CPW, Jan25_CPW,
           Feb21_CPW, Feb22_CPW, Feb23_CPW, Feb24_CPW, Mar21_CPW, Mar22_CPW)
BigList = [Mar2_CPW, Apr1_CPW, Apr2_CPW, Apr3_CPW, Apr4_CPW,
           May1_CPW, May2_CPW, May3_CPW, May4_CPW, May5_CPW,
           Jun1_CPW, Jun2_CPW, Jun3_CPW, Jun4_CPW, Jul1_CPW, Jul2_CPW, Jul3_CPW, Jul4_CPW,
           Aug1_CPW, Aug2_CPW, Aug3_CPW, Aug4_CPW, 
           Sep1_CPW, Sep2_CPW, Sep3_CPW, Sep4_CPW, Oct1_CPW, Oct2_CPW, Oct3_CPW, Oct4_CPW,
           Nov1_CPW, Nov2_CPW, Nov3_CPW, Nov4_CPW, Nov5_CPW,
           Dec1_CPW, Dec2_CPW, Dec3_CPW, Dec4_CPW,
           Jan21_CPW, Jan22_CPW, Jan23_CPW, Jan24_CPW, Jan25_CPW,
           Feb22_CPW, Feb23_CPW, Feb24_CPW, Mar21_CPW, Mar22_CPW]
##Note: Mar1, Aug5 and Feb21 CPW are not in the BigList
MatchList = [Mar1_CPW, Aug5_CPW, Feb21_CPW]
factors = open("Factors_updated.txt", "r")
lines = factors.readlines()
temp = []
dates = []
Mtemp = []
for x in lines:
    temp.append(x.split(',')[4])
    dates.append(x.split(',')[0])
factors.close()
temp.remove('Max Avg Temp C')
dates.remove('Date Week Ends On')
for i in range(len(dates)):
    if dates[i] in ['22.03.15','30.08.15','07.02.16']:
        Mtemp.append(temp[i])
        temp.remove(temp[i])
Mtemperature = [] ##Used to turn Mtemp into float
for k in range(len(Mtemp)):
    Mtemperature.append(float(Mtemp[k]))
temperature = []
for g in range(len(temp)):
    temperature.append(float(temp[g])) ##Needs to be in float for later calculations involving
Names = open("Names.txt","r")          ##line of best fit
lines = Names.readlines()
names = []
for x in lines:
    names.append(x.split(',')[0])
Names.close()

Mpercentages = [] ##will be storing all the percentages for every product here
percentages = []
for l in range(len(names)):
    units_sold = [item[l] for item in BigList]
    slope, intercept, r_value, p_value, std_err = stats.linregress(temperature, units_sold)
    predic_values = [] ##predicted values
    for j in range(len(Mtemperature)):
        predic_values.append(Mtemperature[j]*slope + intercept)
        real_values = [item[l] for item in MatchList]##real values used for comparison with predicted values
    for t in range(len(real_values)):
        percentages.append(round((((real_values[t]-predic_values[t])/predic_values[t])*100),4))
    Mpercentages.append(sum(percentages)/5)
    percentages.clear()
    real_values.clear()
    predic_values.clear()
    units_sold.clear()

##titleProduct = "Product:"
##titlePercent = "Percentage Difference:"
##print("%-65s %s" %(titleProduct, titlePercent))
##for y in range(len(names)):
##    print("%-65s %s" %(names[y], round(Mpercentages[y],2)), "%")
