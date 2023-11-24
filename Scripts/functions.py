#functions

import pygame as py
from Resources.Variables.variables import *
from Resources.Fonts.fonts import *

py.init()

def cash_val_change(value, amount):
    if (value+amount <= 0):
        return 0
    else:
        return (value+amount)

def get_fps_info():
    return str(clock.get_fps())

def do_counter():
    if(time_is_paused == False):
        day_counter_text = "0" + str(day_counter) + ":00"
        day_counter_text = str(day_counter) + ":00"
        if day_counter <= 22:
            if day_counter <= 9:
                return (day_counter + 1)   
    else:
        pass