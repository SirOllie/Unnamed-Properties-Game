#Base
#
#VERSION
#Pre-Alpha0.0_1
#

import pygame as py
from Resources.Fonts.fonts import *
from Scripts.functions import *
from Resources.Variables.variables import *
from Resources.Colours.colours import *

#initialising pygame
py.init()

#-----------

#-----------
cash_text = cash_font.render("Cash: "+str(cash_val), True, cash_text_colour)
screen.blit(bg, (0, 0))
screen.blit(cash_text, cash_text_position)
py.display.flip()

running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.KEYDOWN:
            # Check if the right arrow key is pressed
            if event.key == py.K_RIGHT:
                cash_val = cash_val_change(cash_val, 1)
                cash_text = cash_font.render("Cash: " + str(cash_val), True, cash_text_colour)
                screen.blit(bg, (0, 0))
                screen.blit(cash_text, cash_text_position)
                py.display.flip()

            if event.key == py.K_LEFT:
                cash_val = cash_val_change(cash_val, -1)
                cash_text = cash_font.render("Cash: " + str(cash_val), True, cash_text_colour)
                screen.blit(bg, (0, 0))
                screen.blit(cash_text, cash_text_position)
                py.display.flip()
                
    py.display.flip()

py.quit()