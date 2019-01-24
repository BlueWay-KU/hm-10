# test BLE Scanning software jcs 6/8/2014

import blescan
import sys
import time
import copy
#import pandas as pd

import bluetooth._bluetooth as bluez

dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

sum_L=[0]*60
temp=0

def iBeacon():
        while True:
                returnedList = blescan.parse_events(sock, 10)
                print "----------"
                if len(returnedList)!=0:
                        sort_L=[]
                        for i in returnedList:
                                sum_L[int(i[i.index('x')+1:i.index(',')])]=int(i[i.index(',')+1:])
                        num_L=sum_L[:]
                        copy_L=sum_L[:]
                        for i in range(len(num_L)-1,0,-1):
                                for j in range(i):
                                        if num_L[j]<num_L[j+1]:
                                                temp=num_L[j]
                                                num_L[j]=num_L[j+1]
                                                num_L[j+1]=temp
                        for i in num_L:
                                for j in range(len(copy_L)):
                                        if i!=0 and i==copy_L[j]:
                                                string='num('+str(copy_L.index(i))+')'
                                                string+='_'
                                                string+='RSSI('+str(i)+')'
                                                #sort_L.append(copy_L.index(i))
                                                #sort_L.append(i)
                                                sort_L.append(string)
                                                copy_L[j]=0
                        #print(sum_L)
                        #print(num_L)
                        return sort_L
                                        
                        #dataframe = pd.DataFrame(mean_L)
                        #dataframe.to_csv("/home/pi/pybluez-pybluez-bfaff35/iBeacon-Scanner-/",header=False, index=False)

