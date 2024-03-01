import pygame
class Paddle:

    def __init__(self, screen, pos, width, height):
        self.height = height
        self.width = width
        self.color = 'white'
        self.screen = screen
        self.pos = pos
        self.velocity = 10

    def get_pos(self):
        return self.pos

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def draw(self):
        pygame.draw.rect(self.screen, 
                        self.color, 
                        pygame.Rect(
                             self.pos.x,
                             self.pos.y,
                             self.width,
                             self.height
                         ))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.pos.x -= self.velocity
            
        if keys[pygame.K_RIGHT]:
            self.pos.x += self.velocity

        #wall collision
        if self.pos.x + self.width > self.screen.get_width():
            self.pos.x = self.screen.get_width() - self.width

        
        if self.pos.x < 0:
            self.pos.x = 0 
