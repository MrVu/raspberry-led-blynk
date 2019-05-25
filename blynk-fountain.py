import BlynkLib
import RPi.GPIO as GPIO
from time import sleep
blynk = BlynkLib.Blynk('a49e0d5f2af8495a9bd5ed7044b31fc5')
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD
GPIO.setup(16, GPIO.OUT)           # set GPIO24 as an output
GPIO.setup(20, GPIO.OUT)

@blynk.VIRTUAL_WRITE(1)
def my_write_handler(value):
    global valueV1
    valueV1 = value

@blynk.VIRTUAL_WRITE(2)
def led_switch(value):
    global valueV1
    int_value = int(value[0])
    GPIO.output(16, int_value)
    GPIO.output(20, int_value)
    print('Current V2 value: {}'.format(value))
    print('Current V1 value: {}'.format(valueV1))


while True:
    blynk.run()
