import BlynkLib
from BlynkTimer import BlynkTimer
from time import sleep

blynk = BlynkLib.Blynk('a49e0d5f2af8495a9bd5ed7044b31fc5')
global valueV1, valueV3
valueV1 = ""
valueV3 = ''
timer = BlynkTimer()


def print_5s():
    global valueV3
    print('Current V3 value: {}'.format(valueV3))


def print_2s():
    print('Current V1 value: {}'.format(valueV1))


led = timer.set_interval(0.2, print_5s)
pump = timer.set_interval(0.01, print_2s)
timer.disable(led)
timer.disable(pump)


@blynk.ON("connected")
def blynk_connected():
    # You can also use blynk.sync_virtual(pin)
    # to sync a specific virtual pin
    print("Updating V1,V2,V3 values from the server...")
    blynk.sync_virtual(1, 3)


@blynk.VIRTUAL_WRITE(1)
def light_slider(value):
    global valueV1
    valueV1 = value


@blynk.VIRTUAL_WRITE(3)
def water_slider(value):
    global valueV3
    valueV3 = value


@blynk.VIRTUAL_WRITE(2)
def led_switch(value):
    global valueV1
    global valueV3

    if int(value[0]) == 1:
        print('ON')
        timer.enable(led)
        timer.enable(pump)
    elif int(value[0]) == 0:
        print('OFF')
        timer.disable(led)
        timer.disable(pump)


while True:
    blynk.run()
    timer.run()
