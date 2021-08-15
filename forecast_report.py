
import requests
import os
from datetime import datetime

user1_api = 'f995309146b53b7859f2524766a08017'

while True:
    ipaddress = input("Enter the ip address of city: ")
    # ipaddress_kurnool='103.24.127.4'
    # ipaddress_mumbai='45.117.223.255'
    # ipaddress_delhi='47.30.197.190'
    # ipaddress_Bangalore='103.5.135.102'
    # ipaddress_hyderabad='124.123.165.97'
    # ipaddress_kolkata='103.51.149.233'
    # ipaddress_chennai='122.174.109.25'
    # ipaddress_panaji='150.107.16.0'
    # ipaddress_vishakapatnam='203.109.75.58'
    # ipaddress_darjeeling='45.250.244.60'

    if ipaddress == "end" or ipaddress == "quit":
        break

    response = requests.get("http://ip-api.com/json/" + ipaddress).json()
    location1 = response['city']

    complete_api_link = "https://api.openweathermap.org/data/2.5/forecast?q="+location1+"&appid="+user1_api
    api_link = requests.get(complete_api_link)
    api_data1 = api_link.json()

    # create variables to store and display data
    temp_city = ((api_data1['list'][0]['main']['temp']) - 273.15)
    weather_desc = api_data1['list'][0]['weather'][0]['description']
    hmdt = api_data1['list'][0]['main']['humidity']
    wind_spd = api_data1['list'][0]['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print ("-------------------------------------------------------------")
    print ("5 Day Weather Forecast of - {} updated at || {}".format(location1.upper(), date_time))
    print ("-------------------------------------------------------------")

    print ("Expected Average Temperature  : {:.2f} deg C".format(temp_city))
    print ("Expected Weather description  :",weather_desc)
    print ("Expected Average Humidity     :",hmdt, '%')
    print ("Expected Average Wind speed   :",wind_spd ,'kmph')
    print('\n')

#resources :
#https://ip-api.com/docs/api:json - returns city of given Ip address
#https://openweathermap.org/forecast5 - returns weather report of given city
