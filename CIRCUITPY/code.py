# ---------------- #
# import libraries #
# ---------------- #
from pmk.platform.keybow2040 import Keybow2040 as Hardware
from pmk import PMK

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
# -------------------- #
# end import libraries #
# -------------------- #




# ------------------------------------ #
# define global variables and settings #
# ------------------------------------ #
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

pmk = PMK(Hardware())
pmk.rotate(90)

pmk.led_sleep_enabled = True
pmk.led_sleep_time = 10

windowcolor = (255,255,255)

# ---------------------------------------- #
# end define global variables and settings #
# ---------------------------------------- #




# -------------------------------- #
# operational macros and functions #
# -------------------------------- #
# - #
# - #
# - #
# - #
# ------------------------------------ #
# end operational macros and functions #
# ------------------------------------ #




# ------------------------ #
# window management macros #
# ------------------------ #
wleft = pmk.keys[0]
wleft.set_led(*windowcolor)

@pmk.on_press(wleft)
def press_handler(key):
  keyboard.send(Keycode.OPTION, Keycode.ONE)

# -- #

wtop = pmk.keys[1]
wtop.set_led(*windowcolor)

@pmk.on_press(wtop)
def press_handler(key):
  keyboard.send(Keycode.OPTION, Keycode.TWO)

# -- #

wright = pmk.keys[2]
wright.set_led(*windowcolor)

@pmk.on_press(wright)
def press_handler(key):
  keyboard.send(Keycode.OPTION, Keycode.THREE)

# -- #

wbottom = pmk.keys[3]
wbottom.set_led(*windowcolor)

@pmk.on_press(wbottom)
def press_handler(key):
  keyboard.send(Keycode.OPTION, Keycode.FOUR)

# -- #

nextdisplay = pmk.keys[4]
nextdisplay.set_led(*windowcolor)

@pmk.on_press(nextdisplay)
def press_handler(key):
  keyboard.send(Keycode.OPTION, Keycode.SEVEN)

# -- #

almostmax = pmk.keys[5]
almostmax.set_led(*windowcolor)

@pmk.on_press(almostmax)
def press_handler(key):
  keyboard.send(Keycode.OPTION, Keycode.EIGHT)

# -- #
  
wmax = pmk.keys[6]
wmax.set_led(*windowcolor)

@pmk.on_press(wmax)
def press_handler(key):
  keyboard.send(Keycode.OPTION, Keycode.FIVE)

# -- #
  
wfull = pmk.keys[7]
wfull.set_led(*windowcolor)

@pmk.on_press(wfull)
def press_handler(key):
  keyboard.send(Keycode.OPTION, Keycode.SIX)
# ---------------------------- #
# end window management macros #
# ---------------------------- #


# ------------------ #
# application macros #
# ------------------ #

# -- arc -- # 
arcapp = pmk.keys[8]
arccolor = (255,255,0)
arcapp.set_led(*arccolor)
@pmk.on_press(arcapp)
def press_handler(key):
  keyboard.send(Keycode.CONTROL, Keycode.ONE)

# -- slack -- # 
slackapp = pmk.keys[9]
slackcolor = (0,255,0)
slackapp.set_led(*slackcolor)
@pmk.on_press(slackapp)
def press_handler(key):
  keyboard.send(Keycode.CONTROL, Keycode.TWO)

# -- zoom -- # 
zoomapp = pmk.keys[10]
zoomcolor = (0,0,255)
zoomapp.set_led(*zoomcolor)
@pmk.on_press(zoomapp)
def press_handler(key):
  keyboard.send(Keycode.CONTROL, Keycode.THREE)

# -- obsidian -- # 
obsidianapp = pmk.keys[11]
obsidiancolor = (255,0,255)
obsidianapp.set_led(*obsidiancolor)
@pmk.on_press(obsidianapp)
def press_handler(key):
  keyboard.send(Keycode.CONTROL, Keycode.FOUR)

# ---------------------- #
# end application macros #
# ---------------------- #



# -------------------- #
# miscellaneous macros #
# -------------------- #
# -- pomodoro -- # 
pstart = (255, 0, 0)
pomodoro_start = pmk.keys[13]
pomodoro_start.set_led(*pstart)
@pmk.on_press(pomodoro_start)
def press_handler(key):
  keyboard.send(Keycode.OPTION, Keycode.P)


# -- harvest -- # 
harvest = (255, 69, 0)
harvest_start = pmk.keys[12]
harvest_start.set_led(*harvest)
@pmk.on_press(harvest_start)
def press_handler(key):
  keyboard.send(Keycode.OPTION, Keycode.T)


# -- confetti -- # 
confetti = (0, 255, 0)
confettikey = pmk.keys[15]
confettikey.set_led(*confetti)
@pmk.on_press(confettikey)
def press_handler(key):
  keyboard.send(Keycode.OPTION, Keycode.BACKSLASH)
# ------------------------ #
# end miscellaneous macros #
# ------------------------ #

while True:
  pmk.update()

  if pmk.keys[14].held:
    pmk.keys[14].set_led(*windowcolor)
    pmk.led_sleep_enabled = not pmk.led_sleep_enabled