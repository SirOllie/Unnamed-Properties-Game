#variables

import pygame as py
from Resources.Colours.colours import *

########## SCREEN ##########
screen_size = (1280, 720)
screen = py.display.set_mode(screen_size)
bg = py.image.load("Resources/Images/Background1.png")
bg = py.transform.scale(bg, screen_size)
screen_width = screen.get_width()
########## TIMING ##########
clock = py.time.Clock()
fps = 0
fps_limit = 144
day_counter = 0
day_counter_text = '00:00'
time_is_paused = False
update_ticker = fps_limit
########## CASH ##########
cash_val = 0
cash_text_position = (20, 20)
cash_text_colour = white

