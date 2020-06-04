#!/usr/bin/env pybricks-micropython
# from pybricks.hubs import EV3Brick
from spike import PrimeHub

# from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from spike import Motor 
from spike import ForceSensor 
from spike import ColorSensor
import utime 
from spike import MotorPair 

# from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
# from hub import (port, stop, direction, button, color, SoundFile, ImageFile, Align)

# from pybricks.tools import print, wait, StopWatch
# from hub import print, wait_for_seconds, StopWatch

# from pybricks.robotics import DriveBase
# import urequests
 
# ev3 = EV3Brick()
hub = PrimeHub()

# Connect motor to port A and touch sensor to port S1
# pointer=Motor(Port.A)
pointer = Motor('A')

# touch=TouchSensor(Port.S1)
 touch = ForceSensor('E')
 
#set the arrow to blue bar (minimum) to begin with
# pointer.reset_angle(0)

pointer.run_to_position(0)
 
# defining the maximum and minimum temperatures shown by the dashboard
# You can change the minimum and maximum temperatures based on your location.
# Calculate where you should place the green (comfortable temperature)
# and yellow (slightly uncomfortable temperature) bars on your design?
 
blue_temp = 0 # minimum temperature in celsius
red_temp = 40 # maximum temperature in celsius
 
# Angle between red and blue bar. 180 degrees in our case.
# It will be based on your gauge design.
angle_bw_blueandred = 180
 
# Get the API key from openweathermap.org and replace the text YOUR_API_KEY with the key
# don't remove the  quotes
# key = "YOUR_API_KEY "
 
# Replace the city id with your city's id
#Find the entire list of id here http://bulk.openweathermap.org/sample/
 
# city_id = "CITY_ID"
 
# base url of the API
# baseurl = "https://api.openweathermap.org/"
 
# format the baseurl, city and API key into a url
# url = baseurl + "data/2.5/weather?id=" + city_id + "&appid=" + key
 
 # we don't know enough about this yet; need to make another file with code and API 
# Defining a function
def turn_pointer():
   # This is how you do a get call using urequests.get. It returns a string in json format
   # ret = urequests.get(url).json()
 
   # ret is a long json string. You can parse the temperature data only by using the following code
   temp_in_kelvin = 300 # the temperature in kelvin
   city_name = ''tester"
   # you can access other information  in 'ret' by changing the 'main' , 'temp' or 'name'
   # to see what other information is contained in ret, remove the comment '#' sign from the code below
 
   # print(ret)
 
   temp_in_celsius = round(temp_in_kelvin -273.15)       # temperature conversion to celsius
   print(temp_in_celsius)                              # prints the data
 
   # each degree of temperature should turn the pointer by one unit_degree
   unit_degree =  angle_bw_blueandred / (red_temp-blue_temp)
 
   # the pointer should turn turn_angle degrees to represent the temp_in_celsius degree temperature
   turn_angle = unit_degree * temp_in_celsius
 
   # move the pointer to turn_angle degrees
   pointer.run_for_degrees(20,turn_angle)
   return temp_in_celsius, city_name
 
counter=180000 #start with 1800 so that the pointer function  (called below)  turns the first time
#runs forever
while True:
 
   #Since the temperature don't change significantly over short period of time
   # we can update the pointer every half an hour
 
   if counter==180000:
       # call the function that moves the motor and save temperature and city name
       temp_in_celsius, city_name = turn_pointer()
 
        # reset counter
       counter = 0               
 
   # increase counter by one     
   counter+ = 1                         
 
   # The EV3 will say out the temperature from the speaker when the touch sensor is pressed
   if touch.is_pressed():
 
       # Try making it say it in different ways
       # ev3.speaker.say("It's "+ str(temp_in_celsius)+ "degree celsius in" + city_name)
       hub.light_matrix.write("It's "+ str(temp_in_celsius)+ "degree celsius in" + city_name)
       
   # wait(10) # wait for 10 milliseconds
utime.sleep(.01)
