import sys  # Allows us to use sys.path.append below
import time # Allows us to insert delays in our script

sys.path.append('/home/rkumar/  sphero-sdk-raspberrypi-python') 

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import Colors

import functions

rvr = SpheroRvrObserver()

#Start RVR:
rvr.wake()
time.sleep(2)

def main():
    # Make sure RVR is awake and ready to receive commands
    rvr.wake()
    
    # Wait for RVR to wake up
    time.sleep(2)
    
    # Set all of RVR's LEDs to a named color
    rvr.led_control.set_all_leds_color(color=Colors.yellow)
    
    # Wait a second so we get to see the color change
    time.sleep(1)
    
    # Now try using RGB (Red Green Blue) values.  
    # This allows us to pick any color in the RGB colorspace.
    rvr.led_control.set_all_leds_rgb(red=255, green=0, blue=0)

# This tells the interpreter to run our main() function if it is running this script 
# directly (and not importing it as a module from elsewhere)
if __name__ == '__main__':
    try:
        # Stuff to try doing (which might generate an exception)
        main()
    except KeyboardInterrupt:
        # What to do if there's a keyboard interrupt (ctrl+c) exception
        # In this case, we're just going to print a message
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        # What to do before we exit the block
        rvr.close()