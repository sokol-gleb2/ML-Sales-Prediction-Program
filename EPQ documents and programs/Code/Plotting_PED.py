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
for i in range(len(names)):
    print(names[i], i)
print("\n")
print("\n")

##using sublists to extract data easier:
BigList = [Mar1_CPW, Mar2_CPW, Apr1_CPW, Apr2_CPW, Apr3_CPW, Apr4_CPW,
           May1_CPW, May2_CPW, May3_CPW, May4_CPW, May5_CPW,
           Jun1_CPW, Jun2_CPW, Jun3_CPW, Jun4_CPW, Jul1_CPW, Jul2_CPW, Jul3_CPW, Jul4_CPW,
           Aug1_CPW, Aug2_CPW, Aug3_CPW, Aug4_CPW, Aug5_CPW,
           Sep1_CPW, Sep2_CPW, Sep3_CPW, Sep4_CPW, Oct1_CPW, Oct2_CPW, Oct3_CPW, Oct4_CPW,
           Nov1_CPW, Nov2_CPW, Nov3_CPW, Nov4_CPW, Nov5_CPW,
           Dec1_CPW, Dec2_CPW, Dec3_CPW, Dec4_CPW,
           Jan21_CPW, Jan22_CPW, Jan23_CPW, Jan24_CPW, Jan25_CPW,
           Feb21_CPW, Feb22_CPW, Feb23_CPW, Feb24_CPW, Mar21_CPW, Mar22_CPW]
dates = ['22/03/2015','29/03/2015','05/04/2015','12/04/2015','19/04/2015','26/04/2015',
         '03/05/2015','10/05/2015','17/05/2015','24/05/2015','31/05/2015',
         '07/06/2015','14/06/2015','21/06/2015','28/06/2015',
         '05/07/2015','12/07/2015','19/07/2015','26/07/2015',
         '02/08/2015','09/08/2015','16/08/2015','23/08/2015','30/08/2015',
         '06/09/2015','13/09/2015','20/09/2015','27/09/2015',
         '04/10/2015','11/10/2015','18/10/2015','25/10/2015',
         '01/11/2015','08/11/2015','15/11/2015','22/11/2015','29/11/2015',
         '06/12/2015','13/12/2015','20/12/2015','27/12/2015',
         '03/01/2016','10/01/2016','17/01/2016','24/01/2016','31/01/2016',
         '07/02/2016','14/02/2016','21/02/2016','28/02/2016',
         '05/03/2016','12/03/2016']


choice = int(input("Choose which products sales data you want to see "))
sales_data = [item[choice] for item in BigList]
print("\n")
print("\n")
print("Here is the sales data for chosen product:")
print("\n")
for k in range(len(sales_data)):
    print(dates[k],':   ',sales_data[k])


##drawing graph of date against sales:
xs = [dt.datetime.strptime(d,'%d/%m/%Y').date() for d in dates]
plt.scatter(xs,sales_data)
plt.xlabel("Time")
plt.ylabel("Units sold")
plt.title('CLOSE THIS WINDOW TO SEE THE TEMPERATURE VS UNITS SOLD GRAPH')
plt.show()

##drawing graph of temp against sales:
temp = open("Factors_updated.txt", "r")
lines = temp.readlines()
temp_xs = []
for x in lines:
    temp_xs.append(x.split(',')[4])
temp.close()
temp_xs.remove('Max Avg Temp C')
temp_xs_float = []
for l in range(len(temp_xs)):
    temp_xs_float.append(float(temp_xs[l]))
slope, intercept, r_value, p_value, std_err = stats.linregress(temp_xs_float, sales_data)
print ("")
print ("The equation of line of best fit for the chosen product is:")
print ('y = ', round(slope,4), '*x + ', round(intercept,4))
plt.scatter(temp_xs_float, sales_data)
plt.xlabel("Temperature")
plt.ylabel("Units sold")
plt.show()
