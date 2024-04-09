import os
import sys  # Allows us to use sys.path.append below
import time # Allows us to insert delays in our script

sys.path.append('/home/rkumar/sphero-sdk-raspberrypi-python') 


from sphero_sdk import SpheroRvrObserver
rvr = SpheroRvrObserver()

#Functions:

def battery_percentage_handler(battery_percentage):
            print('Battery:', battery_percentage)

def left_turn():
    rvr.drive_control.turn_left_degrees(
            heading=0,  # Valid heading values are 0-359
            amount=90
        )