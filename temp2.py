# Temp.py
#import sys
#sys.path.append("/pi/temperature")
import time
from ds18b20 import DS18B20
   
# test temperature sensors
x = DS18B20()
count=x.device_count()
i = 0
dev=list()
ID=list()

dev=x.get_dev()
j=len(dev)
print("Devices: "+str(j))
if j==0:
    print("No devices available")
while i<j:
    dev1=dev[i]
    dev2=dev1.split("/")
    dev3=dev2[-2]
    if dev3=="28-0516212f7fff":
        ID.append(1)
    elif dev3=="28-0516212e2bff":
        ID.append(2)
    else:
        ID.append(0)
        print("Device not recognized. You need to check its name first")
    i=i+1

dateNow=x.get_ntp_time()
shortDate=dateNow.strftime("%Y-%m-%d")

z=0

while z < count:
    dateNow=x.get_ntp_time()
    data=str(dateNow.strftime("%Y-%m-%d %H:%M:%S"))+","+str(ID[z])+": "+str(x.tempC(z))
    data1=str(dateNow.strftime("%Y-%m-%d %H:%M:%S"))+","+str(x.tempC(z))
    print(data)
        
    with open(str(str(ID[z])+"_"+str(shortDate)+".txt"),'a',encoding = 'utf-8') as theFile:
        theFile.write(str(data1)+"\n")

    z=z+1

z=0
