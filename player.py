import pygame

from background import Background
G=0.05
class Player:
    def __init__(self,surface): 
        self.state = "idle"
        self.direction = "right"
        self.Idle = [pygame.image.load("assets/Sprites/Character1/idle/tile000.png"),
                     pygame.image.load("assets/Sprites/Character1/idle/tile001.png"),
                     pygame.image.load("assets/Sprites/Character1/idle/tile002.png"),
                     pygame.image.load("assets/Sprites/Character1/idle/tile003.png"),
                    ]
        self.Jump = [pygame.image.load("assets/Sprites/Character1/jump/tile000.png"),
                     pygame.image.load("assets/Sprites/Character1/jump/tile001.png"),
                     pygame.image.load("assets/Sprites/Character1/fall/tile000.png"),
                     pygame.image.load("assets/Sprites/Character1/fall/tile001.png"),
                    ]
        self.Run = [pygame.image.load("assets/Sprites/Character1/run/tile000.png"),
                     pygame.image.load("assets/Sprites/Character1/run/tile001.png"),
                     pygame.image.load("assets/Sprites/Character1/run/tile002.png"),
                     pygame.image.load("assets/Sprites/Character1/run/tile003.png"),
                     pygame.image.load("assets/Sprites/Character1/run/tile004.png"),
                     pygame.image.load("assets/Sprites/Character1/run/tile005.png"),
                    ]
        self.count=0       
        self.surface= surface
        self.x=200
        self.y=0
        self.height=50
        self.width=50
        self.lastY=0   
        self.speed=0.1
        self.background = Background()
    
    def draw(self):
        if(self.state == "idle"):
            if(self.direction == "right"):
                self.surface.blit(self.Idle[(self.count//16)%4],(200,self.y))
            else:
                self.surface.blit(pygame.transform.flip(self.Idle[(self.count//16)%4], True, False),(200,self.y))
        if(self.state == "jump"):
            if(self.direction == "right"):
                self.surface.blit(self.Jump[1],(200,self.y))
            else:
                self.surface.blit(pygame.transform.flip(self.Jump[1], True, False),(200,self.y))
        if(self.state == "fall"):
            if(self.direction == "right"):
                self.surface.blit(self.Jump[3],(200,self.y))
            else:
                self.surface.blit(pygame.transform.flip(self.Jump[3], True, False),(200,self.y))
        if(self.state == "run"):
            if(self.direction == "right"):
                self.surface.blit(self.Run[(self.count//16)%4],(200,self.y)) 
            else:
                self.surface.blit(pygame.transform.flip(self.Run[(self.count//16)%6], True, False) ,(200,self.y))   
        self.count+=1 
    def check_collision(self,rect1, rect2):
        if (rect1[0] < rect2[0] + rect2[2] and
                rect1[0] + rect1[2] > rect2[0] and
                rect1[1] < rect2[1] + rect2[3] and
                rect1[1] + rect1[3] > rect2[1]):
            return True
        return False
    def update(self):
        rectPlayer = [ self.x,  self.y,  self.width,  self.height]
        rectBase = [ 0,  210,  100000,  500]
        if(self.speed!=0):
            self.y += self.speed + 0.5*G
            self.speed += G
        if(self.check_collision(rectPlayer, rectBase)):    
            self.speed = 0
        if self.speed >0:
            self.state="fall"       
        key_input = pygame.key.get_pressed()
        if(key_input):
            if key_input[pygame.K_a]:
                self.direction="left"
                self.state = "run" 
                if(self.x>0):
                    self.x-=1
            if key_input[pygame.K_d]  :
                self.direction="right"
                self.state = "run"
                self.x+=1
            if key_input[pygame.K_SPACE] and self.check_collision(rectPlayer, rectBase):
                self.state="jump"
                self.speed = -3
        
        else:
            self.state = "idle"
        self.background.draw(self.surface,self.x,self.y)        
        self.draw()
        print(self.speed)
    

        