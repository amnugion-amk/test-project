import pygame
import random
pygame.init()

from settingsFile import settings
from settingsFile import clock
from settingsFile import screen
from settingsFile import isRunning
from objects.star import starClass
from updateService import updateScreen

starObject1 = starClass()
starObject2 = starClass()
starObject2.positionX = settings.screen_Width-starObject2.image.get_width()

starObject1.velocityX = 1
starObject2.velocityX = -1

while settings.isRunning:
    updateScreen()
    starObject1.update()
    starObject2.update()
    
    pygame.display.flip()
    
    clock.tick(settings.frameRate)
pygame.quit()