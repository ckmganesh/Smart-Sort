import RPi.GPIO as GPIO                                
import time
import os
import requests
os.system('fswebcam image.jpg -save /home/pi/Desktop/image.jpg')
url="https://smart-sort.herokuapp.com/process"
filess = {"img":open("/home/pi/Desktop/image.jpg","rb")}
result=requests.post(url,files=filess)
print(result.text)

if result.text=="Biodegradable":
    GPIO.setmode(GPIO.BOARD)                    
    GPIO.setup(29, GPIO.OUT)                    
    pwm=GPIO.PWM(29,50)              
    pwm.start(2.5)
    pwm.ChangeDutyCycle(10)
    time.sleep(0.8)
    pwm.ChangeDutyCycle(12.5)
    time.sleep(0.8)
if result.text=="NonBiodegradable":
    GPIO.setmode(GPIO.BOARD)                    
    GPIO.setup(12, GPIO.OUT)                    
    pwm=GPIO.PWM(12,50)              
    pwm.start(2.5)
    pwm.ChangeDutyCycle(7.5)
    time.sleep(0.8)
    pwm.ChangeDutyCycle(10.5)
    time.sleep(0.8)
"""
Motor 1 9.5 12.5
Motor 2 7.5 10.5
angle1=15
duty1= float(angle1)/18 + 2
pwm.ChangeDutyCycle(duty1)
time.sleep(0.1)
pwm.ChangeDutyCycle(2)
"""

"""angle2=50
duty2= float(angle2)/10 + 2.5
ck=0
while ck<=1:
    pwm.ChangeDutyCycle(duty1)
    time.sleep(0.8)
    pwm.ChangeDutyCycle(duty2)
    time.sleep(0.8)
    ck=ck+1
"""

GPIO.cleanup()