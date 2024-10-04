import storage
import digitalio, board

#Button Reassignment
button = digitalio.DigitalInOut(board.BUTTON)
button.switch_to_input(pull=digitalio.Pull.UP)

if not button.value:
    storage.enable_usb_drive()

else:
    storage.disable_usb_drive()