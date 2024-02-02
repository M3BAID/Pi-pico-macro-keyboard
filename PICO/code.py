import time
import board
import digitalio
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

keyboard = Keyboard(usb_hid.devices)
btn1_pin = board.GP0
btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2_pin = board.GP1
btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3_pin = board.GP2
btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4_pin = board.GP3
btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5_pin = board.GP4
btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6_pin = board.GP5
btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

btn7_pin = board.GP7
btn7 = digitalio.DigitalInOut(btn7_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.DOWN

btn8_pin = board.GP8
btn8 = digitalio.DigitalInOut(btn8_pin)
btn8.direction = digitalio.Direction.INPUT
btn8.pull = digitalio.Pull.DOWN

btn9_pin = board.GP9
btn9 = digitalio.DigitalInOut(btn9_pin)
btn9.direction = digitalio.Direction.INPUT
btn9.pull = digitalio.Pull.DOWN

btn10_pin = board.GP10
btn10 = digitalio.DigitalInOut(btn10_pin)
btn10.direction = digitalio.Direction.INPUT
btn10.pull = digitalio.Pull.DOWN

btn11_pin = board.GP11
btn11 = digitalio.DigitalInOut(btn11_pin)
btn11.direction = digitalio.Direction.INPUT
btn11.pull = digitalio.Pull.DOWN

btn12_pin = board.GP12
btn12 = digitalio.DigitalInOut(btn12_pin)
btn12.direction = digitalio.Direction.INPUT
btn12.pull = digitalio.Pull.DOWN

led.value = True
time.sleep(0.5)
led.value = False
time.sleep(0.1)
while True:
    if btn1.value:
        keyboard.send(Keycode.SHIFT, Keycode.F1)
        led.value = True
        time.sleep(0.08)
        led.value = False

    if btn2.value:
        keyboard.send(Keycode.SHIFT, Keycode.F9)
        led.value = True
        time.sleep(0.08)
        led.value = False

    if btn3.value:
        keyboard.send(Keycode.SHIFT, Keycode.F6)
        led.value = True
        time.sleep(0.08)
        led.value = False

    if btn4.value:
        keyboard.send(Keycode.SHIFT, Keycode.F7)
        led.value = True
        time.sleep(0.08)
        led.value = False

    if btn5.value:
        keyboard.send(Keycode.SHIFT, Keycode.F10)
        led.value = True
        time.sleep(0.08)
        led.value = False

    if btn6.value:
        keyboard.send(Keycode.SHIFT, Keycode.F8)
        led.value = True
        time.sleep(0.08)
        led.value = False

    if btn7.value:
        keyboard.send(KKeycode.SHIFT, Keycode.F12)
        led.value = True
        time.sleep(0.08)
        led.value = False

    if btn8.value:
        keyboard.send(Keycode.SHIFT, Keycode.F11)
        led.value = True
        time.sleep(0.08)
        led.value = False

    if btn9.value:
        keyboard.send(Keycode.SHIFT, Keycode.F3)
        led.value = True
        time.sleep(0.08)
        led.value = False

    if btn10.value:
        keyboard.send(Keycode.SHIFT, Keycode.F2)
        led.value = True
        time.sleep(0.08)
        led.value = False

    if btn11.value:
        keyboard.send(Keycode.SHIFT, Keycode.F4)
        led.value = True
        time.sleep(0.08)
        led.value = False

    if btn12.value:
        keyboard.send(Keycode.SHIFT, Keycode.F5)
        led.value = True
        time.sleep(0.08)
        led.value = False
    time.sleep(0.05)