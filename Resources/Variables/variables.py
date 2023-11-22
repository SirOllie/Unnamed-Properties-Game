#variables

import pygame as py
from Resources.Colours.colours import *

########## SCREEN ##########
screen_size = (1280, 720)
screen = py.display.set_mode(screen_size)
bg = py.image.load("Resources/Images/Background1.png")
bg = py.transform.scale(bg, screen_size)
########## CASH ##########
cash_val = 0
cash_text_position = (20, 20)
cash_text_colour = white