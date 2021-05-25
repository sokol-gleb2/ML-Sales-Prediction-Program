##This document is the same as Finding_Fringe_Per.py except there's no commands like print so
##when I import arrays from here in other progeammes it doesn't print out the percentages but
##does what I wan to do with them

from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from scipy import stats
from scipy.stats import linregress
from Extracting_Info import (Mar1_CPW, Mar2_CPW, Apr1_CPW, Apr2_CPW, Apr3_CPW, Apr4_CPW,
           May1_CPW, May2_CPW, May3_CPW, May4_CPW, May5_CPW,
           Jun1_CPW, Jun2_CPW, Jun3_CPW, Jun4_CPW, Jul1_CPW, Jul2_CPW, Jul3_CPW, Jul4_CPW,
           Aug1_CPW, Aug2_CPW, Aug3_CPW, Aug4_CPW, Aug5_CPW,
           Sep1_CPW, Sep2_CPW, Sep3_CPW, Sep4_CPW, Oct1_CPW, Oct2_CPW, Oct3_CPW, Oct4_CPW,
           Nov1_CPW, Nov2_CPW, Nov3_CPW, Nov4_CPW, Nov5_CPW,
           Dec1_CPW, Dec2_CPW, Dec3_CPW, Dec4_CPW,
           Jan21_CPW, Jan22_CPW, Jan23_CPW, Jan24_CPW, Jan25_CPW,
           Feb21_CPW, Feb22_CPW, Feb23_CPW, Feb24_CPW, Mar21_CPW, Mar22_CPW)
factors = open("Factors_updated.txt", "r")
lines = factors.readlines()
temp = []
dates = []
Fringe_temp = []
for x in lines:
    temp.append(x.split(',')[4])
    dates.append(x.split(',')[0])
factors.close()
temp.remove('Max Avg Temp C')
dates.remove('Date Week Ends On')

##removing temp of weeks that were doing Fringe and placing them into a new array Fringe_temp:
for i in range(len(dates)):
    if dates[i] in ['9.08.15','16.08.15','23.08.15','30.08.15','6.09.15']:
        temp.remove(temp[i])
        Fringe_temp.append(temp[i])
BigList = [Mar1_CPW, Mar2_CPW, Apr1_CPW, Apr2_CPW, Apr3_CPW, Apr4_CPW,
           May1_CPW, May2_CPW, May3_CPW, May4_CPW, May5_CPW,
           Jun1_CPW, Jun2_CPW, Jun3_CPW, Jun4_CPW, Jul1_CPW, Jul2_CPW, Jul3_CPW, Jul4_CPW,
           Aug1_CPW, Sep2_CPW, Sep3_CPW, Sep4_CPW, Oct1_CPW, Oct2_CPW, Oct3_CPW, Oct4_CPW,
           Nov1_CPW, Nov2_CPW, Nov3_CPW, Nov4_CPW, Nov5_CPW,
           Dec1_CPW, Dec2_CPW, Dec3_CPW, Dec4_CPW,
           Jan21_CPW, Jan22_CPW, Jan23_CPW, Jan24_CPW, Jan25_CPW,
           Feb21_CPW, Feb22_CPW, Feb23_CPW, Feb24_CPW, Mar21_CPW, Mar22_CPW]
##Note to Marker: Aug2, Aug3, Aug4, Aug5 and Sep1 CPW is missing from the BigList as that's
##when Fringe was going on
FringeList = [Aug2_CPW, Aug3_CPW, Aug4_CPW, Aug5_CPW, Sep1_CPW]

Fringe_temperature = [] ##Used to turn Fringe_temp into float
for k in range(len(Fringe_temp)):
    Fringe_temperature.append(float(Fringe_temp[k]))
temperature = []
for g in range(len(temp)):
    temperature.append(float(temp[g])) ##Needs to be in float for later calculations involving
Names = open("Names.txt","r")          ##line of best fit
lines = Names.readlines()
names = []
for x in lines:
    names.append(x.split(',')[0])
Names.close()

##Up to this point, it's all been about extracting info from files
##Next Part finds percentage increase due to Fringe:
Fringe_percentages = [] ##will be storing all the percentages for every product here
percentages = []
Fringe_UI = []
Fringe_unit_increase = [] ##needed in "Finding_Fringe_Matches_Holidays_Percentages.py"
for l in range(len(names)):
    units_sold = [item[l] for item in BigList]
    slope, intercept, r_value, p_value, std_err = stats.linregress(temperature, units_sold)
    predic_values = [] ##predicted values
    for j in range(len(Fringe_temperature)):
        predic_values.append(Fringe_temperature[j]*slope + intercept)
        real_values = [item[l] for item in FringeList]##real values used for comparison with predicted values
    for t in range(len(real_values)):
        percentages.append(round((((real_values[t]-predic_values[t])/predic_values[t])*100),4))
        Fringe_UI.append(real_values[t]-predic_values[t])
    Fringe_unit_increase.append(sum(Fringe_UI)/5)
    Fringe_UI.clear()
    Fringe_percentages.append(sum(percentages)/5)
    percentages.clear()
    real_values.clear()
    predic_values.clear()
    units_sold.clear()


