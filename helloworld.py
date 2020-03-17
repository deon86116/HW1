# Part. 1

#=======================================

# Import module

#  csv -- fileIO operation

import csv

#=======================================


# Part. 2

#=======================================

# Read cwb weather data

cwb_filename = '106060022.csv'

data = []

header = []

with open(cwb_filename) as csvfile:

   mycsv = csv.DictReader(csvfile)

   header = mycsv.fieldnames

   for row in mycsv:

      data.append(row)

#=======================================


# Part. 3

#=======================================

# Analyze data depend on your group and store it to target_data like:

# Retrive all data points which station id is "C0X260" as a list.

data1 = list(filter(lambda item: item['station_id'] == 'C0A880', data))
data2 = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))
data3 = list(filter(lambda item: item['station_id'] == 'C0G640', data))
data4 = list(filter(lambda item: item['station_id'] == 'C0R190', data))
data5 = list(filter(lambda item: item['station_id'] == 'C0X260', data))
max1=-1000
max2=-1000
max3=-1000
max4=-1000
max5=-1000
min1=100
min2=100
min3=100
min4=100
min5=100
A=2
B=2
C=2
D=2
E=2
for i in data1:
    if float(i['WDSD'])>= max1:
        max1=float(i['WDSD'])
    if float(i['WDSD'])<= min1:
        min1=float(i['WDSD'])
    if  float(i['WDSD'])== -99.000:
        A=0
    elif float(i['WDSD']) == -999.000:
        A=0
ans1=max1-min1

for i in data2:
    if float(i['WDSD'])>= max2:
        max2=float(i['WDSD'])
    if float(i['WDSD'])<= min2:
        min2=float(i['WDSD'])
    if float(i['WDSD'])== -99.000:
        B=0
    elif float(i['WDSD']) == -999.000:
        B=0
ans2=max2-min2

for i in data3:
    if float(i['WDSD'])>= max3:
        max3=float(i['WDSD'])
    if float(i['WDSD'])<= min1:
        min3=float(i['WDSD'])
    if  float(i['WDSD'])== -99.000:
        C=0
    elif float(i['WDSD']) == -999.000:
        C=0
ans3=max3-min3

for i in data4:
    if float(i['WDSD'])>= max4:
        max4=float(i['WDSD'])
    if float(i['WDSD'])<= min4:
        min4=float(i['WDSD'])
    if  float(i['WDSD'])== -99.000:
        D=0
    elif float(i['WDSD']) == -999.000:
        D=0
ans4=max4-min4

for i in data5:
    if float(i['WDSD'])>= max5:
        max5=float(i['WDSD'])
    if float(i['WDSD'])<= min5:
        min5=float(i['WDSD'])
    if  float(i['WDSD'])== -99.000:
        E=0
    elif float(i['WDSD']) == -999.000:
        E=0
ans5=max5-min5


anslist=[]
if A==0:
    anslist.append(['C0A880', 'None'])
else:
    anslist.append(['C0A880', ans1])
if B==0:
    anslist.append(['C0F9A0', 'None'])
else:
    anslist.append(['C0F9A0', ans2])
if C==0:
    anslist.append(['C0G640', 'None'])
else:
    anslist.append(['C0G640', ans3])
if D==0:
    anslist.append(['C0R190', 'None'])
else:
    anslist.append(['C0R190', ans4])
if E==0:
    anslist.append(['C0X260', 'None'])
else:
    anslist.append(['C0X260', ans5])
#=======================================
print (anslist)

# Part. 4

#=======================================

# Print result



#========================================