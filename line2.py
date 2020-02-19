#import cv2
import RPi.GPIO as IO
import time
import numpy as np
import smtplib 
from time import sleep
#import pyzbar
IO.setwarnings(False)
IO.setmode(IO.BCM)      #Set GPIO pin numbering 

TRIG = 23                                  #Associate pin 23 to TRIG
ECHO = 24                                  #Associate pin 24 to ECHO


IO.setup(TRIG,IO.OUT)                  #Set pin as GPIO out
IO.setup(ECHO,IO.IN)                   #Set pin as GPIO in
def check():
 while True:

   IO.output(TRIG, False)                 #Set TRIG as LOW
   time.sleep(2)                            #Delay of 2 seconds

   IO.output(TRIG, True)                  #Set TRIG as HIGH
   time.sleep(0.00001)                      #Delay of 0.00001 seconds
   IO.output(TRIG, False)                 #Set TRIG as LOW

   while IO.input(ECHO)==0:               #Check whether the ECHO is LOW
    pulse_start = time.time()              #Saves the last known time of LOW pulse

   while IO.input(ECHO)==1:               #Check whether the ECHO is HIGH
    pulse_end = time.time()                #Saves the last known time of HIGH pulse 

   pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

   distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
   distance = round(distance, 2)
   print (distance)
   return distance
   break       #display out of range
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login("amitskotagi.cs18@rvce.edu.in", "Qwerty#0987") 





IO.setup(2,IO.IN) #GPIO 2 -> Left IR out
IO.setup(3,IO.IN) #GPIO 3 -> Right IR out

IO.setup(4,IO.OUT) #GPIO 4 -> Motor 1 terminal A
IO.setup(14,IO.OUT) #GPIO 14 -> Motor 1 terminal B

IO.setup(17,IO.OUT) #GPIO 17 -> Motor Left terminal A
IO.setup(18,IO.OUT) #GPIO 18 -> Motor Left terminal 
IO.setup(26,IO.OUT)#servo
def servom():
    p=IO.PWM(26,50)
    p.start(7.5)
    while 1:
        p.ChangeDutyCycle(2.5)
        sleep(1)
        p.ChangeDutyCycle(12.5)
        sleep(1)
        p.ChangeDutyCycle(2.5)
        sleep(1)
        p.ChangeDutyCycle(7.5)
        sleep(1)
        message = "I can only move straight so please move"
        print("I can only move straight so please move")
        s.sendmail("amitskotagi.cs18@rvce.edu.in", "amitkotagi@gmail.com", message)
        break
def forward():
        IO.output(4,True) #1A+
        IO.output(14,False) #1B-
        IO.output(17,True) #2A+
        IO.output(18,False) #2B-
    
def right():
        IO.output(4,True) #1A+
        IO.output(14,True) #1B-
        IO.output(17,True) #2A+
        IO.output(18,False) #2B-
def left():
        IO.output(4,True) #1A+
        IO.output(14,False) #1B-
        IO.output(17,True) #2A+
        IO.output(18,True) #2B-
    
def back():
        IO.output(4,False) #1A+
        IO.output(14,True) #1B-
        IO.output(17,False) #2A+
        IO.output(18,True) #2B-

def stay():
        IO.output(4,True) #1A+
        IO.output(14,True) #1B-
        IO.output(17,True) #2A+
        IO.output(18,True) #2B-
    

# cap =   cv2.VideoCapture(0)
#font =  cv2.FONT_HERSHEY_PLAIN
while 1:
    d=check()
    print(d)
    if(IO.input(2)==True and IO.input(3)==True and d>30.0): #both while move forward     
        forward()

    elif(IO.input(2)==False and IO.input(3)==True): #turn right  
        right()

    elif(IO.input(2)==True and IO.input(3)==False): #turn left
        left()
    elif(d<=30.0):
        stay()
        servom()
    elif(IO.input(2)==False and IO.input(3)==False):
        stay()
        message = "IM AT Smart Circle"
        print("IM AT Smart Circle")
        
        
        s.sendmail("amitskotagi.cs18@rvce.edu.in", "amitkotagi@gmail.com", message)
            

        
#         _, frame = cap.read()

#         decodedObjects = pyzbar.decode(frame)
#         for obj in decodedObjects:
#             print("Data", obj.data)
#             cv2.putText(frame, str(obj.data), (50, 50), font, 2,(255, 0, 0), 3)
            
            
#             if(obj.data == b'1'):
#                 #                 break  
            
