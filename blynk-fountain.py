import BlynkLib
import RPi.GPIO as GPIO
from time import sleep
blynk = BlynkLib.Blynk('a49e0d5f2af8495a9bd5ed7044b31fc5')
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD
GPIO.setup(16, GPIO.OUT)           # set GPIO24 as an output
GPIO.setup(20, GPIO.OUT)
@blynk.VIRTUAL_WRITE(1)
def my_write_handler(value):
    while True:
        print('Current V1 value: {}'.format(value))

@blynk.VIRTUAL_WRITE(2)
def led_switch(value):
    int_value = int(value[0])
    if int_value == 1:
        GPIO.output(16, 1)
        GPIO.output(20, 1)
        print('Current V2 value: {}'.format(value))
        sleep(5)
        GPIO.output(16, 0)
        GPIO.output(20, 0)

while True:
    blynk.run()