from machine import Pin, Timer
import time

# Character definitions.

# Segment to GPIO mappings: A,B,C,D,E,F,G -> 0,1,2,3,4,5,6

#    AAA
#   F   B
#   F   B
#    GGG
#   E   C
#   E   C
#    DDD

decimal = [
    [1,1,1,1,1,1,0], # 0
    [0,1,1,0,0,0,0], # 1
    [1,1,0,1,1,0,1], # 2
    [1,1,1,1,0,0,1], # 3
    [0,1,1,0,0,1,1], # 4
    [1,0,1,1,0,1,1], # 5
    [1,0,1,1,1,1,1], # 6
    [1,1,1,0,0,0,0], # 7
    [1,1,1,1,1,1,1], # 8
    [1,1,1,1,0,1,1]  # 9
    ]

hexadecimal = decimal + [
    [1,1,1,0,1,1,1], # A
    [0,0,1,1,1,1,1], # b
    [1,0,0,1,1,1,0], # C
    [0,1,1,1,1,0,1], # d
    [1,0,0,1,1,1,1], # E
    [1,0,0,0,1,1,1]  # F
    ]

# Set the LED cathodes to GPIO pins.
LEDS = [Pin(8, Pin.OUT), Pin(7, Pin.OUT)]

# Turn both LED displays off.
LEDS[0].value(1)
LEDS[1].value(1)

# Define the data we want to display (0x00 to 0xFF).
value = 0

# The current display.
curr_disp = 0

# Configure the GPIO pins for the segments of the displays.
pins = []
for pin in range(7):
    pins.append(Pin(pin, Pin.OUT))

# Create a hardware timer.
timer = Timer()

# Function that handles multiplexing of the 2 displays.
def tick(timer):
    global value, hexadecimal, curr_disp
    
    # Get the high & low nibble values.
    lower = value % 16
    upper = value // 16
    
    # Determine which LED is currently displaying.
    if curr_disp == 0:                     # The lower nibble is being shown.
        LEDS[0].value(1)                   # Turn it off.
        show(upper, hexadecimal)           # Load the upper nibble value.
        LEDS[1].value(0)                   # Turn it on.
        curr_disp = 1                      # Update accordingly
    else:                                  # Then it must be the upper nibble being shown.
        LEDS[1].value(1)                   # Turn it off.
        show(lower, hexadecimal)           # Load the lower nibble value.
        LEDS[0].value(0)                   # Turn it on.
        curr_disp = 0                      # Update accordingly


# Configure a hardware timer to process the multiplexing.
timer.init(freq=100, mode=Timer.PERIODIC, callback=tick)


def show(n, charset):
    for pin, segment in enumerate(charset[n]):
        pins[pin].value(segment)
        
def test():
    while True:
        for n in range(16):
            display(n, hexadecimal)
            time.sleep(0.5)
    
    