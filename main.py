import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
clock = pygame.time.Clock()

#paddle vars
paddle_width = 120
paddle_height = 20
paddle_x = (SCREEN_WIDTH / 2) - (paddle_width / 2)
paddle_y = SCREEN_HEIGHT - paddle_height 
paddle_pos = pygame.Vector2(paddle_x,paddle_y)

#ball vars
ball_rad = 10
ball_x = (SCREEN_WIDTH / 2)
ball_y = (SCREEN_HEIGHT / 2)
ball_pos = pygame.Vector2(ball_x, ball_y)

paddle = Paddle(screen,paddle_pos,paddle_width, paddle_height)
ball = Ball(screen,ball_pos,ball_rad, paddle)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('purple')
    paddle.draw()
    paddle.update()

    ball.draw()
    ball.update()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()  
