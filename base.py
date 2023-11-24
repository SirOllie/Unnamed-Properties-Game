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

cash_text = cash_font.render("Cash: "+str(cash_val), True, cash_text_colour)
fps_counter = fps_font.render("fps: "+str(fps), True, white)
time_text = cash_font.render((day_counter_text), True, white)
py.time.set_timer(py.USEREVENT, 1000)
screen.blit(bg, (0, 0))
screen.blit(cash_text, cash_text_position)
screen.blit(fps_counter, (1000, 20))
screen.blit(time_text, (1000, 680))
py.display.flip()

running = True
while running:
    for event in py.event.get():
        if event.type == py.USEREVENT: 
            do_counter()
            
        if event.type == py.QUIT:
            running = False
        elif event.type == py.KEYDOWN:
           
            if event.key == py.K_SPACE:
                time_is_paused = not time_is_paused

            if event.key == py.K_LEFT:
                pass

            
    keys = py.key.get_pressed()  # Checking pressed keys
    if keys[py.K_LEFT]:
        if update_ticker == 144:
            update_ticker -= (10)
            cash_val = cash_val_change(cash_val, -1)
            cash_text = cash_font.render("Cash: " + str(cash_val), True, cash_text_colour)
            screen.blit(bg, (0, 0))
            screen.blit(cash_text, cash_text_position)
            py.display.flip()
        else: pass
    if keys[py.K_RIGHT]:
        if update_ticker == 144:
            update_ticker -= (10)
            cash_val = cash_val_change(cash_val, 1)
            cash_text = cash_font.render("Cash: " + str(cash_val), True, cash_text_colour)
            screen.blit(bg, (0, 0))
            screen.blit(cash_text, cash_text_position)
            py.display.flip()
        else: pass
    #if keys[py.K_SPACE]:
        
        

    clock.tick(144)
    fps_counter = fps_font.render("fps: "+str(round(float(get_fps_info()))), True, white)
    fps_counter_pos = (fps_counter.get_rect(topleft=(20, 20))).width
    time_text = cash_font.render((day_counter_text), True, white)
    screen.blit(bg, (0, 0))
    screen.blit(cash_text, cash_text_position)
    screen.blit(fps_counter, (((screen.get_width())-fps_counter_pos-20), 20))
    screen.blit(time_text, (1000, 680))
    if update_ticker < fps_limit:
        update_ticker += 1
    py.display.flip()

py.quit()