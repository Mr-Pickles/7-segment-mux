# 7-segment-mux
Multiplexing 2 7-segment LEDs using a Raspberry Pico and Micropython.

The 2 digit seven segment display I used for this was an TG320of I had lying around.  Details of this can be found at http://www.voti.nl/docs/disp-7.pdf for the pin outs.

The schematic shows a 7-segment LED that has a decimal point - my TG302of does not so that is not connected up on the schematic.

The python application defines the led characters for the hexidecimal digits 0,1,2,3,4,5,6,7,8,9,A,b,C,d,E,F.  It uses a variable called "value" that is splits into a high and low nibble value to display on each of the two leds accordingly.  A timer interrupt is set up which switches between the two leds.  So, although both leds are wired together and, technically, display the same value, that value changes and one led to turned off whilst the other is turned on.

All this happens at 100 Hz so persistence of vision makes it look like a normal display - only 9 pins are used to drive the 2 leds.
