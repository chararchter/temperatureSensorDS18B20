import os
import glob
import time
import datetime
import ntplib
import sys
import pathlib

#for ntplib.py
import socket
import struct


from ds18b20 import DS18B20
from pathlib import Path

modulename = 'ntplib'
if modulename not in sys.modules:
    print('You have not imported the module')
else: print('Everything is OK')
