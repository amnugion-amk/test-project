import pygame
import settingsFile
screen = settingsFile.screen

class starClass():
    def __init__(self):
        self.imageSource = "images/star.bmp"
        self.positionX = 0
        self.positionY = 0
        
        self.velocityX = 10
        self.velocityY = 0
        
        self.image = pygame.image.load(self.imageSource).convert_alpha()
        self.isUpdating = True
        
    def draw(self, x, y):
        screen.blit(self.image, (x, y))
        
    def updateVelocity(self):
        self.positionX += self.velocityX
        self.positionY += self.velocityY
        
    def update(self):
        self.updateVelocity()
        self.draw(self.positionX, self.positionY)
        
starObject = starClass()