# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 12:07:16 2024

@author: bluet
"""
import random
import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))

class Charlie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
    
        self.image = pygame.image.load("elephant.png")
        self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.centerx = 320
        self.rect.centery = 240
        
        self.dx = 5
        self.dy = 3
        
    def update(self):
        self.rect.right += self.dx
        if self.rect.centerx >= screen.get_width():
            self.rect.centerx = screen.get_width()
            self.dx = -self.dx + random.randint(-10,10)
            if self.dx > 25:
                self.dx = 5
            elif self.dx < -25:
                self.dx = -5
        elif self.rect.centerx <= 0:
            self.rect.centerx = 0
            self.dx = -self.dx + random.randint(-10,10)
            if self.dx > 25:
                self.dx = 5
            elif self.dx < -25:
                self.dx = -5
        self.rect.top += self.dy
        if self.rect.centery >= screen.get_height():
            self.rect.centery = screen.get_height()
            self.dy = -self.dy + random.randint(-10,10)
            if self.dy > 25:
                self.dy = 5
            elif self.dy < -25:
                self.dy = -5
        elif self.rect.centery <= 0:
            self.rect.centery = 0
            self.dy = -self.dy + random.randint(-10,10)
            if self.dy > 25:
                self.dy = 5
            elif self.dy < -25:
                self.dy = -5
    
            
def main():
    
    pygame.display.set_caption("Bouncing Image")
    background = pygame.image.load("sample.png")
    background.convert_alpha()
    background = pygame.transform.scale(background,screen.get_size())
    screen.blit(background, (0, 0))
    
    charlie = Charlie()
    allSprites = pygame.sprite.Group(charlie)
    
    clock = pygame.time.Clock()
    keepGoing = True
    while(keepGoing):
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
        
if __name__ == "__main__":
    main()
    pygame.quit()   

