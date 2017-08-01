
import time
import os
from ds18b20 import DS18B20

z=0
i = 0
dev=list()
ID=list()

#get file path and make new folder for measurements
filepath=os.getcwd()
newpath = filepath+"/measurements/" 
if not os.path.exists(newpath):
    os.makedirs(newpath)

# test temperature sensors
x = DS18B20()
count=x.device_count()
dev=x.get_dev()

#gets devices ID
if count==0:
    print("No devices available")
while i<count:
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


# one loop through devices
while z < count:
    #gets time and date from ntplib
    dateNow=x.get_ntp_time()
    shortDate=dateNow.strftime("%Y-%m-%d")
    #data is used to display the results in console (can be commented out)
    data=str(dateNow.strftime("%Y-%m-%d %H:%M:%S"))+","+str(ID[z])+": "+str(x.tempC(z))
    print(data)
    #data1 is used to write results in file
    data1=str(dateNow.strftime("%Y-%m-%d %H:%M:%S"))+","+str(x.tempC(z))
    
    #writes data1 into file  
    with open(newpath+str(str(ID[z])+"_"+str(shortDate)+".txt"),'a',encoding = 'utf-8') as theFile:
        theFile.write(str(data1)+"\n")

    z=z+1

z=0
