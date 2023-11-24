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
    pass