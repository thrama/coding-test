#!/bin/python3

import os
import sys

def timeConversion(s):
    """
    Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
    Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on 
    a 12-hour clock, and 12:00:00 on a 24-hour clock. 
    """

    if s == "12:00:00AM": #mezzanotte
        return "00:00:00"
    elif s == "12:00:00PM": #mezzogiorno
        return "12:00:00"
    else:
        arr=s.split(':')

        if s.find("PM") != -1:  #PM
            arr[0] = str(int(arr[0])+12)
            if arr[0] == "24": arr[0]="12"
            arr[2] = arr[2].replace("PM", "")
            #print("P")
        else:                   #AM
            if arr[0] == "12": arr[0]="00"
            arr[2] = arr[2].replace("AM", "")
            #print("A")
    
        #print(arr)

        return arr[0]+":"+arr[1]+":"+arr[2]


#s = "12:45:54PM"
s = input("Insert you 12-time format string (ei. 12:45:54PM): ")
result = timeConversion(s)

print(result)