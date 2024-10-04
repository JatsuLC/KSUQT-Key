import time, os, usb_hid, board, digitalio

from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.mouse import Mouse
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

import neopixel as np

#-----------------FUNTIONS------------------#

###Map Keyboard Keys###
def execKBDCMD(keycode, cmd):
    keycode_map = {
        "A": Keycode.A, "B": Keycode.B, "C": Keycode.C, "D": Keycode.D,
        "E": Keycode.E, "F": Keycode.F, "G": Keycode.G, "H": Keycode.H,
        "I": Keycode.I, "J": Keycode.J, "K": Keycode.K, "L": Keycode.L,
        "M": Keycode.M, "N": Keycode.N, "O": Keycode.O, "P": Keycode.P,
        "Q": Keycode.Q, "R": Keycode.R, "S": Keycode.S, "T": Keycode.T,
        "U": Keycode.U, "V": Keycode.V, "W": Keycode.W, "X": Keycode.X,
        "Y": Keycode.Y, "Z": Keycode.Z,
        "ONE": Keycode.ONE, "TWO": Keycode.TWO, "THREE": Keycode.THREE,
        "FOUR": Keycode.FOUR, "FIVE": Keycode.FIVE, "SIX": Keycode.SIX,
        "SEVEN": Keycode.SEVEN, "EIGHT": Keycode.EIGHT, "NINE": Keycode.NINE,
        "ZERO": Keycode.ZERO,
        "ENTER": Keycode.ENTER, "RETURN": Keycode.ENTER,
        "ESCAPE": Keycode.ESCAPE, "BACKSPACE": Keycode.BACKSPACE,
        "TAB": Keycode.TAB, "SPACEBAR": Keycode.SPACEBAR, "SPACE": Keycode.SPACEBAR,
        "MINUS": Keycode.MINUS, "EQUALS": Keycode.EQUALS,
        "LEFT_BRACKET": Keycode.LEFT_BRACKET, "RIGHT_BRACKET": Keycode.RIGHT_BRACKET,
        "BACKSLASH": Keycode.BACKSLASH, "POUND": Keycode.POUND,
        "SEMICOLON": Keycode.SEMICOLON, "QUOTE": Keycode.QUOTE,
        "GRAVE_ACCENT": Keycode.GRAVE_ACCENT, "COMMA": Keycode.COMMA,
        "PERIOD": Keycode.PERIOD, "FORWARD_SLASH": Keycode.FORWARD_SLASH,
        "CAPS_LOCK": Keycode.CAPS_LOCK,
        "F1": Keycode.F1, "F2": Keycode.F2, "F3": Keycode.F3, "F4": Keycode.F4,
        "F5": Keycode.F5, "F6": Keycode.F6, "F7": Keycode.F7, "F8": Keycode.F8,
        "F9": Keycode.F9, "F10": Keycode.F10, "F11": Keycode.F11, "F12": Keycode.F12,
        "PRINT_SCREEN": Keycode.PRINT_SCREEN, "SCROLL_LOCK": Keycode.SCROLL_LOCK,
        "PAUSE": Keycode.PAUSE, "INSERT": Keycode.INSERT, "HOME": Keycode.HOME,
        "PAGE_UP": Keycode.PAGE_UP, "DELETE": Keycode.DELETE, "END": Keycode.END,
        "PAGE_DOWN": Keycode.PAGE_DOWN, "RIGHT_ARROW": Keycode.RIGHT_ARROW,
        "LEFT_ARROW": Keycode.LEFT_ARROW, "DOWN_ARROW": Keycode.DOWN_ARROW,
        "UP_ARROW": Keycode.UP_ARROW,
        "KEYPAD_NUMLOCK": Keycode.KEYPAD_NUMLOCK,
        "KEYPAD_FORWARD_SLASH": Keycode.KEYPAD_FORWARD_SLASH,
        "KEYPAD_ASTERISK": Keycode.KEYPAD_ASTERISK,
        "KEYPAD_MINUS": Keycode.KEYPAD_MINUS, "KEYPAD_PLUS": Keycode.KEYPAD_PLUS,
        "KEYPAD_ENTER": Keycode.KEYPAD_ENTER,
        "KEYPAD_ONE": Keycode.KEYPAD_ONE, "KEYPAD_TWO": Keycode.KEYPAD_TWO,
        "KEYPAD_THREE": Keycode.KEYPAD_THREE, "KEYPAD_FOUR": Keycode.KEYPAD_FOUR,
        "KEYPAD_FIVE": Keycode.KEYPAD_FIVE, "KEYPAD_SIX": Keycode.KEYPAD_SIX,
        "KEYPAD_SEVEN": Keycode.KEYPAD_SEVEN, "KEYPAD_EIGHT": Keycode.KEYPAD_EIGHT,
        "KEYPAD_NINE": Keycode.KEYPAD_NINE, "KEYPAD_ZERO": Keycode.KEYPAD_ZERO,
        "KEYPAD_PERIOD": Keycode.KEYPAD_PERIOD,
        "KEYPAD_BACKSLASH": Keycode.KEYPAD_BACKSLASH,
        "APPLICATION": Keycode.APPLICATION, "POWER": Keycode.POWER,
        "KEYPAD_EQUALS": Keycode.KEYPAD_EQUALS,
        "F13": Keycode.F13, "F14": Keycode.F14, "F15": Keycode.F15,
        "F16": Keycode.F16, "F17": Keycode.F17, "F18": Keycode.F18,
        "F19": Keycode.F19, "F20": Keycode.F20, "F21": Keycode.F21,
        "F22": Keycode.F22, "F23": Keycode.F23, "F24": Keycode.F24,
        "LEFT_CONTROL": Keycode.LEFT_CONTROL, "CONTROL": Keycode.LEFT_CONTROL,
        "LEFT_SHIFT": Keycode.LEFT_SHIFT, "SHIFT": Keycode.LEFT_SHIFT,
        "LEFT_ALT": Keycode.LEFT_ALT, "ALT": Keycode.LEFT_ALT, "OPTION": Keycode.LEFT_ALT,
        "LEFT_GUI": Keycode.LEFT_GUI, "GUI": Keycode.LEFT_GUI,
        "WINDOWS": Keycode.LEFT_GUI, "COMMAND": Keycode.LEFT_GUI,
        "RIGHT_CONTROL": Keycode.RIGHT_CONTROL,
        "RIGHT_SHIFT": Keycode.RIGHT_SHIFT,
        "RIGHT_ALT": Keycode.RIGHT_ALT,
        "RIGHT_GUI": Keycode.RIGHT_GUI,
    }
    
    if keycode in keycode_map:
        if cmd == "PRESS":
            kbd.press(keycode_map[keycode])
        elif cmd == "RELEASE":
            kbd.release(keycode_map[keycode])

###Map Mouse Keys###
def execMouseCMD(keycode, cmd):
    mouse_button_map = {
        "BACK_BUTTON": Mouse.BACK_BUTTON,
        "FORWARD_BUTTON": Mouse.FORWARD_BUTTON,
        "LEFT_BUTTON": Mouse.LEFT_BUTTON,
        "MIDDLE_BUTTON": Mouse.MIDDLE_BUTTON,
        "RIGHT_BUTTON": Mouse.RIGHT_BUTTON
    }
    
    if keycode in mouse_button_map:
        if cmd == "PRESS":
            mouse.press(mouse_button_map[keycode])
        elif cmd == "RELEASE":
            mouse.release(mouse_button_map[keycode])

###Map ConsumerControl Keys###
def execCCCMD(keycode, cmd):
    cc_code_map = {
        "BRIGHTNESS_DECREMENT": ConsumerControlCode.BRIGHTNESS_DECREMENT,
        "BRIGHTNESS_INCREMENT": ConsumerControlCode.BRIGHTNESS_INCREMENT,
        "EJECT": ConsumerControlCode.EJECT,
        "FAST_FORWARD": ConsumerControlCode.FAST_FORWARD,
        "MUTE": ConsumerControlCode.MUTE,
        "PLAY_PAUSE": ConsumerControlCode.PLAY_PAUSE,
        "RECORD": ConsumerControlCode.RECORD,
        "REWIND": ConsumerControlCode.REWIND,
        "SCAN_NEXT_TRACK": ConsumerControlCode.SCAN_NEXT_TRACK,
        "SCAN_PREVIOUS_TRACK": ConsumerControlCode.SCAN_PREVIOUS_TRACK,
        "STOP": ConsumerControlCode.STOP,
        "VOLUME_DECREMENT": ConsumerControlCode.VOLUME_DECREMENT,
        "VOLUME_INCREMENT": ConsumerControlCode.VOLUME_INCREMENT
    }
    
    if keycode in cc_code_map:
        if cmd == "PRESS":
            consumer_control.press(cc_code_map[keycode])
        elif cmd == "RELEASE":
            consumer_control.release()
            
'''
readScript() reads the file titled script.txt in the scripts folder on the QT. It returns a list of iterable commands and input from the txt file in a list like the following:
[['CMD1', 'cmdinput'], ['CMD', 'cmdinput'], ...]

'''
def readScript(fileName):
    with open('scripts/' + fileName, 'r') as script:
        scriptLines = []
        for line in script:
            strippedLine = line.strip().split()
            if not strippedLine or strippedLine[0].startswith('#'):
                continue
            
            command = strippedLine[0].upper()
            if command in ["STRING", "TITLE"]:
                scriptLines.append([command, " ".join(strippedLine[1:])])
            else:
                scriptLines.append([command] + strippedLine[1:])

    return scriptLines

def execCode(scriptList):
    def sleep_action(args):
        time.sleep(float(args[0]))

    def string_action(args):
        kbdLayout.write(args[0])

    def enter_action(args):
        kbd.press(Keycode.ENTER)
        kbd.release(Keycode.ENTER)

    def gui_action(args):
        kbd.press(Keycode.LEFT_GUI)
        kbd.release(Keycode.LEFT_GUI)

    def press_action(args):
        for value in args:
            execKBDCMD(value, "PRESS")

    def release_action(args):
        for value in args:
            execKBDCMD(value, "RELEASE")

    def send_action(args):
        for value in args:
            execKBDCMD(value, "PRESS")
        for value in args:
            execKBDCMD(value, "RELEASE")

    def mouse_press_action(args):
        for value in args:
            execMouseCMD(value, "PRESS")

    def mouse_release_action(args):
        for value in args:
            execMouseCMD(value, "RELEASE")

    def click_action(args):
        for value in args:
            execMouseCMD(value, "PRESS")
        for value in args:
            execMouseCMD(value, "RELEASE")

    def move_action(args):
        mouse.move(x=int(args[0]), y=int(args[1]), wheel=int(args[2]))

    def cc_press_action(args):
        execCCCMD(args[0], "PRESS")

    def cc_release_action(args):
        execCCCMD(args[0], "RELEASE")

    def cc_send_action(args):
        execCCCMD(args[0], "PRESS")
        execCCCMD(args[0], "RELEASE")

    command_map = {
        "SLEEP": sleep_action,
        "STRING": string_action,
        "ENTER": enter_action,
        "GUI": gui_action,
        "WINDOWS": gui_action,
        "PRESS": press_action,
        "RELEASE": release_action,
        "RELEASEALL": lambda args: kbd.release_all(),
        "SEND": send_action,
        "MOUSE_PRESS": mouse_press_action,
        "MOUSE_RELEASE": mouse_release_action,
        "MOUSE_RELEASEALL": lambda args: mouse.release_all(),
        "CLICK": click_action,
        "MOUSE_X": lambda args: mouse.move(x=int(args[0])),
        "MOUSE_Y": lambda args: mouse.move(y=int(args[0])),
        "MOUSE_WHEEL": lambda args: mouse.move(wheel=int(args[0])),
        "MOVE": move_action,
        "CC_PRESS": cc_press_action,
        "CC_RELEASE": cc_release_action,
        "CC_SEND": cc_send_action,
    }

    for line in scriptList:
        command = line[0]
        args = line[1:]
        if command in command_map:
            command_map[command](args)
#---------------FUNTIONS END----------------#
        
#LED assignment
pixels = np.NeoPixel(board.NEOPIXEL, 1)
pixels.brightness=0.05
pixels[0] = ((0, 0, 255))

#Button Reassignment - may need modification if not using Adafruit qt stemma QT key
button = digitalio.DigitalInOut(board.BUTTON)
button.switch_to_input(pull=digitalio.Pull.UP)

###HID Devices Creation###
kbd = Keyboard(usb_hid.devices)
kbdLayout = KeyboardLayoutUS(kbd)
mouse = Mouse(usb_hid.devices)
consumer_control = ConsumerControl(usb_hid.devices)

###Script file assignment###
scriptCommands = readScript("script.txt") # Change string to script txt file to run!
#print(scriptCommands)
###Title assignment OLED SCREEN###
#print(scriptCommands)
for command in scriptCommands:
    if "TITLE" in command:
        #print("True")
        scriptName = command[1]
        break
    else:
        scriptName = "Placeholder"
###End Title Assignment###

###MAIN LOOP FUNCTIONS###
def set_pixel_color(status):
    pixels[0] = (255, 0, 0) if status == 'running' else (0, 255, 0)

###MAIN LOOP###
while True:
    if not button.value:
        set_pixel_color('running')
        execCode(scriptCommands)
    else:
        set_pixel_color('ready')
