import pygame
import os
# from base import Base
from player import Player
class GameManager:
    def __init__(self,size,icon,title):
        pygame.init()
        self.surface= pygame.display.set_mode(size)
        pygame.display.set_icon(icon)
        pygame.display.set_caption(title)
        self.player = Player(self.surface)  
        # self.base = Base(self.surface)   
    def check_collision(self,rect1, rect2):
        if (rect1[0] < rect2[0] + rect2[2] and
                rect1[0] + rect1[2] > rect2[0] and
                rect1[1] < rect2[1] + rect2[3] and
                rect1[1] + rect1[3] > rect2[1]):
            return True
        return False      
    def start(self):
        pass
    
    def update(self,dt):
        # rectPlayer = [ self.player.x,  self.player.y,  self.player.width,  self.player.height]
        # rectBase = [ 0,  250,  1000,  50]
         
            # self.player.y=160
            # self.player.speed=0
        self.player.update()
        # self.base.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
