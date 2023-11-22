#Base
#
#VERSION
#Pre-Alpha0.0_1
#

import pygame as py
from Resources.Fonts.fonts import *


text = cash_font.render(str(23), True, (0, 0, 0))
#initialising pygame
py.init()

#-----------

screen = py.display.set_mode((800, 600))
screen.fill((255, 255, 255))
screen.blit(text, (20, 20))
py.display.flip()

running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    py.display.flip()

py.quit()