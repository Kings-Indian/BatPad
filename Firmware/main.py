# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.RGB import RGB, AnimationModes

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Add RGB lighting
rgb = RGB(
    pixel_pin=board.D5,  # Using D5 for RGB
    num_pixels=2,
    val_default=50,
    animation_mode=AnimationModes.BREATHING
)
keyboard.extensions.append(rgb)

# Define your pins here! (4 keys)
PINS = [board.D0, board.D1, board.D2, board.D3]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Configure rotary encoders (2 encoders)
encoder_handler = EncoderHandler()
encoder_handler.pins = (
    (board.D6, board.D7, None),  # Encoder 1
    (board.D8, board.D9, None),  # Encoder 2
)
keyboard.modules.append(encoder_handler)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [
        KC.MACRO(Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL)),  # Copy
        KC.MACRO(Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL)),  # Paste
        KC.MACRO(Press(KC.LCTRL), Tap(KC.X), Release(KC.LCTRL)),  # Cut
        KC.MACRO(Press(KC.LCTRL), Tap(KC.Z), Release(KC.LCTRL)),  # Undo
    ]
]

# Configure encoder actions
encoder_handler.map = [
    [(KC.VOLD, KC.VOLU)],  # Encoder 1: Volume down/up
    [(KC.MPRV, KC.MNXT)],  # Encoder 2: Previous/next track
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()