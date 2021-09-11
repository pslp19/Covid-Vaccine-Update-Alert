# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 02:23:55 2021

@author: Ramasiva Majji
"""

import requests
import time
from playsound import playsound


pincode = input("Enter Your Pincode: ")

date = input("Enter Date of Vaccine, format(dd-mm-yyyy): ")

age = int(input("Enter Your Age: "))

URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pincode, date)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}


def findAvailability():
    counter = 0
    result = requests.get(URL, headers=header)
    response_json = result.json()
    for center in response_json["centers"]:
        for session in center["sessions"]:
            if((session["available_capacity_dose1"] > 0) & (session["min_age_limit"] <= age)):
                counter += 1
                
               # print("\t Pincode:", center["pincode"])
                
                print("\n \t Vaccine Status: Available :) \n\n Fetching details...")
                
                print("\n     ........" "\n     ........" "\n     ........\n")
               
                
                
                print("\t Center Name:", center["name"])
                print("\t Address:", center["address"])
                print("\t Block Name:", center["block_name"])
                print("\t Price:", center["fee_type"])
                
                
                print("\t Vaccine Name:", session["vaccine"])
                print("\t Available Capacity:", session["available_capacity"])
                
                print("\n Alert Tone is Playing..... \n")
                playsound('C:/Users/Prasanna/Downloads/Final.zip/Final/Alert.mp3')
                print("Alert completed. Goto Cowin portal and Register your Slot. \n Thank you...")
                
                return True
    if(counter == 0):
        print("No Available Slots")
        return False


while(findAvailability() != True):
    time.sleep(5)
    findAvailability()