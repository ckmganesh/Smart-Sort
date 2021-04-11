import RPi.GPIO as GPIO                                
import time
#import requests
#import os

#os.system('fswebcam image.jpg -save /home/pi/Desktop/image.jpg')
#url="https://smart-sort.herokuapp.com/process"
#filess = {"img":open("/home/pi/Desktop/image.jpg","rb")}
#result=requests.post(url,files=filess)
#print(result.text)
GPIO.setmode(GPIO.BOARD)                    
GPIO.setup(12, GPIO.OUT)                    
pwm=GPIO.PWM(12,100)              
pwm.start(5)
angle1=10
duty1= float(angle1)/10 + 2.5               
angle2=200
duty2= float(angle2)/10 + 2.5
ck=0 
"""GPIO.setmode(GPIO.BOARD)                    
GPIO.setup(33, GPIO.OUT)                    
pwm=GPIO.PWM(33,100)              
pwm.start(5)
angle1=10
duty1= float(angle1)/10 + 2.5               
angle2=200
duty2= float(angle2)/10 + 2.5
ck=0
"""
#if result.text=='Biodegradable':
while ck<=5:
    pwm.ChangeDutyCycle(duty1)
    time.sleep(0.8)
    pwm.ChangeDutyCycle(duty2)
    time.sleep(0.8)
    ck=ck+1
time.sleep(1)
"""while ck<=5:
    pwm.ChangeDutyCycle(duty1)
    time.sleep(0.8)
    pwm.ChangeDutyCycle(duty2)
    time.sleep(0.8)
    ck=ck+1
time.sleep(1)"""
GPIO.cleanup()
