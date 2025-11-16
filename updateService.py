import pygame
from settingsFile import screen
from settingsFile import settings
from settingsFile import clock
from settingsFile import isRunning

def updateScreen():
    screen.fill(settings.backgroundColor)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           settings.isRunning = False