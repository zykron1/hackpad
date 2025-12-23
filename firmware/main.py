import board
import busio
import displayio
from adafruit_displayio_ssd1306 import SSD1306
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [
    board.GP26,
    board.GP27,
    board.GP28,
    board.GP3,
    board.GP4,
    board.GP2,
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [] # Configure as you want

displayio.release_displays()
i2c = busio.I2C(board.GP7, board.GP6)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C) # depends on the model sometimes
display = SSD1306(display_bus, width=128, height=32)

if __name__ == "__main__":
    keyboard.go()

