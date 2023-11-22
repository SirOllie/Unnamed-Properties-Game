#variables

import pygame as py
from Resources.Colours.colours import *

########## SCREEN ##########
screen = py.display.set_mode((768, 432))
bg = py.image.load("Resources/Images/Background1.png")
bg = py.transform.scale(bg, (768, 432))
########## CASH ##########
cash_val = 0
cash_text_position = (20, 20)
cash_text_colour = white