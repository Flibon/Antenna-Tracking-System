import RPi.GPIO as GPIO
from time import sleep
import math

DIR1 = 10 # Direction pin from controller (motor1)
STEP1 = 8 # Step pin from controller (motor1)
DIR2 = 18 # Direction pin from controller (motor2)
STEP2 = 16 # Step pin from controller (motor2)
CW = 1 # 0/1 used to signify clockwise or counterclockwise.
CCW = 0

#               SETTING UP PINS AND OUTPUT
GPIO.setmode(GPIO.BOARD)
GPIO.setup(DIR1, GPIO.OUT)
GPIO.setup(STEP1, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(STEP2, GPIO.OUT)

def motor_control(motor_num,Direction,steps,speed_delay,cycles):
    count=0
    steps=int(steps)
    if motor_num ==1:
        GPIO.output(DIR1,Direction)
        while count<int(cycles):
            count+=1
            for x in range(steps):
                GPIO.output(STEP1,GPIO.HIGH)
                sleep(speed_delay)
                GPIO.output(STEP1,GPIO.LOW)
                sleep(speed_delay)
    elif motor_num ==2:
        GPIO.output(DIR2,Direction)
        while count<int(cycles):
            count+=1
            for x in range(steps):
                GPIO.output(STEP2,GPIO.HIGH)
                sleep(speed_delay)
                GPIO.output(STEP2,GPIO.LOW)
                sleep(speed_delay)

def heading(lat1, long1, h1, lat2, long2, h2):
    dLon = (long2 - long1)
    y = math.sin(dLon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dLon)
    brng = math.atan2(y, x)
    brng = math.degrees(brng)
    brng = (brng + 360) % 360
    brng = 360 - brng 
    stepsh=(960*brng)/360

    lat1 = math.radians(lat1)
    long1 = math.radians(long1)
    lat2 = math.radians(lat2)
    long2 = math.radians(long2)

    R = 6371 # radius of the Earth in km
    
    d = math.acos(math.sin(lat1) * math.sin(lat2) + 
                  math.cos(lat1) * math.cos(lat2) * math.cos(long2 - long1)) * R
    if h1!=h2:
        if h1>h2:
            z=h1-h2
        elif h1<h2:
            z=h2-h1
        angle = math.atan2(z, d) * (180/ math.pi)
        print("Elevation Angle = ",angle)
    else:
        angle=0
        print(angle)    
    steps=(960*angle)/360
    print("Steps taken = "+str(steps))
    return brng,stepsh,angle,steps

while True:
    motor_control(1,1,heading(28.739668,77.125360,0,28.751394,77.117531,5.7),0.0005,4) #960 steps for 360 degrees rotation
    print('Task Completed')
    print("cleanup")
    sleep(5)

