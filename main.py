import sys  # Allows us to use sys.path.append below
import time # Allows us to insert delays in our script

sys.path.append('/home/pi/sphero-sdk-raspberrypi-python') 

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import Colors

import functions

rvr = SpheroRvrObserver()

#Start RVR:
rvr.wake()
time.sleep(2)

rvr.led_control.set_all_leds_color(color=Colors.yellow)

# Wait a second so we get to see the color change
time.sleep(1)

# Now try using RGB (Red Green Blue) values.  
# This allows us to pick any color in the RGB colorspace.
rvr.led_control.set_all_leds_rgb(red=255, green=0, blue=0)

# Call this at the end of your program to close the serial port
rvr.close() 
