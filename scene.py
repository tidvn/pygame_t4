import pygame
class Scene:
    def __init__(self):
        pygame.init()
        WINDOW_WIDTH = 800
        WINDOW_HEIGHT = 600
        self.surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("My Game") 
    def handle_events(self):
        pass
    def draw(self):
        pass

class StartScene(Scene):
    def __init__(self):
        super().__init__()
        self.start_button = pygame.Rect(300, 200, 200, 100)

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button.collidepoint(event.pos):
                return True
        return False

    def draw(self):
        
        pygame.draw.rect(self.surface, (0, 255, 0), self.start_button)
        font = pygame.font.SysFont(None, 48)
        text = font.render("Start Game", True, (255, 255, 255))
        self.surface.blit(text, (320, 230))


class EndScene(Scene):
    def __init__(self):
        super().__init__()
        self.restart_button = pygame.Rect(300, 200, 200, 100)

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.restart_button.collidepoint(event.pos):
                return True
        return False

    def draw(self):
        pygame.draw.rect(self.surface, (255, 0, 0), self.restart_button)
        font = pygame.font.SysFont(None, 48)
        text = font.render("Restart Game", True, (255, 255, 255))
        self.surface.blit(text, (310, 230))
