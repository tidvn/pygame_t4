import pygame
from game import GameManager
from scene import StartScene,EndScene
FPS = 165
fpsClock = pygame.time.Clock()

start_scene = StartScene()
end_scene = EndScene()
game_scene=GameManager((600,300),pygame.image.load("assets/Props/props.png"),"game xịn") 
def gamerun(game):
    game.start()
    while True:
        dt = fpsClock.tick(FPS) 
        game.update(dt)
        
# current_scene = start_scene
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 running = False

#         if current_scene == start_scene:
#             if start_scene.handle_events(event):
#                 current_scene = end_scene
#         elif current_scene == end_scene:
#             if end_scene.handle_events(event):
#                 current_scene = start_scene

#     current_scene.draw()
gamerun(game_scene)
pygame.quit()
input()
    
     