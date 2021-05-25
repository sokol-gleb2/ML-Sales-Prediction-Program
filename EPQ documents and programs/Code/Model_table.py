##The idea behind this programme is to print out a table between {Temperature, Fringe, Matches,
##Holidays} and Sales
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
BigList = [Mar1_CPW, Mar2_CPW, Apr1_CPW, Apr2_CPW, Apr3_CPW, Apr4_CPW,
           May1_CPW, May2_CPW, May3_CPW, May4_CPW, May5_CPW,
           Jun1_CPW, Jun2_CPW, Jun3_CPW, Jun4_CPW, Jul1_CPW, Jul2_CPW, Jul3_CPW, Jul4_CPW,
           Aug1_CPW, Aug2_CPW, Aug3_CPW, Aug4_CPW, Aug5_CPW,
           Sep1_CPW, Sep2_CPW, Sep3_CPW, Sep4_CPW, Oct1_CPW, Oct2_CPW, Oct3_CPW, Oct4_CPW,
           Nov1_CPW, Nov2_CPW, Nov3_CPW, Nov4_CPW, Nov5_CPW,
           Dec1_CPW, Dec2_CPW, Dec3_CPW, Dec4_CPW,
           Jan21_CPW, Jan22_CPW, Jan23_CPW, Jan24_CPW, Jan25_CPW,
           Feb21_CPW, Feb22_CPW, Feb23_CPW, Feb24_CPW, Mar21_CPW, Mar22_CPW]
Names = open("Names.txt","r")          
lines = Names.readlines()
names = []
for x in lines:
    names.append(x.split(',')[0])
Names.close()
for i in range(len(names)):
    print(names[i], i)
print("\n")
choice = int(input("Choose which products sales data you want to see "))
sales_data = [item[choice] for item in BigList]
print("%-15s %-15s %-15s %-15s %-15s %s" %("    ", "Coef", "Stand. Err.", "95% Conf Int: Lower Bound,", "Upper Bound", "Percentage Difference"))

##Temperature row:
temp = open("Factors_updated.txt", "r")
lines = temp.readlines()
temp_xs = []
for x in lines:
    temp_xs.append(x.split(',')[4])
temp.close()
temp_xs.remove('Max Avg Temp C')
Ttemp_xs_float = []
Ttemp_squared = [] ##needed later for calculatin standard deviation
for l in range(len(temp_xs)):
    Ttemp_xs_float.append(float(temp_xs[l]))
    Ttemp_squared.append(Ttemp_xs_float[l]**2)
Tslope, Tintercept, Tr_value, Tp_value, Tstd_err = stats.linregress(Ttemp_xs_float, sales_data)
##Calculating 95% Confidence Interval:
Tmean = round(sum(Ttemp_xs_float)/len(Ttemp_xs_float), 2)
Tstd_dev = ((sum(Ttemp_squared)/len(Ttemp_squared)) - Tmean**2)**0.5 ##mean of squares - square of means
TLower_bound = round(Tmean - 1.96*(Tstd_dev/(len(Ttemp_xs_float)**0.5)), 2)
TUpper_bound = round(Tmean + 1.96*(Tstd_dev/(len(Ttemp_xs_float)**0.5)), 2)

print("%-15s %-15s %-30s %-15s %s" %("Temp", round(Tslope,2), round(Tstd_err,2), TLower_bound, TUpper_bound))

##Fringe Row:
factors = open("Factors_updated.txt", "r")
lines = factors.readlines()
Ftemp = []
Fdates = []
Fringe_temp = []
Ftemp_squared = []
for x in lines:
    Ftemp.append(x.split(',')[4])
    Fdates.append(x.split(',')[0])
factors.close()
Ftemp.remove('Max Avg Temp C')
Fdates.remove('Date Week Ends On')
##removing temp of weeks that were doing Fringe and placing them into a new array Fringe_temp:
for i in range(len(Fdates)):
    if Fdates[i] in ['9.08.15','16.08.15','23.08.15','30.08.15','6.09.15']:
        Ftemp.remove(Ftemp[i])
        Fringe_temp.append(Ftemp[i])
FringeList = [Aug2_CPW, Aug3_CPW, Aug4_CPW, Aug5_CPW, Sep1_CPW]
units_sold = [item[choice] for item in FringeList]
Fringe_temperature = [] ##Used to turn Fringe_temp into float
for k in range(len(Fringe_temp)):
    Fringe_temperature.append(float(Fringe_temp[k]))
    Ftemp_squared.append(Fringe_temperature[k]**2)
Fslope, Fintercept, Fr_value, Fp_value, Fstd_err = stats.linregress(Fringe_temperature, units_sold)
##Calculating 95% Confidence Interval:
Fmean = round(sum(Fringe_temperature)/len(Fringe_temperature), 2)
Fstd_dev = ((sum(Ftemp_squared)/len(Ftemp_squared)) - Fmean**2)**0.5 ##mean of squares - square of means
FLower_bound = round(Fmean - 1.96*(Fstd_dev/(len(Fringe_temperature)**0.5)), 2)
FUpper_bound = round(Fmean + 1.96*(Fstd_dev/(len(Fringe_temperature)**0.5)), 2)
##Importing Percentage increase/decrease from Fringe_percentages.py
from Fringe_Percentages_Extracting import Fringe_percentages
Fpercentage = Fringe_percentages[choice]

print("%-15s %-15s %-30s %-15s %-15s %s" %("Fringe", round(Fslope,2), round(Fstd_err,2), FLower_bound, FUpper_bound, round(Fpercentage,2)))

##Matches Row:
factors = open("Factors_updated.txt", "r")
lines = factors.readlines()
Matches = []
Mtemp = []
Mdates = []
Match_temp = []
for x in lines:
    Matches.append(x.split(',')[5])
    Mtemp.append(x.split(',')[4])
    Mdates.append(x.split(',')[0])
Matches.remove("Match (1/0)")
Mdates.remove("Date Week Ends On")
Mtemp.remove("Max Avg Temp C")
for i in range(len(Mdates)):
    if Mdates[i] in ['22.03.15','30.08.15','07.02.16']:
        Mtemp.remove(Mtemp[i])
        Match_temp.append(Mtemp[i])
Mtemperature = []
Mtemp_squared = []
for k in range(len(Match_temp)):
    Mtemperature.append(float(Match_temp[k]))
    Mtemp_squared.append(Mtemperature[k]**2)
MatchList = [Mar1_CPW, Aug5_CPW, Feb21_CPW]
sold = [item[choice] for item in MatchList]
Mslope, Mintercept, Mr_value, Mp_value, Mstd_err = stats.linregress(Mtemperature, sold)
##Calculating 95% Confidence Interval:
Mmean = round(sum(Mtemperature)/len(Mtemperature), 2)
Mstd_dev = ((sum(Mtemp_squared)/len(Mtemp_squared)) - Mmean**2)**0.5 ##mean of squares - square of means
MLower_bound = round(Mmean - 1.96*(Mstd_dev/(len(Mtemperature)**0.5)), 2)
MUpper_bound = round(Mmean + 1.96*(Mstd_dev/(len(Mtemperature)**0.5)), 2)
##Importing Match percentage increase/decrease from Match_precentages.py
from Match_percentages import Mpercentages
Mpercentage = Mpercentages[choice]

print("%-15s %-15s %-30s %-15s %-15s %s" %("Matches", round(Mslope,2), round(Mstd_err,2), MLower_bound, MUpper_bound, round(Mpercentage,2)))





