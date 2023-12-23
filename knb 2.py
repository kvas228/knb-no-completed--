import pygame,sys
from button import *
from tkinter import Button
# Инициализируем библиотеку pygame
pygame.init()

running = True
GAME_RES = WIDTH, HEIGHT = 1024, 1024
FPS = 60
# Устанавливаем ширину и высоту окна
window = pygame.display.set_mode((1024,1024,))
icon = pygame.image.load('image/icon.png')
background_image = pygame.image.load('image/k.png')
pygame.display.set_icon(icon)
kamen = pygame.Surface((50,69))
kamen.fill((86, 91, 99))
myfont = pygame.font.Font('fonts/Montserrat-Black.ttf',35)
text_surface = myfont.render('Игра Камень,ножницы, Бумага:',True,(33, 30, 48))
text_surface2 = myfont.render('Menu',True,(33, 30, 48))
object = pygame.image.load('image/k.png')
object2 = pygame.image.load('image/b.png')
object3 = pygame.image.load('image/n.png')
background_image = pygame.image.load('image/fon4.png')
def get_font(size):
    pass
while running:
    #window.blit(background_image,(0,0))
    pygame.display.update()
    #background_color = (114, 229, 242)
    #window.blit(background_image,(1,1)) Фон
    window.blit(object, (800,400))
    window.blit(object2, (1,450))
    window.blit(object3, (700,100))
    window.blit(text_surface, (200, 150))
    window.blit(text_surface2, (490, 180))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                window.fill((148, 135, 153))
                pygame.display.update()
            if event.key == pygame.K_b:
                pygame.display.update()
                window.fill((0, 0, 0))
                pygame.display.update()
            if event.key == pygame.K_ESCAPE:
                exit()
