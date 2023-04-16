from pygame import *
import pygame
import time as tm
import sys

font.init()
main_font = font.Font(None, 50)
win_text = main_font.render("Игрок 1 выиграл!", True, (0, 191, 25))
lose_text = main_font.render("Игрок 2 выиграл!", True, (0, 191, 25))

win_width = 700
win_height = 500

enemy_points = 0
player_points = 0

game = True
finish = False

window = display.set_mode((win_width, win_height))
display.set_caption("Пинг Понг")
back = (0, 170, 204)
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, width, height, speed_x, speed_y):
        sprite.Sprite.__init__(self)
        self.player_image = transform.scale(image.load(player_image), (width,height))
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rect = self.player_image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

    def reset(self):
        window.blit(self.player_image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_P(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_e] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        elif keys_pressed[K_d] and self.rect.y < win_height - 102:
            self.rect.y += self.speed_y
        
        self.reset()

    def update_E(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_r] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        elif keys_pressed[K_f] and self.rect.y < win_height - 102:
            self.rect.y += self.speed_y

        self.reset()

class Ball(GameSprite):
    def update(self):
        global enemy_points
        global player_points

        if self.rect.y <= 0:
            self.speed_y = 3
        elif self.rect.y >= win_height - 50:
            self.speed_y = -3

        if self.colliderect(player):
            self.speed_x = 3
        elif self.colliderect(enemy):
            self.speed_x = -3

        if self.rect.x >= win_width:
            player_points += 1
            self.rect.x = 300
            self.rect.y = 200
            self.speed_x = 3
            self.speed_y = 3

        elif self.rect.x <= 0:
            enemy_points += 1
            self.rect.x = 300
            self.rect.y = 200
            self.speed_x = 3
            self.speed_y = 3

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        self.reset()

clock = time.Clock()
player = Player("player.png", 10, 200, 10, 100, 0, 3)
enemy = Player("player.png", 680, 200, 10, 100, 0, 3)
ball = Ball("ball.png", 300, 200, 50,50, 3, 3)

while game:
    while finish != True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
                game = False
                pygame.quit()

        window.fill(back)
        player.update_P()
        enemy.update_E()
        ball.update()

        if player_points >= 5:
            finish = True
            window.blit(win_text, (250, 100))

        elif enemy_points >= 5:
            finish = True
            window.blit(lose_text, (250, 100))

        display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
            game = False
            pygame.quit()