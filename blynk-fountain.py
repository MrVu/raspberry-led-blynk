import BlynkLib
import RPi.GPIO as GPIO
blynk = BlynkLib.Blynk('a49e0d5f2af8495a9bd5ed7044b31fc5')
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD
GPIO.setup(16, GPIO.OUT)           # set GPIO24 as an output

@blynk.VIRTUAL_WRITE(1)
def my_write_handler(value):
    print('Current V1 value: {}'.format(value))

@blynk.VIRTUAL_WRITE(2)
def led_switch(value):
    print('Current V2 value: {}'.format(value))

while True:
    blynk.run()