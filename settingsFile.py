import pygame

class settingsClass():
    def __init__(self):
        self.screen_Width = 1000
        self.screenHeight = 1000
        
        self.backgroundColor = (255, 255, 255)
        self.isRunning = True
        
        self.frameRate = 60
        
settings = settingsClass()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((settings.screen_Width, settings.screenHeight), pygame.RESIZABLE)
isRunning = True