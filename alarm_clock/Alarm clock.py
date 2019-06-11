
# Import the time module, it provides various time-related 
# functions. 
import time 
  
#Import pygame.mixer to add sound 
import pygame.mixer
  
# First Input: It is the time of the form 
# 'Hours:Minutes:Seconds' that you'll 
# use to set the alarm. 
Set_Alarm = str(input("Set the website alarm as H:M:S:")) 
  


  
# This is the actual time that we will use to print. 
Actual_Time = time.strftime("%I:%M:%S") 
  
# This is the while loop that'll print the time 
# until it's value will be equal to the alarm time 
while (Actual_Time != Set_Alarm): 
    print ("The time is " + Actual_Time) 
    Actual_Time = time.strftime("%I:%M:%S") 
    time.sleep(1) 
  
  
# This if statement plays the role when its the 
# alarm time and executes the code within it. 
if (Actual_Time == Set_Alarm): 
    pygame.mixer.init()
    pygame.mixer.music.load(open("D:\hello.wav","rb"))

    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(5)

    print ("Wake up")
