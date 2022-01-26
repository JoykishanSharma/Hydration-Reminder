import ctypes
import time
from time import sleep


# gets called every hour recursively
def recursiveTimer():
    # sleep the process for 1 hour
    sleep(3600)

    # show Dialog box
    MessageBox(None, "It's Been an Hour. Take a Break and get Hydrated!", 'Hourly Reminder', 0)

    # continue the infinite recursion
    recursiveTimer()


# windows dialog box reference
MessageBox = ctypes.windll.user32.MessageBoxW

# initial dialog box 
MessageBox(None, "Get Hydrated! I'll remind you after 1 Hour.", 'Hourly Reminder', 0)

# start recursive Timer
recursiveTimer()
