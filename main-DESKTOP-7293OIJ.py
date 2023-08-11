import pygame
from game import GameManager
FPS = 165
fpsClock = pygame.time.Clock()
game=GameManager((600,300),pygame.image.load("assets/Props/props.png"),"game xịn")
 
game.start()
while True:
    dt = fpsClock.tick(FPS) 
    game.update(dt)
    
    
      