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
Names = open("Names.txt","r")          
lines = Names.readlines()
names = []
for x in lines:
    names.append(x.split(',')[0])
Names.close()
for i in range(len(names)):
    print(names[i], i)
print("\n")

##Finding Match Percentages:
MatchBigList = [Mar2_CPW, Apr1_CPW, Apr2_CPW, Apr3_CPW, Apr4_CPW,
           May1_CPW, May2_CPW, May3_CPW, May4_CPW, May5_CPW,
           Jun1_CPW, Jun2_CPW, Jun3_CPW, Jun4_CPW, Jul1_CPW, Jul2_CPW, Jul3_CPW, Jul4_CPW,
           Aug1_CPW, Aug2_CPW, Aug3_CPW, Aug4_CPW, Aug5_CPW,
           Sep1_CPW, Sep2_CPW, Sep3_CPW, Sep4_CPW, Oct1_CPW, Oct2_CPW, Oct3_CPW, Oct4_CPW,
           Nov1_CPW, Nov2_CPW, Nov3_CPW, Nov4_CPW, Nov5_CPW,
           Dec1_CPW, Dec2_CPW, Dec3_CPW, Dec4_CPW,
           Jan21_CPW, Jan22_CPW, Jan23_CPW, Jan24_CPW, Jan25_CPW,
           Feb22_CPW, Feb23_CPW, Feb24_CPW, Mar21_CPW, Mar22_CPW]
##Note: Mar1_CPW and Feb21_CPW are missing from the list - the 2 weeks where there's a match and
##no fringe nor holidays
MatchList = [Mar1_CPW, Feb21_CPW]
Mfactors = open("Factors_updated.txt", "r")
lines = Mfactors.readlines()
temp = []
dates = []
Mtemp = []
NMtemp = [] ##non match temp
for x in lines:
    temp.append(x.split(',')[4])
    dates.append(x.split(',')[0])
Mfactors.close()
temp.remove('Max Avg Temp C')
dates.remove('Date Week Ends On')
for i in range(len(dates)):
    if dates[i] in ['22.03.15','07.02.16']:
        Mtemp.append(temp[i])
    else:
        NMtemp.append(temp[i])
Mtemperature = [] ##Used to turn Mtemp into float
for k in range(len(Mtemp)):
    Mtemperature.append(float(Mtemp[k]))
temperature = []
for g in range(len(NMtemp)):
    temperature.append(float(NMtemp[g])) ##Needs to be in float for later calculations involving
Names = open("Names.txt","r")          ##line of best fit
lines = Names.readlines()
names = []
for x in lines:
    names.append(x.split(',')[0])
Names.close()

Mpercentages = [] ##will be storing all the percentages for every product here
percentages = []
M_UI = []
Munit_increase = []
for l in range(len(names)):
    units_sold = [item[l] for item in MatchBigList]
    Mslope, Mintercept, Mr_value, Mp_value, Mstd_err = stats.linregress(temperature, units_sold)
    Mpredic_values = [] ##predicted values
    for j in range(len(Mtemperature)):
        Mpredic_values.append(Mtemperature[j]*Mslope + Mintercept)
        Mreal_values = [item[l] for item in MatchList]##real values used for comparison with predicted values
    for t in range(len(Mreal_values)):
        percentages.append(round((((Mreal_values[t]-Mpredic_values[t])/Mpredic_values[t])*100),4))
        M_UI.append(Mreal_values[t]-Mpredic_values[t])
    Munit_increase.append(sum(M_UI)/2)
    M_UI.clear()
    Mpercentages.append(sum(percentages)/5)
    percentages.clear()
    Mreal_values.clear()
    Mpredic_values.clear()
    units_sold.clear()
temp.clear()     ##this is to use them again later
dates.clear()


##Finding Hols Percentages:
HolsBigList = [Mar1_CPW, Apr4_CPW,
           May1_CPW, May2_CPW, May3_CPW, May4_CPW, Jun2_CPW, Jun3_CPW, Jun4_CPW,
           Sep1_CPW, Sep2_CPW, Sep3_CPW, Sep4_CPW, Oct1_CPW, Oct2_CPW, Oct3_CPW,
           Nov3_CPW, Nov4_CPW, Nov5_CPW,
           Dec1_CPW, Jan23_CPW, Jan24_CPW, Jan25_CPW,
           Feb21_CPW, Feb24_CPW, Mar21_CPW, Mar22_CPW]
##Note that all the weeks that are holidays for school and university students are missing -
##but not the ones overlapping with fringe or matches
HolsList = [Mar2_CPW, Apr1_CPW, Apr2_CPW, Apr3_CPW, May5_CPW, Jun1_CPW, Jul1_CPW, Jul2_CPW,
            Jul3_CPW, Jul4_CPW, Aug1_CPW, Aug2_CPW, Aug3_CPW, Aug4_CPW, Aug5_CPW, Oct4_CPW,
            Nov1_CPW, Nov2_CPW, Dec2_CPW, Dec3_CPW, Dec4_CPW, Jan21_CPW, Jan22_CPW, Feb22_CPW,
            Feb23_CPW]
factors = open("Factors_updated.txt", "r")
lines = factors.readlines()
for x in lines:
    temp.append(x.split(',')[4])
    dates.append(x.split(',')[0])
factors.close()
temp.remove('Max Avg Temp C')
dates.remove('Date Week Ends On')
Htemp = []
NHtemp = [] ##non holiday temp
for i in range(len(dates)):
    if dates[i] in ['29.03.15','05.04.15','12.04.15','19.04.15', '31.05.15','7.06.15',
                    '05.07.15','12.07.15','19.07.15','26.07.15','2.08.15', '9.08.15',
                    '16.08.15', '23.08.15', '30.08.15','25.10.15','1.11.15','8.11.15',
                    '13.12.15','20.12.15','27.12.15','03.01.16','10.01.16','14.02.16',
                    '21.02.16']:
        Htemp.append(temp[i])
    else:
        NHtemp.append(temp[i])
Htemperature = []
for k in range(len(Htemp)):
    Htemperature.append(float(Htemp[k]))
temperature2 = []
for g in range(len(NHtemp)):
    temperature2.append(float(NHtemp[g]))

Hpercentages = []
percentages2 = []
Hunit_increase = []
H_UI = []
for l in range(len(names)):
    Hunits_sold = [item[l] for item in HolsBigList]
    Hslope, Hintercept, Hr_value, Hp_value, Hstd_err = stats.linregress(temperature2, Hunits_sold)
    Hpredic_values = [] ##predicted values during holidays
    for j in range(len(Htemperature)):
        Hpredic_values.append(Htemperature[j]*Hslope + Hintercept)
        Hreal_values = [item[l] for item in HolsList]##real values used for comparison with predicted values
    for t in range(len(Hreal_values)):
        percentages2.append(round((((Hreal_values[t]-Hpredic_values[t])/Hpredic_values[t])*100),4))
        H_UI.append(Hreal_values[t]-Hpredic_values[t])
    Hunit_increase.append(sum(H_UI)/25)
    H_UI.clear()
    Hpercentages.append(sum(percentages2)/25)
    percentages2.clear()
    Hreal_values.clear()
    Hpredic_values.clear()
    Hunits_sold.clear()
temp.clear()
dates.clear()

##Finding Fringe Percentages:
from Fringe_Percentages_Extracting import Fringe_unit_increase
FringeList = [Aug2_CPW, Aug3_CPW, Aug4_CPW, Aug5_CPW, Sep1_CPW]
Fringe_increase = []
for i in range(len(names)):
    if Hunit_increase[i]>=0:
        Fringe_increase.append(Fringe_unit_increase[i]-Hunit_increase[i])
    else:
        Fringe_increase.append(Fringe_unit_increase[i]+Hunit_increase[i])

choice = int(input("Choose which product info you would like to see: "))
##Finding temperature equation:
BigList = [Apr4_CPW, May1_CPW, May2_CPW, May3_CPW, May4_CPW, Jun2_CPW, Jun3_CPW, Jun4_CPW,
           Sep1_CPW, Sep2_CPW, Sep3_CPW, Sep4_CPW, Oct1_CPW, Oct2_CPW, Oct3_CPW, Nov3_CPW,
           Nov4_CPW, Nov5_CPW, Dec1_CPW, Jan23_CPW, Jan24_CPW, Jan25_CPW, Feb24_CPW, Mar21_CPW,
           Mar22_CPW]
##BigList only has lists of consuption per week when there are NO factors acting
sales_data = [item[choice] for item in BigList]
temp = open("Factors_updated.txt", "r")
lines = temp.readlines()
temp_xs = []
temps = []
dates = []
for x in lines:
    temps.append(x.split(',')[4])
    dates.append(x.split(',')[0])
temp.close()
dates.remove('Date Week Ends On')
temps.remove('Max Avg Temp C')
for i in range(len(dates)):
    if dates[i] in ['26.04.15', '3.05.15', '10.05.15', '17.05.15', '24.05.15', '14.06.15',
                    '21.06.15', '28.06.15', '6.09.15', '13.09.15', '20.09.15', '27.09.15', '4.10.15',
                    '11.10.15', '18.10.15', '15.11.15', '22.11.15', '29.11.15', '06.12.15', '17.01.16',
                    '24.01.16', '31.01.16', '28.02.16', '05.03.16', '12.03.16']:
        temp_xs.append(temps[i])
Ttemp_xs_float = []
for l in range(len(temp_xs)):
    Ttemp_xs_float.append(float(temp_xs[l]))
Tslope, Tintercept, Tr_value, Tp_value, Tstd_err = stats.linregress(Ttemp_xs_float, sales_data)



##Table:
print("%-15s %-30s %s" %("        ", "Coeficient", "Intercept"))
print("%-15s %s" %("Fringe  ", Fringe_increase[choice]))
print("%-15s %s" %("Holidays", Hunit_increase[choice]))
print("%-15s %s" %("Matches ", Munit_increase[choice]))
print("%-15s %-30s %s" %("Temp    ", Tslope, Tintercept))

print("\n")
print("The Multiple Linear Regression equation for the chosen product is: ")
print("Y = ", round(Tintercept,2), " + ", round(Tslope,2), "*temp  + ", round(Fringe_increase[choice],2), "*fringe  + ", round(Hunit_increase[choice],2), "*holidays  + ",  round(Munit_increase[choice],2), "*match")
print("")
print("Note: fringe, holidays and match can only be either 1 or 0")



