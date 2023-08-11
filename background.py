import pygame       

class Background:
    def __init__(self): 

        background_layer_02 = pygame.Surface((256*3, 248), pygame.SRCALPHA)
        background_layer_02.blit(pygame.image.load("assets/Background/Background_layer_02.png").convert_alpha(), (0, 0))
        background_layer_02.blit(pygame.image.load("assets/Background/Background_layer_02.png").convert_alpha(), (256, 0))
        background_layer_02.blit(pygame.image.load("assets/Background/Background_layer_02.png").convert_alpha(), (512, 0))
        background_layer_03 = pygame.Surface((780, 195), pygame.SRCALPHA)
        background_layer_03.blit(pygame.image.load("assets/Background/Background_layer_03.png").convert_alpha(), (0, 0))
        background_layer_03.blit(pygame.image.load("assets/Background/Background_layer_03.png").convert_alpha(), (260, 0))
        background_layer_03.blit(pygame.image.load("assets/Background/Background_layer_03.png").convert_alpha(), (520, 0))
        background_layer_04 = pygame.Surface((780, 195), pygame.SRCALPHA)
        background_layer_04.blit(pygame.image.load("assets/Background/Background_layer_04.png").convert_alpha(), (0, 0))
        background_layer_04.blit(pygame.image.load("assets/Background/Background_layer_04.png").convert_alpha(), (260, 0))
        background_layer_04.blit(pygame.image.load("assets/Background/Background_layer_04.png").convert_alpha(), (520, 0))
        self.layers =[
            pygame.transform.scale(pygame.image.load("assets/Background/Background_layer_01.png"), (600, 300)),
            background_layer_02,
            background_layer_03,
            background_layer_04,
            ]
         
        self.img = pygame.image.load("assets/Base/5.png")
    def draw(self, screen, x,y):
        
        # elif(x>230):
        #     screen.blit(self.layers[1], (-0.1* x, 30))
        #     screen.blit(self.layers[2], (-0.3* x, 70))
        #     screen.blit(self.layers[3], (-0.7*x-512, 100))

        screen.blit(self.layers[0], (0, 0))

        screen.blit(self.layers[1], (-0.1*x+(0.1*x//768-1)*768, 30))
        screen.blit(self.layers[1], (-0.1*x+(0.1*x//768)*768, 30))
        screen.blit(self.layers[1], (-0.1*x+(0.1*x//768+1)*768, 30))

        screen.blit(self.layers[2], (-0.3*x+(0.3*x//780-1)*780, 70))
        screen.blit(self.layers[2], (-0.3*x+(0.3*x//780)*780, 70))
        screen.blit(self.layers[2], (-0.3*x+(0.3*x//780+1)*780, 70))

        screen.blit(self.layers[3], (-0.7*x+(0.7*x//780-1)*780, 100))
        screen.blit(self.layers[3], (-0.7*x+(0.7*x//780)*780, 100))
        screen.blit(self.layers[3], (-0.7*x+(0.7*x//780+1)*780, 100))

        for i in range(-50,50):
            screen.blit(self.img,(-0.7*x+i*90, 200))
        
        