import RPi.GPIO as GPIO
from time import sleep
#import keyboard
#from pynput.keyboard import Key, Controller

GPIO.setmode(GPIO.BOARD)   
# Pins for Motor Driver Inputs 
Motor1in2 = 16 #IN2  
Motor1in1 = 18 #IN1
Motor1E = 22 #EN

def setup():
    GPIO.setwarnings(False)
               # GPIO Numbering
    GPIO.setup(Motor1in1,GPIO.OUT)  # All pins as Outputs
    GPIO.setup(Motor1in2,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)
    global p
    p = GPIO.PWM(Motor1E, 20)
    #p.start(0)
    
    
def loop():
    p.start(15)
    
  # Going forwards
    GPIO.output(Motor1in1,GPIO.HIGH)
    GPIO.output(Motor1in2,GPIO.LOW)
    #GPIO.output(Motor1E,GPIO.HIGH)
    print("Going forwards")
    '''
   
    sleep(2)
    print('start speed up')
    p.ChangeDutyCycle(60)
    GPIO.output(Motor1in1,GPIO.HIGH)
    GPIO.output(Motor1in2,GPIO.LOW)
    sleep(1)
    p.ChangeDutyCycle(70)
    GPIO.output(Motor1in1,GPIO.HIGH)
    GPIO.output(Motor1in2,GPIO.LOW)
    sleep(2)
    p.ChangeDutyCycle(80)
    GPIO.output(Motor1in1,GPIO.HIGH)
    GPIO.output(Motor1in2,GPIO.LOW)
    sleep(3)
    p.ChangeDutyCycle(90)
    GPIO.output(Motor1in1,GPIO.HIGH)
    GPIO.output(Motor1in2,GPIO.LOW)
    sleep(4)
    p.ChangeDutyCycle(100)
    GPIO.output(Motor1in1,GPIO.HIGH)
    GPIO.output(Motor1in2,GPIO.LOW)
   
    
    '''
    sleep(.2)
    
    GPIO.output(Motor1in1,GPIO.LOW)
    GPIO.output(Motor1in2,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.LOW)
    print("Going backwards")
    
        # Going backwards
    GPIO.output(Motor1in1,GPIO.LOW)
    GPIO.output(Motor1in2,GPIO.HIGH)
    #GPIO.output(Motor1E,GPIO.HIGH)
    print("Going backwards")

    
    sleep(2)
    
    
    # Stop
    GPIO.output(Motor1in1,GPIO.LOW)
    GPIO.output(Motor1in2,GPIO.LOW)
    #GPIO.output(Motor1E,GPIO.LOW)
    
    p.stop()
    
    print("Stop")

def destroy():  
    GPIO.cleanup()

if __name__ == '__main__':     # Program start from here
    setup()
    try:
            loop()
    except KeyboardInterrupt:
        destroy()