import pygame
import random
pygame.init()

from settingsFile import settings
from settingsFile import clock
from settingsFile import screen
from settingsFile import isRunning
from objects.star import starObject
from updateService import updateScreen

while settings.isRunning:
    updateScreen()
    starObject.update()
    
    pygame.display.flip()
    
    clock.tick(settings.frameRate)
pygame.quit()