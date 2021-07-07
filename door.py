import RPi.GPIO as GPIO          
from time import sleep
import time



def dooro():
    in1 = 24
    in2 = 23
    en = 25
    temp1=1

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(en,GPIO.OUT)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    p=GPIO.PWM(en,1000)
    p.start(100)
    p.ChangeDutyCycle(100)
    GPIO.output(in1,GPIO.HIGH)
    print("opening  door")
    GPIO.output(in2,GPIO.LOW)
    sleep(10)
    GPIO.cleanup()
    
    
    
def doorc():
    in1 = 24
    in2 = 23
    en = 25
    temp1=1

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(en,GPIO.OUT)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    p=GPIO.PWM(en,1000)
    p.start(100)
    p.ChangeDutyCycle(100)
    GPIO.output(in1,GPIO.LOW)
    print("closing Door")
    GPIO.output(in2,GPIO.HIGH)
    sleep(10)
    GPIO.cleanup()

def dor():
    dooro()
    print("you can enter now")
    sleep(10)
    doorc()

