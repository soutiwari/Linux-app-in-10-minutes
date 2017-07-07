#!/usr/bin/python3
import time
from tkinter import *
from tkinter import messagebox
batteryStatusFile="/sys/class/power_supply/BAT1/status"
batteryCapacityFile="/sys/class/power_supply/BAT1/capacity"
def displaymessage(title,text):
    root=Tk()
    root.withdraw()
    if title=="BATTERY FULL":
        msg=messagebox.showinfo(title,text)
    else:
        msg=messagebox.showwarning(title,text)
    root.mainloop()
while True:
    file1=open(batteryCapacityFile,"r")
    file2=open(batteryStatusFile,"r")
    capacity=file1.read().replace('\n','')
    status=file2.read().replace('\n','')
    if capacity=="100" and status=="Full":
        displaymessage("BATTERY FULL","100% CHARGED!!PLEASE REMOVE THE CHARGER TO SAVE ELECTRICITY!!!")
        time.sleep(600)
    elif capacity<="20" and status=="Discharging":
        displaymessage("BATTERY LOW", "BATTERY LOW!!PLEASE SAVE YOUR WORK AND CONNECT TO ADAPTER")
        time.sleep(300)
    else:
        time.sleep(60)

