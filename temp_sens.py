import os
import glob
import time
import datetime
import ntplib
import sys

def get_ntp_time():
        try:
                call = ntplib.NTPClient()
                response = call.request('pool.ntp.org')
                t = datetime.datetime.fromtimestamp(response.tx_time)
                #print(t.strftime("%Y-%m-%d %H:%M:%S"))
                return t
        except:
                e=sys.exc_info()[0]
                write_to_page( "<p>Error: %s</p>" % e )
             
      
get_ntp_time()

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
dev=device_folder.split("/")
dev1=dev[-1]
if dev1=="28-0516212f7fff":
    ID=1
elif dev1=="28-0516212e2bff":
    ID=2
else:
    ID=0

print(ID)
dateNow=get_ntp_time()
shortDate=dateNow.strftime("%Y-%m-%d")


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
while True:
    dateNow=get_ntp_time()
    data=str(dateNow.strftime("%Y-%m-%d %H:%M:%S"))+","+str(read_temp())
    print(data)
    time.sleep(1)

    with open(str(str(ID)+"_"+str(shortDate)+".txt"),'a',encoding = 'utf-8') as theFile:
        theFile.write(str(data)+"\n")
        
    
    
