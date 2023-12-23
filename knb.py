
import pygame,sys
import time
from random import *
import random
from pygame.locals import *
import pygame_menu
clock = pygame.time.Clock()
# Инициализируем библиотеку pygame
pygame.init()

class Start():
    window = pygame.display.set_mode((1920, 1080,))
    background_image = pygame.image.load('image/fon6.jpg')
    muz = pygame.mixer.Sound('audio/muz.mp3')
    muz.play()
    FPS = 60
    icon = pygame.image.load('image/icon.png')
    pygame.display.set_icon(icon)
    myfont = pygame.font.Font('fonts/Montserrat-Black.ttf', 35)
    text_surface = myfont.render('Игра Камень,ножницы, Бумага:', True, (33, 30, 48))
    text_surface2 = myfont.render('Menu', True, (33, 30, 48))
    img_k = pygame.image.load('image/k.png')
    img_b = pygame.image.load('image/b.png')
    img_n = pygame.image.load('image/n.png')
    player = pygame.image.load('image/left/left1.png')
    background_image = pygame.image.load('image/fon6.jpg')
    running = True
st1 = Start()

class Player_1():
    knb_player1 = random.choice([pygame.image.load('image/k.PNG'),pygame.image.load('image/b.PNG'),pygame.image.load('image/n.PNG')])
    walk_left = [pygame.image.load('image/left/left1.png'), pygame.image.load('image/left/left2.png'),
                 pygame.image.load('image/left/left3.png'),
                 pygame.image.load('image/left/left4.png'), pygame.image.load('image/left/left5.png'),
                 pygame.image.load('image/left/left6.png'),
                 pygame.image.load('image/left/left7.png'), pygame.image.load('image/left/left8.png'),
                 pygame.image.load('image/left/left9.png')]
    walk_rigth = [pygame.image.load('image/right/right1.png'), pygame.image.load('image/right/right2.png'),
                  pygame.image.load('image/right/right3.png')
        , pygame.image.load('image/right/right4.png'), pygame.image.load('image/right/right5.png'),
                  pygame.image.load('image/right/right6.png')
        , pygame.image.load('image/right/right7.png'), pygame.image.load('image/right/right8.png'),
                  pygame.image.load('image/right/right9.png')]
    walk_up = [
        pygame.image.load('image/up/up1.png'), pygame.image.load('image/up/up2.png'),
        pygame.image.load('image/up/up3.png'),
        pygame.image.load('image/up/up4.png'), pygame.image.load('image/up/up5.png'),
        pygame.image.load('image/up/up6.png'),
        pygame.image.load('image/up/up7.png'), pygame.image.load('image/up/up8.png'),
        pygame.image.load('image/up/up9.png'), ]
    walk_down = [pygame.image.load('image/down/down1.png'), pygame.image.load('image/down/down2.png'),
                 pygame.image.load('image/down/down3.png')
        , pygame.image.load('image/down/down4.png'), pygame.image.load('image/down/down5.png'),
                 pygame.image.load('image/down/down6.png')
        , pygame.image.load('image/down/down7.png'), pygame.image.load('image/down/down8.png'),
                 pygame.image.load('image/down/down9.png'),
                 ]
    walk_stay = [pygame.image.load('image/down/down1.png'), pygame.image.load('image/down/down2.png')]
    bg_x = 0
    bg_x2 = 0
    player_speed = 10
    p_x = 300
    p_y = 820
    p_x2 = p_x + 500
    p_y2 = p_y - 500
    jump = False
    jump_count = 13
    player_anim_count = 0
    player_anim_count_stay = 0
    player_speed = 10
    cuenta = [pygame.image.load('image/1.jpg'), pygame.image.load('image/1.jpg'), pygame.image.load('image/1.jpg'),
              pygame.image.load('image/2.jpg'), pygame.image.load('image/2.jpg'), pygame.image.load('image/2.jpg'),
              pygame.image.load('image/3.jpg'), pygame.image.load('image/3.jpg'), pygame.image.load('image/3.jpg')]
pl1 = Player_1()
class Player_2():
    walk_left = [pygame.image.load('image/left/left1.png'), pygame.image.load('image/left/left2.png'),
                 pygame.image.load('image/left/left3.png'),
                 pygame.image.load('image/left/left4.png'), pygame.image.load('image/left/left5.png'),
                 pygame.image.load('image/left/left6.png'),
                 pygame.image.load('image/left/left7.png'), pygame.image.load('image/left/left8.png'),
                 pygame.image.load('image/left/left9.png')]
    walk_rigth = [pygame.image.load('image/right/right1.png'), pygame.image.load('image/right/right2.png'),
                  pygame.image.load('image/right/right3.png')
        , pygame.image.load('image/right/right4.png'), pygame.image.load('image/right/right5.png'),
                  pygame.image.load('image/right/right6.png')
        , pygame.image.load('image/right/right7.png'), pygame.image.load('image/right/right8.png'),
                  pygame.image.load('image/right/right9.png')]
    walk_up = [
        pygame.image.load('image/up/up1.png'), pygame.image.load('image/up/up2.png'),
        pygame.image.load('image/up/up3.png'),
        pygame.image.load('image/up/up4.png'), pygame.image.load('image/up/up5.png'),
        pygame.image.load('image/up/up6.png'),
        pygame.image.load('image/up/up7.png'), pygame.image.load('image/up/up8.png'),
        pygame.image.load('image/up/up9.png'), ]
    walk_down = [pygame.image.load('image/down/down1.png'), pygame.image.load('image/down/down2.png'),
                 pygame.image.load('image/down/down3.png')
        , pygame.image.load('image/down/down4.png'), pygame.image.load('image/down/down5.png'),
                 pygame.image.load('image/down/down6.png')
        , pygame.image.load('image/down/down7.png'), pygame.image.load('image/down/down8.png'),
                 pygame.image.load('image/down/down9.png'),
                 ]
    walk_stay = [pygame.image.load('image/down/down1.png'), pygame.image.load('image/down/down2.png')]
    bg_x = 0
    bg_x2 = 0
    player_speed = 10
    p_x = 500
    p_y = 820
    jump = False
    jump_count = 13
    animation_count = 7
    player_anim_count = 0
    player_anim_count_stay = 0
    player_speed = 10
pl2 = Player_2()

def start_the_game():
    while st1.running:
        st1.window.blit(st1.background_image, ((0, 0)))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and pl1.p_x > 200:
            pl1.p_x -= pl1.player_speed
            st1.window.blit(pl1.walk_left[pl1.player_anim_count], (pl1.p_x, pl1.p_y))
        else:
            st1.window.blit(pl1.walk_stay[pl1.player_anim_count_stay], (pl1.p_x, pl1.p_y))
        if keys[pygame.K_RIGHT] and pl1.p_x < 1700:
            pl1.p_x += pl1.player_speed
            st1.window.blit(pl1.walk_rigth[pl1.player_anim_count], (pl1.p_x, pl1.p_y))
        else:
            st1.window.blit(pl1.walk_stay[pl1.player_anim_count_stay], (pl1.p_x, pl1.p_y))
        if keys[pygame.K_e]:
            while True:
                st1.window.blit(pl1.cuenta[pl1.player_anim_count], (pl1.p_x2, pl1.p_y2))
                st1.window.blit(pl1.knb_player1, (pl1.p_x2, pl1.p_y2))
                break
        if not pl1.jump:
            if keys[pygame.K_SPACE]:
                pl1.jump = True

        else:
            if pl1.jump_count >= -13:
                if pl1.jump_count > 0:
                    pl1.p_y -= (pl1.jump_count ** 2) / 2
                else:
                    pl1.p_y += (pl1.jump_count ** 2) / 2
                pl1.jump_count -= 1
            else:
                pl1.jump = False
                pl1.jump_count = 13

        if pl1.player_anim_count == 8:
            pl1.player_anim_count = 0
        else:
            pl1.player_anim_count += 1
        pl1.bg_x -= 2
        if pl1.bg_x == -1136:
            pl1.bg_x = 0
        pl1.bg_x2 += 2
        if pl1.bg_x == 1136:
            pl1.bg_x = 0
        if pl1.player_anim_count_stay == 1:
            pl1.player_anim_count_stay = 0
        else:
            pl1.player_anim_count_stay += 1
        if keys[pygame.K_a] and pl2.p_x > 200:
            pl2.p_x -= pl2.player_speed
            st1.window.blit(pl2.walk_left[pl2.player_anim_count], (pl2.p_x, pl2.p_y))
        else:
            st1.window.blit(pl2.walk_stay[pl2.player_anim_count_stay], (pl2.p_x, pl2.p_y))
        if keys[pygame.K_d] and pl2.p_x < 1700:
            pl2.p_x += pl2.player_speed
            st1.window.blit(pl2.walk_rigth[pl2.player_anim_count], (pl2.p_x, pl2.p_y))
        else:
            st1.window.blit(pl2.walk_stay[pl2.player_anim_count_stay], (pl2.p_x, pl2.p_y))
        if not pl2.jump:
            if keys[pygame.K_CAPSLOCK]:
                pl2.jump = True
        else:
            if pl2.jump_count >= -13:
                if pl2.jump_count > 0:
                    pl2.p_y -= (pl2.jump_count ** 2) / 2
                else:
                    pl2.p_y += (pl2.jump_count ** 2) / 2
                pl2.jump_count -= 1
            else:
                pl2.jump = False
                pl2.jump_count = 13

        if pl2.player_anim_count == 8:
            pl2.player_anim_count = 0
        else:
            pl2.player_anim_count += 1
        pl2.bg_x -= 2
        if pl2.bg_x == -1136:
            pl2.bg_x = 0
        pl2.bg_x2 += 2
        if pl2.bg_x == 1136:
            pl2.bg_x = 0
        if pl2.player_anim_count_stay == 1:
            pl2.player_anim_count_stay = 0
        else:
            pl2.player_anim_count_stay += 1
        pygame.display.update()
        clock.tick(17)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                st1.running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()

def set_difficulty(value, difficulty):
    pass
menu = pygame_menu.Menu('Игра Камень,ножницы, Бумага:', 1080,720,
                       theme=pygame_menu.themes.THEME_DARK)
menu.add.text_input('Введите ваше Имя :', default='Имя')
menu.add.selector('Режим игры:', [('С компьютером', 1), ('Онлайн', 2),('Локальный',3)], onchange=set_difficulty)
menu.add.button('Играть', start_the_game)
menu.add.button('Выход', pygame_menu.events.EXIT)
menu.mainloop(st1.window)

