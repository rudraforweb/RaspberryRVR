import os
import sys  # Allows us to use sys.path.append below
import time # Allows us to insert delays in our script

sys.path.append('/home/rkumar/sphero-sdk-raspberrypi-python') 

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import Colors

from functions import *

rvr = SpheroRvrObserver()


#Start RVR:
rvr.wake()
time.sleep(2)

def main():
    """ This program has RVR drive with how to drive RVR using the drive control helper.
    """

    try:
        rvr.wake()

        # Give RVR time to wake up
        time.sleep(2)
        
        rvr.get_battery_percentage(handler=battery_percentage_handler)


        rvr.drive_control.reset_heading()

        rvr.drive_control.drive_forward_seconds(
            speed=64,
            heading=0,  # Valid heading values are 0-359
            time_to_drive=1
        )

        # Delay to allow RVR to drive
        time.sleep(1)

        rvr.drive_control.drive_backward_seconds(
            speed=64,
            heading=0,  # Valid heading values are 0-359
            time_to_drive=1
        )

        # Delay to allow RVR to drive
        time.sleep(1)

        left_turn()

        # Delay to allow RVR to drive
        time.sleep(1)

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        rvr.close()
        time.sleep(1)
        exit()


if __name__ == '__main__':
    main()