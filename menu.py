# -*- coding: utf-8 -*-
"""
Created on Sat May 14 21:45:20 2016

@author: Riccardo Rossi
"""

import pygame

text_menu =  ['Simple simulation of an aquarium with fish and predators',\
            ' ',\
            '- The fish (black squares) move on a straight line;',\
            '- The dolphins (blue rectangles) chase the mass of fish;',\
            '- The sharks (red rectangles) chase the single closest fish.',\
            ' ',\
            'See which species outlives the other']
            
def launch(screen):
    font_menu = pygame.font.Font(None, 24)
    
    menu_running = True
    while menu_running: 
        for event in pygame.event.get(): 
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN: 
                menu_running = False  
        screen.fill(BLACK)        
        
        for i in range(0, len(text_menu)):
            menu = font_menu.render(text_menu[i], 1, WHITE)
            text_rect = menu.get_rect()
            
            text_rect.top = screen.get_rect().top + 15 + i*20
            text_rect.left = screen.get_rect().left + 15
            screen.blit(menu, text_rect)
        
        menu = font_menu.render('PRESS ANY KEY TO START', 1, YELLOW)
        text_rect = menu.get_rect()
        text_rect.bottom = screen.get_rect().bottom - 200
        text_rect.centerx = screen.get_rect().centerx
        screen.blit(menu, text_rect)

        pygame.display.flip()
    
    del menu, font_menu
    return(0)
            
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)
GREEN = (  0, 100,   0)
YELLOW =(255, 250, 205)