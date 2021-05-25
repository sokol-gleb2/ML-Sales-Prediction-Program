from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from scipy import stats
from scipy.stats import linregress


##Week ending 22nd March 2015:
March1 = open("Ending_22_Mar_2015.txt", "r")
lines = March1.readlines()
LW = [] ##Last Week
D = [] ##Delivery
TW = [] ##This Week
Mar1_CPW = [] ##Consumption Per Week
for x in lines:
    LW.append(x.split(',')[0]) ##Last Week
    D.append(x.split(',')[1]) ##Delivery
    TW.append(x.split(',')[2]) ##This Week
March1.close()
LW.remove('Last Week')
D.remove('Delivery')
TW.remove('This Week')
for i in range (len(LW)):
    a=float(LW[i])+float(D[i])-float(TW[i])
    Mar1_CPW.append(a)

##Week ending 29th March 2015:
March2 = open("Ending_29_Mar_2015.txt", "r")
lines = March2.readlines()
LW2 = [] ##Last Week
D2 = [] ##Delivery
TW2 = [] ##This Week
Mar2_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
March2.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Mar2_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()
##dif1 = []
##for j in range (len(Mar1_CPW)):
##    d = float(Mar2_CPW[j])-float(Mar1_CPW[j]) 
##    dif1.append(d) ##difference1
##print(dif1)

##Week ending 5 April 2015:
April1 = open("Ending_05_Apr_2015.txt", "r")
lines = April1.readlines()
Apr1_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
April1.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Apr1_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()
##dif2 = []
##for j in range (len(Apr1_CPW)):
##    d = float(Apr1_CPW[j])-float(Mar1_CPW[j]) 
##    dif2.append(d) ##difference1
##print(dif2)

##Week ending 12 April 2015:
April2 = open("Ending_12_Apr_2015.txt", "r")
lines = April2.readlines()
Apr2_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
April2.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Apr2_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 19 April 2015:
April3 = open("Ending_19_Apr_2015.txt", "r")
lines = April3.readlines()
Apr3_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
April3.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Apr3_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()


##Week ending 26 April 2015:
April4 = open("Ending_26_Apr_2015.txt", "r")
lines = April4.readlines()
Apr4_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
April4.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Apr4_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 03 May 2015:
May1 = open("Ending_03_May_2015.txt", "r")
lines = May1.readlines()
May1_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
May1.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    May1_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 10 May 2015:
May2 = open("Ending_10_May_2015.txt", "r")
lines = May2.readlines()
May2_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
May2.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    May2_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 17 May 2015:
May3 = open("Ending_17_May_2015.txt", "r")
lines = May3.readlines()
May3_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
May3.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    May3_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 24 May 2015:
May4 = open("Ending_24_May_2015.txt", "r")
lines = May4.readlines()
May4_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
May4.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    May4_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 31 May 2015:
May5 = open("Ending_31_May_2015.txt", "r")
lines = May5.readlines()
May5_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
May5.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    May5_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 07 June 2015:
June1 = open("Ending_07_Jun_2015.txt", "r")
lines = June1.readlines()
Jun1_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
June1.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Jun1_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 14 June 2015:
June2 = open("Ending_14_Jun_2015.txt", "r")
lines = June2.readlines()
Jun2_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
June2.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Jun2_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 21 June 2015:
June3 = open("Ending_21_Jun_2015.txt", "r")
lines = June3.readlines()
Jun3_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
June3.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Jun3_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 28 June 2015:
June4 = open("Ending_28_Jun_2015.txt", "r")
lines = June4.readlines()
Jun4_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
June4.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Jun4_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 05 July 2015:
July1 = open("Ending_05_Jul_2015.txt", "r")
lines = July1.readlines()
Jul1_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
July1.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Jul1_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 12 July 2015:
July2 = open("Ending_05_Jul_2015.txt", "r")
lines = July2.readlines()
Jul2_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
July2.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Jul2_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 19 July 2015:
July3 = open("Ending_19_Jul_2015.txt", "r")
lines = July3.readlines()
Jul3_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
July3.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Jul3_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 26 July 2015:
July4 = open("Ending_26_Jul_2015.txt", "r")
lines = July4.readlines()
Jul4_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
July4.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Jul4_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 02 August 2015:
August1 = open("Ending_02_Aug_2015.txt", "r")
lines = August1.readlines()
Aug1_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
August1.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Aug1_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 09 August 2015:
August2 = open("Ending_09_Aug_2015.txt", "r")
lines = August2.readlines()
Aug2_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
August2.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Aug2_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 16 August 2015:
August3 = open("Ending_16_Aug_2015.txt", "r")
lines = August3.readlines()
Aug3_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
August3.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Aug3_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 23 August 2015:
August4 = open("Ending_23_Aug_2015.txt", "r")
lines = August4.readlines()
Aug4_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
August4.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Aug4_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 30 August 2015:
August5 = open("Ending_30_Aug_2015.txt", "r")
lines = August5.readlines()
Aug5_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
August5.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Aug5_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 06 September 2015:
September1 = open("Ending_06_Sep_2015.txt", "r")
lines = September1.readlines()
Sep1_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
September1.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Sep1_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 13 September 2015:
September2 = open("Ending_13_Sep_2015.txt", "r")
lines = September2.readlines()
Sep2_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
September2.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Sep2_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 20 September 2015:
September3 = open("Ending_20_Sep_2015.txt", "r")
lines = September3.readlines()
Sep3_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
September3.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Sep3_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 27 September 2015:
September4 = open("Ending_27_Sep_2015.txt", "r")
lines = September4.readlines()
Sep4_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
September4.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Sep4_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 04 October 2015:
October1 = open("Ending_04_Oct_2015.txt", "r")
lines = October1.readlines()
Oct1_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
October1.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Oct1_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 11 October 2015:
October2 = open("Ending_11_Oct_2015.txt", "r")
lines = October2.readlines()
Oct2_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
October2.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Oct2_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 18 October 2015:
October3 = open("Ending_18_Oct_2015.txt", "r")
lines = October3.readlines()
Oct3_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
October3.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Oct3_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 25 October 2015:
October4 = open("Ending_25_Oct_2015.txt", "r")
lines = October4.readlines()
Oct4_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
October4.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Oct4_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 01 November 2015:
November1 = open("Ending_01_Nov_2015.txt", "r")
lines = November1.readlines()
Nov1_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
November1.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Nov1_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 08 November 2015:
November2 = open("Ending_08_Nov_2015.txt", "r")
lines = November2.readlines()
Nov2_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
November2.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Nov2_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 15 November 2015:
November3 = open("Ending_15_Nov_2015.txt", "r")
lines = November3.readlines()
Nov3_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
November3.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Nov3_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 22 November 2015:
November4 = open("Ending_22_Nov_2015.txt", "r")
lines = November4.readlines()
Nov4_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
November4.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Nov4_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 29 November 2015:
November5 = open("Ending_29_Nov_2015.txt", "r")
lines = November5.readlines()
Nov5_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
November5.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Nov5_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 06 December 2015:
December1 = open("Ending_06_Dec_2015.txt", "r")
lines = December1.readlines()
Dec1_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
December1.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Dec1_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 13 December 2015:
December2 = open("Ending_13_Dec_2015.txt", "r")
lines = December2.readlines()
Dec2_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
December2.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Dec2_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 20 December 2015:
December3 = open("Ending_20_Dec_2015.txt", "r")
lines = December3.readlines()
Dec3_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
December3.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Dec3_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 27 December 2015:
December4 = open("Ending_27_Dec_2015.txt", "r")
lines = December4.readlines()
Dec4_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
December4.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Dec4_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 03 January 2016:
January21 = open("Ending_03_Jan_2016.txt", "r")
lines = January21.readlines()
Jan21_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
January21.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Jan21_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 10 January 2016:
January22 = open("Ending_10_Jan_2016.txt", "r")
lines = January22.readlines()
Jan22_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
January22.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Jan22_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 17 January 2016:
January23 = open("Ending_17_Jan_2016.txt", "r")
lines = January23.readlines()
Jan23_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
January23.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Jan23_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 24 January 2016:
January24 = open("Ending_24_Jan_2016.txt", "r")
lines = January24.readlines()
Jan24_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
January24.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Jan24_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 31 January 2016:
January25 = open("Ending_31_Jan_2016.txt", "r")
lines = January25.readlines()
Jan25_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
January25.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Jan25_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 07 February 2016:
February21 = open("Ending_07_Feb_2016.txt", "r")
lines = February21.readlines()
Feb21_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
February21.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Feb21_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 14 February 2016:
February22 = open("Ending_14_Feb_2016.txt", "r")
lines = February22.readlines()
Feb22_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
February22.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Feb22_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 21 February 2016:
February23 = open("Ending_21_Feb_2016.txt", "r")
lines = February23.readlines()
Feb23_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
February23.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Feb23_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 28 February 2016:
February24 = open("Ending_28_Feb_2016.txt", "r")
lines = February24.readlines()
Feb24_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
February24.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Feb24_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 05 March 2016:
March21 = open("Ending_05_Mar_2016.txt", "r")
lines = March21.readlines()
LW2 = [] ##Last Week
D2 = [] ##Delivery
TW2 = [] ##This Week
Mar21_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
March21.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Mar21_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()

##Week ending 12 March 2016:
March22 = open("Ending_12_Mar_2016.txt", "r")
lines = March22.readlines()
LW2 = [] ##Last Week
D2 = [] ##Delivery
TW2 = [] ##This Week
Mar22_CPW = [] ##Consumption Per Week
for x in lines:
    LW2.append(x.split(',')[0]) ##Last Week
    D2.append(x.split(',')[1]) ##Delivery
    TW2.append(x.split(',')[2]) ##This Week
March22.close()
LW2.remove('Last Week')
D2.remove('Delivery')
TW2.remove('This Week')
for i in range (len(LW2)):
    a=float(LW2[i])+float(D2[i])-float(TW2[i])
    Mar22_CPW.append(a)
LW2.clear()
D2.clear()
TW2.clear()



