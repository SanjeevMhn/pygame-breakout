import pygame
class Ball:

    def __init__(self,screen,pos,rad,paddle):
        self.screen = screen
        self.pos = pos
        self.color = 'orange'
        self.rad = rad
        self.x_velocity = 4
        self.y_velocity = 5
        self.paddle = paddle

    def draw(self):
        pygame.draw.circle(self.screen,
                           self.color, 
                           self.pos, 
                           self.rad)

    def update(self):
        self.pos.x += self.x_velocity
        self.pos.y -= self.y_velocity
        
        #collision with wall
        if self.pos.x > self.screen.get_width() - self.rad or self.pos.x < 0:
            self.x_velocity = -self.x_velocity

        if self.pos.y < 0:
            self.y_velocity = -self.y_velocity

        #collision with paddle
        if self.pos.y + self.rad  > self.screen.get_height() - self.paddle.get_height():
            if self.pos.x > self.paddle.get_pos().x and self.pos.x < self.paddle.get_pos().x + self.paddle.get_width():
                self.y_velocity = -self.y_velocity
        

        
