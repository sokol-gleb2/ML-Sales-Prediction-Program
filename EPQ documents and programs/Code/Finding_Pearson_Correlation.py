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


##using sublists to extract data easier:
BigList = [Mar1_CPW, Mar2_CPW, Apr1_CPW, Apr2_CPW, Apr3_CPW, Apr4_CPW,
           May1_CPW, May2_CPW, May3_CPW, May4_CPW, May5_CPW,
           Jun1_CPW, Jun2_CPW, Jun3_CPW, Jun4_CPW, Jul1_CPW, Jul2_CPW, Jul3_CPW, Jul4_CPW,
           Aug1_CPW, Aug2_CPW, Aug3_CPW, Aug4_CPW, Aug5_CPW,
           Sep1_CPW, Sep2_CPW, Sep3_CPW, Sep4_CPW, Oct1_CPW, Oct2_CPW, Oct3_CPW, Oct4_CPW,
           Nov1_CPW, Nov2_CPW, Nov3_CPW, Nov4_CPW, Nov5_CPW,
           Dec1_CPW, Dec2_CPW, Dec3_CPW, Dec4_CPW]
##sales_data = [item[choice] for item in BigList]
##print("\n")
##print("\n")
##print("Here is the sales data for chosen product:")
##print("\n")
dates = ['22/03/2015','29/03/2015','05/04/2015','12/04/2015','19/04/2015','26/04/2015',
         '03/05/2015','10/05/2015','17/05/2015','24/05/2015','31/05/2015',
         '07/06/2015','14/06/2015','21/06/2015','28/06/2015',
         '05/07/2015','12/07/2015','19/07/2015','26/07/2015',
         '02/08/2015','09/08/2015','16/08/2015','23/08/2015','30/08/2015',
         '06/09/2015','13/09/2015','20/09/2015','27/09/2015',
         '04/10/2015','11/10/2015','18/10/2015','25/10/2015',
         '01/11/2015','08/11/2015','15/11/2015','22/11/2015','29/11/2015',
         '06/12/2015','13/12/2015','20/12/2015','27/12/2015']
##for k in range(len(sales_data)):
##    print(dates[k],':   ',sales_data[k])
##
####drawing graphs:
##xs = [dt.datetime.strptime(d,'%d/%m/%Y').date() for d in dates]
##plt.scatter(xs,sales_data)
##plt.show()

Names = open("Names.txt","r")
lines = Names.readlines()
names = []
for x in lines:
    names.append(x.split(',')[0])
for i in range(len(names)):
    xs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,
          15,16,17,18,19,20,21,22,23,24,25,
          26,27,28,29,30,31,32,33,34,35,36,
          37,38,39,40,41]   
    ys = [item[i] for item in BigList]
    slope, intercept, r_value, p_value, std_err = stats.linregress(xs, ys)
    if(r_value>0):
        print (names[i], "r= ", r_value)
    ys.clear()
    
    


