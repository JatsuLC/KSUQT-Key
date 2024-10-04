# K.S.U.Q.T. (KeyStroke Usb QT) Key
An open-source, low cost, Rubber Ducky mimic utilizing the Adafruit Trinkey QT2040.


# KSUQT Device Commands

Note: All command values that continue with "..." means that more than 1 value can be input. if no "..." is present, then only 1 value can be input.
- Use '#' to insert comments in a script.
  
If using a display, this command sets the screen to display the title string. 
- TITLE string 

# Keyboard Strokes
Keycode Values: https://docs.circuitpython.org/projects/hid/en/latest/api.html#adafruit_hid.keycode.Keycode
-------------------------------------------------
Input a string to the target device
- STRING string

Pause script for a certain amount of time in seconds
- SLEEP x.xx

Press the Enter Key
- ENTER

Open the GUI or press the windows Key (Same Function)
- GUI
- WINDOWS

Press keyboard key(s) - presses it 1 by 1 from left to right
- PRESS KEYCODE value ...

Same function as PRESS, but RELEASES keys instead
- RELEASE KEYCODE value ...

Releases all keys
- RELEASEALL

Presses and Releases all keys, 1 by 1, left to right
- SEND KEYCODE value ...

# Mouse Strokes
Mouse Keycode Values: https://docs.circuitpython.org/projects/hid/en/latest/api.html#adafruit_hid.mouse.Mouse
-------------------------------------------------

Press Mouse keys, same function as PRESS but for Mouse
- MOUSE_PRESS KEYCODE value ...

Same function as MOUSE_PRESS but releases
- MOUSE_RELEASE KEYCODE value ...

Releases all MOuse Keys
- MOUSE_RELEASEALL

Same function as SEND, but for Mouse
- CLICK KEYCODE value ...

Move Mouse to X Coordinate
- MOUSE_X value

Move Mouse to Y Coordinate
- MOUSE_Y value

Scroll Mouse wheel, negative values towards user, positive values away from user
- MOUSE_WHEEL value

Same as MOUSE_X, MOUSE_Y, and MOUSE_WHEEL, but all in one
- MOVE x_value y_value wheel_value


# Consumer Controls
Consumer Control Keycode Values: https://docs.circuitpython.org/projects/hid/en/latest/api.html#adafruit_hid.consumer_control.ConsumerControl
-------------------------------------------------

Only one keycode can be sent at a time. Same functions as previous press, release, and send commands, but for consumer controls.
- CC_PRESS value
- CC_RELEASE value
- CC_SEND value
