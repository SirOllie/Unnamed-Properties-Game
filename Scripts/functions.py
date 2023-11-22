#functions

import pygame as py

py.init()

def cash_val_change(value, amount):
    if (value+amount <= 0):
        return 0
    else:
        return (value+amount)
