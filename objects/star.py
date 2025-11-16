import pygame
import settingsFile
import uniqueKeyService
import objectsService
import random

screen = settingsFile.screen

class starClass():
    def __init__(self):
        self.uniqueKey = uniqueKeyService.requestUniqueKey()
        
        self.imageSource = "images/star.bmp"
        self.positionX = 0
        self.positionY = 0
        
        self.velocityX = 10
        self.velocityY = 0
        
        self.image = pygame.image.load(self.imageSource).convert_alpha()
        self.isUpdating = True
        self.spriteRect = self.image.get_rect()
        
        self.onTouchingColor = (255, 0, 0, 60)
        self.onNotTouchingColor = (0, 0, 255, 60)
        
        self.hitboxColor = (0, 0, 255, 60)
        
        self.hitboxVisual = pygame.Surface((self.image.get_width(), self.image.get_height()), pygame.SRCALPHA)
        self.hitboxVisual.fill(self.hitboxColor)
        
        objectsService.objectList.append(self)
    def checkforCollision(self):
        for object in objectsService.objectList:
            if object.uniqueKey != self.uniqueKey:
                if self.spriteRect.colliderect(object.spriteRect):
                    self.hitboxVisual.fill(self.onTouchingColor)
                    return

        self.hitboxVisual.fill(self.onNotTouchingColor)
    def draw(self, x, y):
        screen.blit(self.image, (x, y))
        screen.blit(self.hitboxVisual, (self.positionX, self.positionY))
                        
    def updateVelocity(self):
        self.positionX += self.velocityX
        self.positionY += self.velocityY
        
    def update(self):
        self.updateVelocity()
        self.draw(self.positionX, self.positionY)
        self.spriteRect.center = (self.positionX+self.image.get_width()/2, self.positionY+self.image.get_width()/2)
        
        self.checkforCollision()