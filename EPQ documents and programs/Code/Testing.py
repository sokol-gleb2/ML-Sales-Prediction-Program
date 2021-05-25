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
from Extracting_increases import (Fringe_increase, Hunit_increase,
                                    Munit_increase, names)

##Finding temperature equation:
BigList = [Apr4_CPW, May1_CPW, May2_CPW, May3_CPW, May4_CPW, Jun2_CPW, Jun3_CPW, Jun4_CPW,
           Sep1_CPW, Sep2_CPW, Sep3_CPW, Sep4_CPW, Oct1_CPW, Oct2_CPW, Oct3_CPW, Nov3_CPW,
           Nov4_CPW, Nov5_CPW, Dec1_CPW, Jan23_CPW, Jan24_CPW, Jan25_CPW, Feb24_CPW, Mar21_CPW,
           Mar22_CPW]
##BigList only has lists of consuption per week when there are NO factors acting
slopes = []
intercepts = []
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
for i in range(len(names)):
    sales_data = [item[i] for item in BigList]
    Tslope, Tintercept, Tr_value, Tp_value, Tstd_err = stats.linregress(Ttemp_xs_float, sales_data)
    slopes.append(Tslope)
    intercepts.append(Tintercept)
    sales_data.clear()
temps.clear()
temp_xs.clear()
dates.clear()

fringe = []
matches = []
holidays = []
factors = open("Factors_updated.txt", "r")
lines = factors.readlines()
for x in lines:
    temps.append(x.split(',')[4])
    dates.append(x.split(',')[0])
    fringe.append(x.split(',')[6])
    matches.append(x.split(',')[5])
    holidays.append(x.split(',')[7])
factors.close()
temps.remove('Max Avg Temp C')
dates.remove('Date Week Ends On')
fringe.remove('Fringe (1/0)')
matches.remove('Match (1/0)')
holidays.remove('Holidays (1/0)')

fringe_float = []
holidays_float = []
matches_float = []
for l in range(len(fringe)):
    fringe_float.append(float(fringe[l]))
for l in range(len(holidays)):
    holidays_float.append(float(holidays[l]))
for l in range(len(matches)):
    matches_float.append(float(matches[l]))
for l in range(len(temps)):
    temp_xs.append(float(temps[l]))

RealList = [Mar1_CPW, Mar2_CPW, Apr1_CPW, Apr2_CPW, Apr3_CPW, Apr4_CPW,
           May1_CPW, May2_CPW, May3_CPW, May4_CPW, May5_CPW,
           Jun1_CPW, Jun2_CPW, Jun3_CPW, Jun4_CPW, Jul1_CPW, Jul2_CPW, Jul3_CPW, Jul4_CPW,
           Aug1_CPW, Aug2_CPW, Aug3_CPW, Aug4_CPW, Aug5_CPW,
           Sep1_CPW, Sep2_CPW, Sep3_CPW, Sep4_CPW, Oct1_CPW, Oct2_CPW, Oct3_CPW, Oct4_CPW,
           Nov1_CPW, Nov2_CPW, Nov3_CPW, Nov4_CPW, Nov5_CPW,
           Dec1_CPW, Dec2_CPW, Dec3_CPW, Dec4_CPW,
           Jan21_CPW, Jan22_CPW, Jan23_CPW, Jan24_CPW, Jan25_CPW,
           Feb21_CPW, Feb22_CPW, Feb23_CPW, Feb24_CPW, Mar21_CPW, Mar22_CPW]

testing_results = []
for i in range(len(names)):
    difference = []
    predicted_values = []
    for g in range(len(temp_xs)):
        PV = slopes[i]*temp_xs[g] + intercepts[i] + fringe_float[g]*Fringe_increase[i] + holidays_float[g]*Hunit_increase[i] + matches_float[g]*Munit_increase[i]
        predicted_values.append(PV)
    real_values = [item[i] for item in RealList]
    for j in range(len(real_values)):
        if (real_values[j]!=0):
            difference.append(((predicted_values[j]-real_values[j])/real_values[j])*100)
        else:
            difference.append(0)
    testing_results.append(round(sum(difference)/len(difference),2))
    difference.clear()
    predicted_values.clear()
    real_values.clear()

for l in range(len(names)):
    if testing_results[l]>=0:
        print("%-65s %s %s" %(names[l], round((100-testing_results[l]),2), "%"))
    else:
        print("%-65s %s %s" %(names[l], round((100+testing_results[l]),2), "%"))

                


    

