import os
import random
from random import randint
import ctypes
import pygame

pygame.init()

# настройка окна и шрифта
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Zombie Wave")
font_menu = pygame.font.Font(None, 120)
font = pygame.font.Font(None, 36)

# экран загрузки
screen.blit(font_menu.render("Загрузка...", True, (255, 255, 255)), (250, 250))
pygame.display.update()

# читаем прогресс
if os.path.exists("progress.txt"):
    with open("progress.txt", "r") as file:
        val = file.readlines()
        coins = int(val[0])
        airplane_summon_bought = int(val[1])
        damage = int(val[2])
        upgrade_gun_price = int(val[3])
        clip = int(val[4])
        robot_bought = int(val[5])
        mine_bought = int(val[6])
        barricades_bought = int(val[7])
        robot_damage = float(val[8])
        robot_upgrade_price = int(val[9])
        max_level_completed = int(val[10])
        volume = float(val[11])
        slider_y = float(val[12])
        music_on = int(val[13])
        sfx_on = int(val[14])
        tutorial_watched = int(val[15])
    file.close()
else:
    file = open("progress.txt", "x")
    file.close()
    file = open("progress.txt", "r")
    airplane_summon_bought = 0
    file.close()
    coins = 0
    damage = 1
    upgrade_gun_price = 70
    clip = 30
    robot_bought = 0
    mine_bought = 0
    barricades_bought = 0
    robot_damage = 0.1
    robot_upgrade_price = 30
    max_level_completed = 0
    volume = 100
    slider_y = 250
    music_on = 1
    sfx_on = 1
    tutorial_watched = 0

# загрузка спрайтов
menu_bg = pygame.image.load("assets\\sprites\\menu_bg.jpg")
menu_bg = pygame.transform.scale(menu_bg, (900, 600))
end_screen = pygame.image.load("assets\\sprites\\end_screen.png")
end_screen = pygame.transform.scale(end_screen, (900, 600))
shop_bg = pygame.image.load("assets\\sprites\\shop_bg.png")
shop_bg = pygame.transform.scale(shop_bg, (900, 600))
airplane_summon = pygame.image.load("assets\\sprites\\airplane_summon.png")
airplane_summon = pygame.transform.scale(airplane_summon, (100, 240))
play = pygame.image.load("assets\\sprites\\play.png")
shop = pygame.image.load("assets\\sprites\\shop.png")
first_level = pygame.image.load("assets\\sprites\\1_level.png")
second_level = pygame.image.load("assets\\sprites\\2_level.png")
third_level = pygame.image.load("assets\\sprites\\3_level.png")
fourth_level = pygame.image.load("assets\\sprites\\4_level.png")
fifth_level = pygame.image.load("assets\\sprites\\5_level.png")
sixth_level = pygame.image.load("assets\\sprites\\6_level.png")
seventh_level = pygame.image.load("assets\\sprites\\7_level.png")
eighth_level = pygame.image.load("assets\\sprites\\8_level.png")
ninth_level = pygame.image.load("assets\\sprites\\9_level.png")
tenth_level = pygame.image.load("assets\\sprites\\10_level.png")
eleventh_level = pygame.image.load("assets\\sprites\\11_level.png")
twelfth_level = pygame.image.load("assets\\sprites\\12_level.png")
thirteenth_level = pygame.image.load("assets\\sprites\\13_level.png")
fourteenth_level = pygame.image.load("assets\\sprites\\14_level.png")
fifteenth_level = pygame.image.load("assets\\sprites\\15_level.png")
sixteenth_level = pygame.image.load("assets\\sprites\\16_level.png")
seventeenth_level = pygame.image.load("assets\\sprites\\17_level.png")
eighteenth_level = pygame.image.load("assets\\sprites\\18_level.png")
nineteenth_level = pygame.image.load("assets\\sprites\\19_level.png")
twentieth_level = pygame.image.load("assets\\sprites\\20_level.png")
level_bg = pygame.image.load("assets\\sprites\\level_bg.png")
level_bg2 = pygame.image.load("assets\\sprites\\level_bg2.png")
player = pygame.image.load("assets\\sprites\\player.png")
player = pygame.transform.scale(player, (100, 200))
zombie = pygame.image.load("assets\\sprites\\zombie.png")
zombie = pygame.transform.scale(zombie, (100, 200))
zombie2 = pygame.image.load("assets\\sprites\\zombie2.png")
zombie2 = pygame.transform.scale(zombie2, (100, 200))
zombie3 = pygame.image.load("assets\\sprites\\zombie3.png")
zombie3 = pygame.transform.scale(zombie3, (100, 200))
zombie4 = pygame.image.load("assets\\sprites\\zombie4.png")
zombie4 = pygame.transform.scale(zombie4, (100, 200))
zombie5 = pygame.image.load("assets\\sprites\\zombie5.png")
zombie5 = pygame.transform.scale(zombie5, (200, 300))
zomboss = pygame.image.load("assets\\sprites\\zomboss.png")
zomboss = pygame.transform.scale(zomboss, (400, 400))
back = pygame.image.load("assets\\sprites\\back.png")
back2 = pygame.image.load("assets\\sprites\\back2.png")
next_pic = back2
next_pic = pygame.transform.scale(next_pic, (119, 114))
buy = pygame.image.load("assets\\sprites\\buy.png")
airplane_summon_ab = pygame.image.load("assets\\sprites\\airplane_summon_ab.png")
airplane_summon_ab = pygame.transform.scale(airplane_summon_ab, (100, 100))
airplane_summon_ab.set_alpha(130)
mine_ab = pygame.image.load("assets\\sprites\\mine_ab.png")
mine_ab = pygame.transform.scale(mine_ab, (100, 100))
mine_ab.set_alpha(130)
airplane_shadow = pygame.image.load("assets\\sprites\\airplane_shadow.png")
airplane_shadow = pygame.transform.scale(airplane_shadow, (300, 100))
airplane_shadow.set_alpha(152)
bomb = pygame.image.load("assets\\sprites\\bomb.png")
explosion = pygame.image.load("assets\\sprites\\explosion.png")
mine_explosion = explosion
mine_explosion = pygame.transform.scale(mine_explosion, (250, 150))
explosion = pygame.transform.scale(explosion, (1200, 600))
m4 = pygame.image.load("assets\\sprites\\m4.png")
m4 = pygame.transform.scale(m4, (300, 100))
robot = pygame.image.load("assets\\sprites\\robot.png")
robot = pygame.transform.scale(robot, (100, 200))
mine = pygame.image.load("assets\\sprites\\mine.png")
mine_shop = mine
mine_shop = pygame.transform.scale(mine_shop, (300, 300))
mine = pygame.transform.scale(mine, (50, 50))
transparent_cube = pygame.image.load("assets\\sprites\\transparent_cube.png")
transparent_cube = pygame.transform.scale(transparent_cube, (900, 600))
barricade = pygame.image.load("assets\\sprites\\barricade.png")
shop_barricade = barricade
shop_barricade = pygame.transform.scale(shop_barricade, (50, 300))
barricade = pygame.transform.scale(barricade, (50, 485))
settings = pygame.image.load("assets\\sprites\\settings.png")
checkbox_empty = pygame.image.load("assets\\sprites\\checkbox_empty.png")
checkbox_filled = pygame.image.load("assets\\sprites\\checkbox_filled.png")
tutorial_screen = pygame.image.load("assets\\sprites\\tutorial_screen.png")
infinity_mode = pygame.image.load("assets\\sprites\\infinity_mode.png")
car = pygame.image.load("assets\\sprites\\car.png")
car = pygame.transform.scale(car, (300, 100))

# загрузка звуков
menu_music = pygame.mixer.Sound("assets\\sounds\\menu.mp3")
level_music = pygame.mixer.Sound("assets\\sounds\\level_music.mp3")
shop_music = pygame.mixer.Sound("assets\\sounds\\shop_music.mp3")
gunshot = pygame.mixer.Sound("assets\\sounds\\gunshot.mp3")
reload = pygame.mixer.Sound("assets\\sounds\\reload.wav")
win_sound = pygame.mixer.Sound("assets\\sounds\\win.mp3")
chaching = pygame.mixer.Sound("assets\\sounds\\cha-ching.mp3")
lose = pygame.mixer.Sound("assets\\sounds\\lose.mp3")
airplane_sound = pygame.mixer.Sound("assets\\sounds\\airplane_sound.mp3")
explosion_sound = pygame.mixer.Sound("assets\\sounds\\explosion.mp3")
nope = pygame.mixer.Sound("assets\\sounds\\nope.mp3")
mine_explosion_sound = pygame.mixer.Sound("assets\\sounds\\mine_explosion.mp3")
final_level_music = pygame.mixer.Sound("assets\\sounds\\big_battle_music.mp3")
level_music2 = pygame.mixer.Sound("assets\\sounds\\level_music2.mp3")
level_music_loc2 = pygame.mixer.Sound("assets\\sounds\\level_music_loc2.mp3")
final_level_music2 = pygame.mixer.Sound("assets\\sounds\\final_level_music.mp3")
win_sound2 = pygame.mixer.Sound("assets\\sounds\\win2.mp3")

# настройка звуков
menu_music.set_volume(volume * 0.01)
level_music.set_volume(volume * 0.01)
shop_music.set_volume(volume * 0.01)
nope.set_volume(volume * 0.01)
win_sound.set_volume(volume * 0.01)
chaching.set_volume(volume * 0.01)
lose.set_volume(volume * 0.01)
airplane_sound.set_volume(volume * 0.01)
explosion_sound.set_volume(volume * 0.01)
mine_explosion_sound.set_volume(volume * 0.01)
gunshot.set_volume(volume * 0.001)
reload.set_volume(volume * 0.01)
mine_explosion_sound.set_volume(volume * 0.01)
final_level_music.set_volume(volume * 0.01)
level_music2.set_volume(volume * 0.01)
level_music_loc2.set_volume(volume * 0.01)
win_sound2.set_volume(volume * 0.01)
final_level_music2.set_volume(volume * 0.01)


# определение переменных
run = True
stage = "menu"
level = 0
x = 50
y = 300
robot_x = 50
robot_y = 100
zombies = []
bullets = []
bullets_have = clip
bullet_tick = 0
target = 0
reload_tick = 0
after_win_tick = 0
reload_tick_activated = False
win_tick = 0
win = 0
item_number = 0
barricade3_hp = 0
shooting = 0
zombies_killed = 0
zombies_spawned = 0
game_over = 0
as_ab_activated = 0
x_text = -300
coins_count_tick = 0
barricade1_rect = pygame.Rect(0, 0, 0, 0)
barricade2_rect = pygame.Rect(0, 0, 0, 0)
barricade3_rect = pygame.Rect(0, 0, 0, 0)
clock = pygame.time.Clock()
x_ab1 = -300
y_ab1 = 150
x1_ab1 = 425
y1_ab1 = -100
bomb_tick = 0
bomb_is_invisible = 0
explosion_activated = 0
bomb_rect = pygame.Rect((250, 50, 600, 500))
explosion_alpha = 255
bomb_tick2 = 0
explosion_activated3 = 0
explosion_timer = 0
loc = 0
barricade1_hp = 0
barricade2_hp = 0
get_money = 0
bullet_robot_tick = 0
mine_placing = 0
mines = []
mines_have = 0
infinity_mode_timer = 0
og_zombie_chance = 0.01
con_zombie_chance = 0.001
bucket_zombie_chance = 0.0001
football_zombie_chance = 0.00001
gargantua_zombie_chance = 0.000001
sl_x1 = 0
sl_x2 = 900
sl_y1 = 300
sl_x3 = 10
sl_hp = 0
sl_timer = 0
zombies_have = 0
explosion_activated2 = 0
zomboss_airplane_damaged = 0


# определение классов
class Button:
    def __init__(self, xx, yy, image):
        self.image = image
        self.rect = image.get_rect()
        self.rect.topleft = (xx, yy)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

    def change_cords(self, xx1, yy1):
        self.rect.x = xx1
        self.rect.y = yy1
        self.rect.topleft = (xx1, yy1)

    def change_image(self, image):
        self.image = image


class Bullet:
    def __init__(self, yyy, damage2):
        self.y = yyy
        self.x = 100
        self.damage = damage2

    def draw(self):
        if self.x < 877:
            rect = pygame.draw.rect(screen, "yellow", (self.x, self.y, 20, 10))
            self.x += 20
            for kk in zombies:
                if rect.colliderect(kk.rect):
                    kk.get_damage(self.damage)
                    bullets.remove(self)
                    del self
                    return 0
        else:
            bullets.remove(self)
            del self


class Zombie:
    def __init__(self, type_of_zombie):
        self.speed = 2
        if type_of_zombie == "zombie":
            self.hp = 3
            self.image = zombie
        elif type_of_zombie == "zombie2":
            self.hp = 5
            self.image = zombie2
        elif type_of_zombie == "zombie3":
            self.hp = 8
            self.image = zombie3
        elif type_of_zombie == "zombie4":
            self.hp = 15
            self.image = zombie4
        elif type_of_zombie == "zombie5":
            self.hp = 100
            self.image = zombie5
            self.speed = 1.1
        elif type_of_zombie == "zomboss":
            self.hp = 4000
            self.image = zomboss
            self.speed = 2
        elif type_of_zombie == "zombie_sl":
            self.image = zombie
        self.type_of_zombie = type_of_zombie
        if self.type_of_zombie != "zombie_sl":
            if type_of_zombie == "zomboss":
                self.y = 100
            else:
                self.y = randint(0, 400)
        else:
            rand = randint(0, 2)
            if rand == 0:
                self.y = 80
            elif rand == 1:
                self.y = 200
            else:
                self.y = 400
        self.x = 1000
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.zombie_attacking_barricade_tick = 0
        self.timer = pygame.time.get_ticks()
        self.timer2 = 4000

    def draw(self):
        if self.type_of_zombie != "zombie_sl":
            if self.x > 155:
                screen.blit(self.image, (self.x, self.y))
                if not self.rect.colliderect(barricade1_rect) and not self.rect.colliderect(barricade2_rect) \
                        and not self.rect.colliderect(barricade3_rect):
                    if self.type_of_zombie != "zomboss":
                        self.x -= self.speed
                        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
                    elif self.type_of_zombie == "zomboss" and self.x >= 600:
                        self.x -= self.speed
                        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
                    else:
                        if pygame.time.get_ticks() - self.timer > self.timer2:
                            self.timer = pygame.time.get_ticks()
                            if self.timer2 > 400:
                                self.timer2 -= 100
                            zombie_choose2 = randint(0, 4)
                            if zombie_choose2 == 0:
                                zombies.append(Zombie("zombie"))
                            elif zombie_choose2 == 1:
                                zombies.append(Zombie("zombie2"))
                            elif zombie_choose2 == 2:
                                zombies.append(Zombie("zombie3"))
                            elif zombie_choose2 == 3:
                                zombies.append(Zombie("zombie4"))
                            else:
                                zombies.append(Zombie("zombie5"))
                else:
                    if self.zombie_attacking_barricade_tick == 0:
                        self.zombie_attacking_barricade_tick = pygame.time.get_ticks()
                    if pygame.time.get_ticks() - self.zombie_attacking_barricade_tick > 500:
                        if self.rect.colliderect(barricade1_rect):
                            self.zombie_attacking_barricade_tick = pygame.time.get_ticks()
                            global barricade1_hp
                            barricade1_hp -= 1
                        elif self.rect.colliderect(barricade2_rect):
                            self.zombie_attacking_barricade_tick = pygame.time.get_ticks()
                            global barricade2_hp
                            barricade2_hp -= 1
                        elif self.rect.colliderect(barricade3_rect):
                            self.zombie_attacking_barricade_tick = pygame.time.get_ticks()
                            global barricade3_hp
                            barricade3_hp -= 1
            else:
                global game_over
                game_over = 1
                del self
                return 0
        else:
            if self.x > -100:
                screen.blit(self.image, (self.x, self.y))
                self.x -= 20
                self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
                if self.rect.colliderect(pygame.Rect(10, sl_y1, car.get_width(), car.get_height())):
                    global sl_hp, zombies_have
                    zombies_have -= 1
                    sl_hp -= 1
                    zombies.remove(self)
                    del self
            else:
                zombies.remove(self)
                zombies_have -= 1
                del self

    def get_damage(self, damage1):
        global zombies_killed, level
        self.hp -= damage1
        self.x += 2.5
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        if self.hp < 1:
            if level == 20 and self.type_of_zombie == "zomboss":
                zombies_killed += 1
            if level != 20:
                zombies_killed += 1
            zombies.remove(self)
            del self


class Mine:
    def __init__(self):
        self.x = pygame.mouse.get_pos()[0] - 23
        self.y = pygame.mouse.get_pos()[1] - 20
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        self.explosion_pic = mine_explosion
        self.explosion_pic_alpha = 255
        self.tick = 0
        self.explosion = 0

    def draw(self):
        zombie_to_kill = 0
        for mm in zombies:
            if self.rect.colliderect(mm.rect):
                self.explosion = 1
                zombie_to_kill = mm
        if self.explosion == 1:
            screen.blit(self.explosion_pic, (self.x - mine.get_size()[0] / 2, self.y - mine.get_size()[1] / 2))
            self.explosion_pic.set_alpha(self.explosion_pic_alpha)
            if self.tick == 0:
                if sfx_on == 1:
                    pygame.mixer.find_channel(True).play(mine_explosion_sound)
                zombie_to_kill.get_damage(20)
                self.tick = pygame.time.get_ticks()
            if pygame.time.get_ticks() - self.tick > 3000:
                self.explosion_pic_alpha -= 5
            if self.explosion_pic_alpha < 1:
                mines.remove(self)
                del self
                return 0
        if self.explosion == 0:
            screen.blit(mine, (self.x, self.y))


class Slider:
    def __init__(self, xx2, yy2, width, height):
        self.rect = pygame.Rect(xx2, yy2, width, height)
        self.clicked = False

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

    def change_val_clicked(self, val1):
        self.clicked = val1

    def get_val_clicked(self):
        return self.clicked


# определение функций
def start_level(level1, get_money1):
    global stage, level, get_money, robot_y, bullets_have, mines_have, mines, \
        barricade1_hp, barricade2_hp, barricade3_hp, back_button, music_on, loc
    mines_have = 10
    stage = "level"
    level = level1
    menu_music.stop()
    if music_on == 1:
        if level1 != 9 and level1 != 19 and level1 != 20:
            if loc == 0:
                level_music.play(-1)
            else:
                level_music_loc2.play(-1)
        else:
            if level1 != 20:
                final_level_music.play(-1)
            else:
                final_level_music2.play(-1)
    get_money = get_money1
    robot_y = 100
    bullets_have = clip
    barricade1_hp = 30
    barricade2_hp = 30
    barricade3_hp = 30
    back_button.change_cords(20, 20)


def win_func():
    global win_tick, win, bullet_robot_tick, target, mine_placing
    win_tick = pygame.time.get_ticks()
    win = 1
    mine_placing = 0
    level_music.stop()
    level_music_loc2.stop()
    final_level_music.stop()
    final_level_music2.stop()
    bullet_robot_tick = 0
    target = 0


# определение экземпляров класса
play_button = Button(272.5, 130, play)
shop_button = Button(272.5, 270, shop)
settings_button = Button(272.5, 410, settings)
first_level_button = Button(20, 130, first_level)
second_level_button = Button(170, 130, second_level)
third_level_button = Button(320, 130, third_level)
fourth_level_button = Button(470, 130, fourth_level)
fifth_level_button = Button(620, 130, fifth_level)
sixth_level_button = Button(770, 130, sixth_level)
seventh_level_button = Button(20, 260, seventh_level)
eighth_level_button = Button(170, 260, eighth_level)
ninth_level_button = Button(320, 260, ninth_level)
tenth_level_button = Button(470, 260, tenth_level)
eleventh_level_button = Button(20, 130, eleventh_level)
twelfth_level_button = Button(170, 130, twelfth_level)
thirteenth_level_button = Button(320, 130, thirteenth_level)
fourteenth_level_button = Button(470, 130, fourteenth_level)
fifteenth_level_button = Button(620, 130, fifteenth_level)
sixteenth_level_button = Button(770, 130, sixteenth_level)
seventeenth_level_button = Button(20, 260, seventeenth_level)
eighteenth_level_button = Button(170, 260, eighteenth_level)
nineteenth_level_button = Button(320, 260, nineteenth_level)
twentieth_level_button = Button(470, 260, twentieth_level)
back_button = Button(20, 20, back)
back_button2 = Button(400, 500, back)
buy_button = Button(600, 500, buy)
back_button3 = Button(500, 500, back2)
next_loc_button = Button(620, 260, next_pic)
slider = Slider(50, slider_y, 20, 20)
if music_on == 0:
    checkbox_music_button = Button(500, 100, checkbox_empty)
else:
    checkbox_music_button = Button(500, 100, checkbox_filled)
if sfx_on == 0:
    checkbox_sfx_button = Button(500, 190, checkbox_empty)
else:
    checkbox_sfx_button = Button(500, 190, checkbox_filled)
infinity_mode_button = Button(272.5, 470, infinity_mode)

# настройка музыки
if music_on == 1:
    menu_music.play(-1)
pygame.mixer.set_num_channels(100)

# основной цикл игры
while run:
    if stage == "level" and level == 1 and zombies_killed >= 20 and win == 0:
        win_func()

    if stage == "level" and level == 2 and zombies_killed >= 50 and win == 0:
        win_func()

    if stage == "level" and level == 3 and zombies_killed >= 35 and win == 0:
        win_func()

    if stage == "level" and level == 4 and zombies_killed >= 50 and win == 0:
        win_func()

    if stage == "level" and level == 5 and zombies_killed >= 90 and win == 0:
        win_func()

    if stage == "level" and level == 6 and zombies_killed >= 200 and win == 0:
        win_func()

    if stage == "level" and level == 7 and zombies_killed >= 150 and win == 0:
        win_func()

    if stage == "level" and level == 8 and zombies_killed >= 230 and win == 0:
        win_func()

    if stage == "level" and level == 9 and zombies_killed >= 350 and win == 0:
        win_func()

    if stage == "level" and level == 11 and zombies_killed >= 170 and win == 0:
        win_func()

    if stage == "level" and level == 12 and zombies_killed >= 300 and win == 0:
        win_func()

    if stage == "level" and level == 13 and zombies_killed >= 200 and win == 0:
        win_func()

    if stage == "level" and level == 14 and zombies_killed >= 200 and win == 0:
        win_func()

    if stage == "level" and level == 15 and zombies_killed >= 500 and win == 0:
        win_func()

    if stage == "level" and level == 16 and zombies_killed >= 200 and win == 0:
        win_func()

    if stage == "level" and level == 17 and zombies_killed >= 20 and win == 0:
        win_func()

    if stage == "level" and level == 18 and zombies_killed >= 300 and win == 0:
        win_func()

    if stage == "level" and level == 19 and zombies_killed >= 350 and win == 0:
        win_func()

    if stage == "level" and level == 19 and zombies_killed >= 350 and win == 0:
        win_func()

    if stage == "level" and level == 20 and zombies_killed >= 1 and win == 0:
        win_func()
        explosion_activated3 = 1
        explosion_timer = pygame.time.get_ticks()
        if sfx_on == 1:
            explosion_sound.play()

    if stage == "level" and level == -1:
        elapsed_time = (pygame.time.get_ticks() - infinity_mode_timer) / 1000
        if elapsed_time > 10:
            og_zombie_chance += 0.001
            con_zombie_chance += 0.0015
            bucket_zombie_chance += 0.002
            football_zombie_chance += 0.0025
            gargantua_zombie_chance += 0.003
            infinity_mode_timer = pygame.time.get_ticks()
        if random.random() < og_zombie_chance:
            zombies_spawned += 1
            zombies.append(Zombie("zombie"))
        if random.random() < con_zombie_chance:
            zombies_spawned += 1
            zombies.append(Zombie("zombie2"))
        if random.random() < bucket_zombie_chance:
            zombies_spawned += 1
            zombies.append(Zombie("zombie3"))
        if random.random() < football_zombie_chance:
            zombies_spawned += 1
            zombies.append(Zombie("zombie4"))
        if random.random() < gargantua_zombie_chance:
            zombies_spawned += 1
            zombies.append(Zombie("zombie5"))

    if stage == "level" and randint(0, 100) == 43 and zombies_spawned < 20 and level == 1:
        zombies_spawned += 1
        zombies.append(Zombie("zombie"))

    if stage == "level" and randint(0, 50) == 43 and zombies_spawned < 50 and level == 2:
        zombies_spawned += 1
        zombies.append(Zombie("zombie"))

    if stage == "level" and randint(0, 75) == 43 and zombies_spawned < 35 and level == 3:
        zombies_spawned += 1
        if randint(0, 3) == 3:
            zombies.append(Zombie("zombie2"))
        else:
            zombies.append(Zombie("zombie"))

    if stage == "level" and randint(0, 80) == 43 and zombies_spawned < 50 and level == 4:
        zombies_spawned += 1
        zombie_choose = randint(0, 3)
        if zombie_choose == 3:
            zombies.append(Zombie("zombie3"))
        elif zombie_choose == 2:
            zombies.append(Zombie("zombie2"))
        else:
            zombies.append(Zombie("zombie"))

    if stage == "level" and randint(0, 30) == 30 and zombies_spawned < 90 and level == 5:
        zombies_spawned += 1
        zombie_choose = randint(0, 3)
        if zombie_choose == 3:
            zombies.append(Zombie("zombie3"))
        elif zombie_choose == 2 or zombie_choose == 1:
            zombies.append(Zombie("zombie2"))
        else:
            zombies.append(Zombie("zombie"))

    if stage == "level" and randint(0, 10) == 10 and zombies_spawned < 200 and level == 6:
        zombies_spawned += 1
        zombies.append(Zombie("zombie"))

    if stage == "level" and randint(0, 20) == 20 and zombies_spawned < 150 and level == 7:
        zombies_spawned += 1
        zombie_choose = randint(0, 3)
        if zombie_choose == 2:
            zombies.append(Zombie("zombie3"))
        elif zombie_choose == 3:
            zombies.append(Zombie("zombie4"))
        elif zombie_choose == 0 or zombie_choose == 1:
            zombies.append(Zombie("zombie2"))

    if stage == "level" and randint(0, 40) == 23 and zombies_spawned < 230 and level == 8:
        zombies_spawned += 1
        zombie_choose = randint(0, 3)
        if zombie_choose == 2:
            zombies.append(Zombie("zombie3"))
        elif zombie_choose == 3:
            zombies.append(Zombie("zombie4"))
        elif zombie_choose == 0 or zombie_choose == 1:
            zombies.append(Zombie("zombie2"))

    if stage == "level" and randint(0, 25) == 23 and zombies_spawned < 350 and level == 9:
        zombies_spawned += 1
        zombie_choose = randint(0, 200)
        if zombie_choose in range(-1, 81):
            zombies.append(Zombie("zombie3"))
        elif zombie_choose in range(80, 161):
            zombies.append(Zombie("zombie4"))
        elif zombie_choose == 200:
            zombies.append(Zombie("zombie5"))
        elif zombie_choose in range(161, 200):
            zombies.append(Zombie("zombie2"))

    if stage == "level" and randint(0, 50) == 50 and zombies_spawned < 170 and level == 11:
        zombies_spawned += 1
        zombie_choose = randint(0, 1)
        if zombie_choose == 0:
            zombies.append(Zombie("zombie3"))
        else:
            zombies.append(Zombie("zombie4"))

    if stage == "level" and randint(0, 20) == 20 and zombies_spawned < 300 and level == 12:
        zombies_spawned += 1
        zombie_choose = randint(0, 71)
        if zombie_choose in range(-1, 71):
            zombies.append(Zombie("zombie"))
        else:
            zombies.append(Zombie("zombie5"))

    if stage == "level" and randint(0, 15) == 15 and zombies_spawned < 200 and level == 13:
        zombies_spawned += 1
        zombies.append(Zombie("zombie2"))

    if stage == "level" and randint(0, 30) == 30 and zombies_spawned < 200 and level == 14:
        zombies_spawned += 1
        zombie_choose = randint(0, 71)
        if zombie_choose in range(-1, 11):
            zombies.append(Zombie("zombie2"))
        elif zombie_choose in range(10, 41):
            zombies.append(Zombie("zombie3"))
        elif zombie_choose in range(40, 71):
            zombies.append(Zombie("zombie4"))
        else:
            zombies.append(Zombie("zombie5"))

    if stage == "level" and randint(0, 7) == 7 and zombies_spawned < 500 and level == 15:
        zombies_spawned += 1
        zombies.append(Zombie("zombie"))

    if stage == "level" and randint(0, 40) == 40 and zombies_spawned < 200 and level == 16:
        zombies_spawned += 1
        zombie_choose = randint(0, 1)
        if zombie_choose == 0:
            zombies.append(Zombie("zombie3"))
        else:
            zombies.append(Zombie("zombie4"))

    if stage == "level" and randint(0, 300) == 300 and zombies_spawned < 20 and level == 17:
        zombies_spawned += 1
        zombies.append(Zombie("zombie5"))

    if stage == "level" and randint(0, 30) == 30 and zombies_spawned < 300 and level == 18:
        zombies_spawned += 1
        zombie_choose = randint(0, 2)
        if zombie_choose == 0:
            zombies.append(Zombie("zombie3"))
        else:
            zombies.append(Zombie("zombie4"))

    if stage == "level" and randint(0, 15) == 15 and zombies_spawned < 350 and level == 19:
        zombies_spawned += 1
        zombies.append(Zombie("zombie3"))

    if stage == "level" and zombies_spawned < 1 and level == 20:
        zombies_spawned += 1
        zombies.append(Zombie("zomboss"))

    if stage == "menu":
        screen.fill((0, 0, 0))
        screen.blit(menu_bg, (0, 0))
        screen.blit(font_menu.render("Zombie Wave", True, (255, 255, 255)), (182.5, 50))
        if play_button.draw():
            stage = "level_selection"
        if shop_button.draw():
            stage = "shop"
            if music_on == 1:
                shop_music.play(-1)
        if settings_button.draw():
            stage = "settings"

    if stage == 'ending':
        screen.fill((0, 0, 0))
        screen.blit(end_screen, (0, 0))
        if back_button.draw():
            stage = "menu"
    if stage == "settings":
        screen.fill((0, 0, 0))
        screen.blit(menu_bg, (0, 0))
        screen.blit(font_menu.render("Настройки", True, (255, 255, 255)), (232.5, 20))
        screen.blit(font.render("Уровень", True, (255, 255, 255)), (15, 190))
        screen.blit(font.render("Громкости", True, (255, 255, 255)), (10, 220))
        pygame.draw.rect(screen, (192, 192, 192), (55, 250, 7, 250))
        slider.draw()
        volume = int(100 - ((slider.rect.y - 250) / (480 - 250) * 100))
        screen.blit(font_menu.render(str(volume), True, (255, 255, 255)), (100, 320))
        menu_music.set_volume(volume * 0.01)
        level_music.set_volume(volume * 0.01)
        shop_music.set_volume(volume * 0.01)
        nope.set_volume(volume * 0.01)
        win_sound.set_volume(volume * 0.01)
        chaching.set_volume(volume * 0.01)
        lose.set_volume(volume * 0.01)
        airplane_sound.set_volume(volume * 0.01)
        explosion_sound.set_volume(volume * 0.01)
        mine_explosion_sound.set_volume(volume * 0.01)
        gunshot.set_volume(volume * 0.001)
        reload.set_volume(volume * 0.01)
        mine_explosion_sound.set_volume(volume * 0.01)
        final_level_music.set_volume(volume * 0.01)
        level_music2.set_volume(volume * 0.01)
        level_music_loc2.set_volume(volume * 0.01)
        win_sound2.set_volume(volume * 0.01)
        final_level_music2.set_volume(volume * 0.01)

        screen.blit(font_menu.render("Музыка", True, (255, 255, 255)), (570, 100))
        if checkbox_music_button.draw():
            if music_on == 1:
                music_on = 0
                checkbox_music_button.change_image(checkbox_empty)
                menu_music.stop()
            elif music_on == 0:
                music_on = 1
                checkbox_music_button.change_image(checkbox_filled)
                menu_music.play(-1)

        screen.blit(font_menu.render("SFX", True, (255, 255, 255)), (570, 190))
        if checkbox_sfx_button.draw():
            if sfx_on == 1:
                sfx_on = 0
                checkbox_sfx_button.change_image(checkbox_empty)
            elif sfx_on == 0:
                sfx_on = 1
                checkbox_sfx_button.change_image(checkbox_filled)

        if back_button.draw():
            stage = "menu"

    if stage == "shop":
        screen.fill((0, 0, 0))
        screen.blit(shop_bg, (0, 0))
        text = font.render(f"Монет: {coins}", True, (255, 255, 255))
        screen.blit(text, (900 - text.get_size()[0], 5))
        menu_music.stop()

        if back_button.draw():
            stage = "menu"
            shop_music.stop()
            if music_on == 1:
                menu_music.play(-1)

        if back_button2.draw():
            item_number -= 1

        if item_number == 1:
            screen.blit(airplane_summon, (600, 120))
            screen.blit(font.render("Пульт от бомбы", True, (255, 255, 255)), (555, 370))
            screen.blit(font.render("200 монет", True, (255, 255, 255)), (590, 400))
            screen.blit(font.render("Вызывает подкрепление в виде", True, (255, 255, 255)), (450, 430))
            screen.blit(font.render("сбрасывания бомбы. Один на уровень.", True, (255, 255, 255)), (400, 460))
            if airplane_summon_bought == 0:
                if buy_button.draw():
                    if coins >= 200:
                        airplane_summon_bought = 1
                        coins -= 200
                        if sfx_on == 1:
                            chaching.play()
                    else:
                        if sfx_on == 1:
                            pygame.mixer.find_channel(True).play(nope)
            else:
                screen.blit(font.render("Куплено!", True, (255, 255, 255)), (670, 520))

        if item_number == 2:
            screen.blit(robot, (590, 150))
            if robot_bought == 0:
                screen.blit(font.render("Робот-помощник", True, (255, 255, 255)), (570, 370))
                screen.blit(font.render("150 монет", True, (255, 255, 255)), (590, 400))
                screen.blit(font.render("Автоматически наводится и", True, (255, 255, 255)), (500, 430))
                screen.blit(font.render("убивает зомби.", True, (255, 255, 255)), (570, 460))
            elif robot_bought == 1:
                screen.blit(font.render("Улучшение робота", True, (255, 255, 255)), (570, 370))
                screen.blit(font.render(f"{robot_upgrade_price} монет", True, (255, 255, 255)), (590, 400))
                screen.blit(font.render("Улучшение урона от пуль", True, (255, 255, 255)), (500, 430))
                screen.blit(font.render("робота.", True, (255, 255, 255)), (570, 460))
            if robot_bought == 0:
                if buy_button.draw():
                    if coins >= 150:
                        robot_bought = 1
                        coins -= 150
                        if sfx_on == 1:
                            chaching.play()
                    else:
                        if sfx_on == 1:
                            pygame.mixer.find_channel(True).play(nope)
            else:
                if buy_button.draw():
                    if coins >= robot_upgrade_price:
                        robot_damage *= 1.75
                        coins -= robot_upgrade_price
                        robot_upgrade_price *= 2
                        if sfx_on == 1:
                            chaching.play()
                    else:
                        if sfx_on == 1:
                            pygame.mixer.find_channel(True).play(nope)

        if item_number == 3:
            screen.blit(mine_shop, (530, 50))
            screen.blit(font.render("Мины", True, (255, 255, 255)), (640, 370))
            screen.blit(font.render("300 монет", True, (255, 255, 255)), (620, 400))
            screen.blit(font.render("Даётся 10 на уровень. Разместите", True, (255, 255, 255)), (480, 430))
            screen.blit(font.render("их с помощью курсора.", True, (255, 255, 255)), (530, 460))
            if mine_bought == 0:
                if buy_button.draw():
                    if coins >= 300:
                        mine_bought = 1
                        coins -= 300
                        if sfx_on == 1:
                            chaching.play()
                    else:
                        if sfx_on == 1:
                            pygame.mixer.find_channel(True).play(nope)
            else:
                screen.blit(font.render("Куплено!", True, (255, 255, 255)), (670, 520))

        if item_number == 4:
            screen.blit(shop_barricade, (650, 50))
            if barricades_bought == 0:
                screen.blit(font.render("Баррикада I", True, (255, 255, 255)), (600, 370))
                screen.blit(font.render("100 монет", True, (255, 255, 255)), (610, 400))
                screen.blit(font.render("Преграда для зомби.", True, (255, 255, 255)), (550, 430))
            elif barricades_bought == 1:
                screen.blit(font.render("Баррикада II", True, (255, 255, 255)), (600, 370))
                screen.blit(font.render("200 монет", True, (255, 255, 255)), (610, 400))
                screen.blit(font.render("Преграда для зомби.", True, (255, 255, 255)), (550, 430))
            elif barricades_bought >= 2:
                screen.blit(font.render("Баррикада III", True, (255, 255, 255)), (600, 370))
                screen.blit(font.render("300 монет", True, (255, 255, 255)), (610, 400))
                screen.blit(font.render("Преграда для зомби.", True, (255, 255, 255)), (550, 430))
            if barricades_bought != 3:
                if buy_button.draw():
                    if barricades_bought == 0:
                        if coins >= 100:
                            barricades_bought += 1
                            coins -= 100
                            if sfx_on == 1:
                                chaching.play()
                        else:
                            if sfx_on == 1:
                                pygame.mixer.find_channel(True).play(nope)
                    elif barricades_bought == 1:
                        if coins >= 200:
                            barricades_bought += 1
                            coins -= 200
                            if sfx_on == 1:
                                chaching.play()
                        else:
                            if sfx_on == 1:
                                pygame.mixer.find_channel(True).play(nope)
                    elif barricades_bought == 2:
                        if coins >= 300:
                            barricades_bought += 1
                            coins -= 300
                            if sfx_on == 1:
                                chaching.play()
                        else:
                            if sfx_on == 1:
                                pygame.mixer.find_channel(True).play(nope)
            else:
                screen.blit(font.render("Куплено!", True, (255, 255, 255)), (670, 520))

        if item_number == 0:
            screen.blit(m4, (500, 250))
            screen.blit(font.render("Улучшение оружия", True, (255, 255, 255)), (555, 370))
            screen.blit(font.render(f"{upgrade_gun_price} монет", True, (255, 255, 255)), (590, 400))
            screen.blit(font.render("Повышает урон и обойму оружия.", True, (255, 255, 255)), (450, 430))
            if buy_button.draw():
                if coins >= upgrade_gun_price:
                    damage += 1
                    coins -= upgrade_gun_price
                    upgrade_gun_price *= 2
                    clip += 5
                    if sfx_on == 1:
                        chaching.play()
                else:
                    if sfx_on == 1:
                        pygame.mixer.find_channel(True).play(nope)

        if item_number == -1:
            item_number = 4
        elif item_number == 5:
            item_number = 0

        if back_button3.draw():
            item_number += 1

    if stage == "level_selection":
        screen.fill((0, 0, 0))
        if tutorial_watched == 0:
            screen.blit(tutorial_screen, (0, 0))
        else:
            screen.blit(menu_bg, (0, 0))
            screen.blit(font_menu.render("Выберите уровень", True, (255, 255, 255)), (67.5, 20))

            if max_level_completed == 0:
                second_level.set_alpha(130)
                third_level.set_alpha(130)
                fourth_level.set_alpha(130)
                fifth_level.set_alpha(130)
                sixth_level.set_alpha(130)
                seventh_level.set_alpha(130)
                eighth_level.set_alpha(130)
                ninth_level.set_alpha(130)
                tenth_level.set_alpha(130)
                next_pic.set_alpha(130)

            if max_level_completed == 1:
                second_level.set_alpha(255)
                third_level.set_alpha(130)
                fourth_level.set_alpha(130)
                fifth_level.set_alpha(130)
                sixth_level.set_alpha(130)
                seventh_level.set_alpha(130)
                eighth_level.set_alpha(130)
                ninth_level.set_alpha(130)
                tenth_level.set_alpha(130)
                next_pic.set_alpha(130)

            if max_level_completed == 2:
                second_level.set_alpha(255)
                third_level.set_alpha(255)
                fourth_level.set_alpha(130)
                fifth_level.set_alpha(130)
                sixth_level.set_alpha(130)
                seventh_level.set_alpha(130)
                eighth_level.set_alpha(130)
                ninth_level.set_alpha(130)
                tenth_level.set_alpha(130)
                next_pic.set_alpha(130)

            if max_level_completed == 3:
                second_level.set_alpha(255)
                third_level.set_alpha(255)
                fourth_level.set_alpha(255)
                fifth_level.set_alpha(130)
                sixth_level.set_alpha(130)
                seventh_level.set_alpha(130)
                eighth_level.set_alpha(130)
                ninth_level.set_alpha(130)
                tenth_level.set_alpha(130)
                next_pic.set_alpha(130)

            if max_level_completed == 4:
                second_level.set_alpha(255)
                third_level.set_alpha(255)
                fourth_level.set_alpha(255)
                fifth_level.set_alpha(255)
                sixth_level.set_alpha(130)
                seventh_level.set_alpha(130)
                eighth_level.set_alpha(130)
                ninth_level.set_alpha(130)
                tenth_level.set_alpha(130)
                next_pic.set_alpha(130)

            if max_level_completed == 5:
                second_level.set_alpha(255)
                third_level.set_alpha(255)
                fourth_level.set_alpha(255)
                fifth_level.set_alpha(255)
                sixth_level.set_alpha(255)
                seventh_level.set_alpha(130)
                eighth_level.set_alpha(130)
                ninth_level.set_alpha(130)
                tenth_level.set_alpha(130)
                next_pic.set_alpha(130)

            if max_level_completed == 6:
                second_level.set_alpha(255)
                third_level.set_alpha(255)
                fourth_level.set_alpha(255)
                fifth_level.set_alpha(255)
                sixth_level.set_alpha(255)
                seventh_level.set_alpha(255)
                eighth_level.set_alpha(130)
                ninth_level.set_alpha(130)
                next_pic.set_alpha(130)
                tenth_level.set_alpha(130)

            if max_level_completed == 7:
                second_level.set_alpha(255)
                third_level.set_alpha(255)
                fourth_level.set_alpha(255)
                fifth_level.set_alpha(255)
                sixth_level.set_alpha(255)
                seventh_level.set_alpha(255)
                eighth_level.set_alpha(255)
                ninth_level.set_alpha(130)
                tenth_level.set_alpha(130)
                next_pic.set_alpha(130)

            if max_level_completed == 8:
                second_level.set_alpha(255)
                third_level.set_alpha(255)
                fourth_level.set_alpha(255)
                fifth_level.set_alpha(255)
                sixth_level.set_alpha(255)
                seventh_level.set_alpha(255)
                eighth_level.set_alpha(255)
                ninth_level.set_alpha(255)
                tenth_level.set_alpha(130)
                next_pic.set_alpha(130)

            if max_level_completed == 9:
                second_level.set_alpha(255)
                third_level.set_alpha(255)
                fourth_level.set_alpha(255)
                fifth_level.set_alpha(255)
                sixth_level.set_alpha(255)
                seventh_level.set_alpha(255)
                eighth_level.set_alpha(255)
                ninth_level.set_alpha(255)
                tenth_level.set_alpha(255)
                next_pic.set_alpha(130)

            if max_level_completed == 10:
                second_level.set_alpha(255)
                third_level.set_alpha(255)
                fourth_level.set_alpha(255)
                fifth_level.set_alpha(255)
                sixth_level.set_alpha(255)
                seventh_level.set_alpha(255)
                eighth_level.set_alpha(255)
                ninth_level.set_alpha(255)
                tenth_level.set_alpha(255)
                next_pic.set_alpha(130)

            if loc == 0:
                back_button.change_cords(20, 500)

                if back_button.draw():
                    stage = "menu"
                    back_button.change_cords(20, 20)

                if first_level_button.draw():
                    start_level(1, 30)

                if second_level_button.draw():
                    if max_level_completed > 0:
                        start_level(2, 60)
                    else:
                        if sfx_on == 1:
                            pygame.mixer.find_channel(True).play(nope)

                if third_level_button.draw():
                    if max_level_completed > 1:
                        start_level(3, 80)
                    else:
                        if sfx_on == 1:
                            pygame.mixer.find_channel(True).play(nope)

                if fourth_level_button.draw():
                    if max_level_completed > 2:
                        start_level(4, 90)
                    else:
                        if sfx_on == 1:
                            pygame.mixer.find_channel(True).play(nope)

                if fifth_level_button.draw():
                    if max_level_completed > 3:
                        start_level(5, 120)
                    else:
                        if sfx_on == 1:
                            pygame.mixer.find_channel(True).play(nope)

                if sixth_level_button.draw():
                    if max_level_completed > 4:
                        start_level(6, 150)
                    else:
                        if sfx_on == 1:
                            pygame.mixer.find_channel(True).play(nope)

                if seventh_level_button.draw() and max_level_completed > 5:
                    if max_level_completed > 5:
                        start_level(7, 200)
                    else:
                        if sfx_on == 1:
                            pygame.mixer.find_channel(True).play(nope)

                if eighth_level_button.draw():
                    if max_level_completed > 6:
                        start_level(8, 180)
                    else:
                        if sfx_on == 1:
                            pygame.mixer.find_channel(True).play(nope)

                if ninth_level_button.draw():
                    if max_level_completed > 7:
                        start_level(9, 200)
                    else:
                        if sfx_on == 1:
                            pygame.mixer.find_channel(True).play(nope)

                if tenth_level_button.draw():
                    if max_level_completed > 8:
                        menu_music.stop()
                        if music_on == 1:
                            level_music2.play(-1)
                        sl_hp = 10
                        sl_x3 = 10
                        sl_y1 = 300
                        back_button.change_cords(20, 20)
                        stage = "special_level"
                        sl_timer = pygame.time.get_ticks()
                        get_money = 200
                        level = 10
                    else:
                        pygame.mixer.find_channel(True).play(nope)

                if infinity_mode_button.draw():
                    start_level(-1, None)
                    infinity_mode_timer = pygame.time.get_ticks()

                if next_loc_button.draw():
                    if max_level_completed > 9:
                        loc = 1
                    else:
                        if sfx_on == 1:
                            pygame.mixer.find_channel(True).play(nope)

            elif loc == 1:

                if max_level_completed == 10:
                    eleventh_level.set_alpha(255)
                    twelfth_level.set_alpha(130)
                    thirteenth_level.set_alpha(130)
                    fourteenth_level.set_alpha(130)
                    fifteenth_level.set_alpha(130)
                    sixteenth_level.set_alpha(130)
                    seventeenth_level.set_alpha(130)
                    eighteenth_level.set_alpha(130)
                    nineteenth_level.set_alpha(130)
                    twentieth_level.set_alpha(130)

                if max_level_completed == 11:
                    eleventh_level.set_alpha(255)
                    twelfth_level.set_alpha(255)
                    thirteenth_level.set_alpha(130)
                    fourteenth_level.set_alpha(130)
                    fifteenth_level.set_alpha(130)
                    sixteenth_level.set_alpha(130)
                    seventeenth_level.set_alpha(130)
                    eighteenth_level.set_alpha(130)
                    nineteenth_level.set_alpha(130)
                    twentieth_level.set_alpha(130)

                if max_level_completed == 12:
                    eleventh_level.set_alpha(255)
                    twelfth_level.set_alpha(255)
                    thirteenth_level.set_alpha(255)
                    fourteenth_level.set_alpha(130)
                    fifteenth_level.set_alpha(130)
                    sixteenth_level.set_alpha(130)
                    seventeenth_level.set_alpha(130)
                    eighteenth_level.set_alpha(130)
                    nineteenth_level.set_alpha(130)
                    twentieth_level.set_alpha(130)

                if max_level_completed == 13:
                    eleventh_level.set_alpha(255)
                    twelfth_level.set_alpha(255)
                    thirteenth_level.set_alpha(255)
                    fourteenth_level.set_alpha(255)
                    fifteenth_level.set_alpha(130)
                    sixteenth_level.set_alpha(130)
                    seventeenth_level.set_alpha(130)
                    eighteenth_level.set_alpha(130)
                    nineteenth_level.set_alpha(130)
                    twentieth_level.set_alpha(130)

                if max_level_completed == 14:
                    eleventh_level.set_alpha(255)
                    twelfth_level.set_alpha(255)
                    thirteenth_level.set_alpha(255)
                    fourteenth_level.set_alpha(255)
                    fifteenth_level.set_alpha(255)
                    sixteenth_level.set_alpha(130)
                    seventeenth_level.set_alpha(130)
                    eighteenth_level.set_alpha(130)
                    nineteenth_level.set_alpha(130)
                    twentieth_level.set_alpha(130)

                if max_level_completed == 15:
                    eleventh_level.set_alpha(255)
                    twelfth_level.set_alpha(255)
                    thirteenth_level.set_alpha(255)
                    fourteenth_level.set_alpha(255)
                    fifteenth_level.set_alpha(255)
                    sixteenth_level.set_alpha(255)
                    seventeenth_level.set_alpha(130)
                    eighteenth_level.set_alpha(130)
                    nineteenth_level.set_alpha(130)
                    twentieth_level.set_alpha(130)

                if max_level_completed == 16:
                    eleventh_level.set_alpha(255)
                    twelfth_level.set_alpha(255)
                    thirteenth_level.set_alpha(255)
                    fourteenth_level.set_alpha(255)
                    fifteenth_level.set_alpha(255)
                    sixteenth_level.set_alpha(255)
                    seventeenth_level.set_alpha(255)
                    eighteenth_level.set_alpha(130)
                    nineteenth_level.set_alpha(130)
                    twentieth_level.set_alpha(130)

                if max_level_completed == 17:
                    eleventh_level.set_alpha(255)
                    twelfth_level.set_alpha(255)
                    thirteenth_level.set_alpha(255)
                    fourteenth_level.set_alpha(255)
                    fifteenth_level.set_alpha(255)
                    sixteenth_level.set_alpha(255)
                    seventeenth_level.set_alpha(255)
                    eighteenth_level.set_alpha(255)
                    nineteenth_level.set_alpha(130)
                    twentieth_level.set_alpha(130)

                if max_level_completed == 18:
                    eleventh_level.set_alpha(255)
                    twelfth_level.set_alpha(255)
                    thirteenth_level.set_alpha(255)
                    fourteenth_level.set_alpha(255)
                    fifteenth_level.set_alpha(255)
                    sixteenth_level.set_alpha(255)
                    seventeenth_level.set_alpha(255)
                    eighteenth_level.set_alpha(255)
                    nineteenth_level.set_alpha(255)
                    twentieth_level.set_alpha(130)

                if max_level_completed >= 19:
                    eleventh_level.set_alpha(255)
                    twelfth_level.set_alpha(255)
                    thirteenth_level.set_alpha(255)
                    fourteenth_level.set_alpha(255)
                    fifteenth_level.set_alpha(255)
                    sixteenth_level.set_alpha(255)
                    seventeenth_level.set_alpha(255)
                    eighteenth_level.set_alpha(255)
                    nineteenth_level.set_alpha(255)
                    twentieth_level.set_alpha(255)

                if eleventh_level_button.draw():
                    if max_level_completed > 9:
                        start_level(11, 250)
                    else:
                        pygame.mixer.find_channel(True).play(nope)

                if twelfth_level_button.draw():
                    if max_level_completed > 10:
                        start_level(12, 300)
                    else:
                        pygame.mixer.find_channel(True).play(nope)

                if thirteenth_level_button.draw():
                    if max_level_completed > 11:
                        start_level(13, 310)
                    else:
                        pygame.mixer.find_channel(True).play(nope)

                if fourteenth_level_button.draw():
                    if max_level_completed > 12:
                        start_level(14, 330)
                    else:
                        pygame.mixer.find_channel(True).play(nope)

                if fifteenth_level_button.draw():
                    if max_level_completed > 13:
                        start_level(15, 350)
                    else:
                        pygame.mixer.find_channel(True).play(nope)

                if sixteenth_level_button.draw():
                    if max_level_completed > 14:
                        start_level(16, 370)
                    else:
                        pygame.mixer.find_channel(True).play(nope)

                if seventeenth_level_button.draw():
                    if max_level_completed > 15:
                        start_level(17, 400)
                    else:
                        pygame.mixer.find_channel(True).play(nope)

                if eighteenth_level_button.draw():
                    if max_level_completed > 16:
                        start_level(18, 420)
                    else:
                        pygame.mixer.find_channel(True).play(nope)

                if nineteenth_level_button.draw():
                    if max_level_completed > 17:
                        start_level(19, 450)
                    else:
                        pygame.mixer.find_channel(True).play(nope)

                if twentieth_level_button.draw():
                    if max_level_completed > 18:
                        start_level(20, 500)
                    else:
                        pygame.mixer.find_channel(True).play(nope)

                back_button.change_cords(20, 500)
                if back_button.draw():
                    loc = 0

    if stage == "special_level" and game_over == 0:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            ctypes.windll.user32.MessageBoxW(0, "Закройте это окно, чтобы продолжить", "Пауза", 0)
        screen.fill((0, 0, 0))
        screen.blit(level_bg, (sl_x1, 0))
        screen.blit(level_bg, (sl_x2, 0))
        if pygame.time.get_ticks() - sl_timer < 40000:
            for i in zombies:
                i.draw()
            if sl_x1 > -880:
                sl_x1 -= 20
            else:
                sl_x1 = 900
            if sl_x2 > -880:
                sl_x2 -= 20
            else:
                sl_x2 = 900
        screen.blit(car, (sl_x3, sl_y1))
        screen.blit(font_menu.render(f"HP: {sl_hp}", True, (255, 0, 0)), (0, 0))
        if randint(0, 50) == 50 and zombies_have < 2:
            zombies_have += 1
            zombies.append(Zombie("zombie_sl"))
        if sl_hp < 1 and game_over == 0:
            game_over = 1
        if pygame.time.get_ticks() - sl_timer > 40000:
            if sl_x3 < 1000:
                sl_x3 += 15
            else:
                if win != 2:
                    win = 2
                    level_music2.stop()
                    if music_on == 1:
                        pygame.mixer.find_channel(True).play(win_sound)
                    coins_count_tick = pygame.time.get_ticks()

    if as_ab_activated == 1 and game_over == 0:
        if x_ab1 < 1000:
            x_ab1 += 10
        else:
            bomb_tick = pygame.time.get_ticks()
            as_ab_activated = 2

    if bomb_tick != 0 and pygame.time.get_ticks() - bomb_tick > 3000 and game_over == 0:
        if y1_ab1 < 300:
            y1_ab1 += 40
        else:
            bomb_tick = 0
            bomb_tick2 = pygame.time.get_ticks()
            if sfx_on == 1:
                pygame.mixer.find_channel(True).play(explosion_sound)
            bomb_is_invisible = 1
            explosion_activated = 1

    if bomb_tick2 != 0 and pygame.time.get_ticks() - bomb_tick2 > 3000:
        if explosion_alpha > 1:
            explosion_alpha -= 5
            explosion.set_alpha(explosion_alpha)
        else:
            bomb_tick2 = 0
            explosion_activated = 0
            x1_ab1 = 425
            y1_ab1 = -100
            x_ab1 = -300
            y_ab1 = 150
            bomb_is_invisible = 0
            explosion_alpha = 255
            explosion.set_alpha(255)

    if type(target) != int:
        if bullet_robot_tick != 0 and pygame.time.get_ticks() - bullet_robot_tick > 100:
            bullet_robot_tick = pygame.time.get_ticks()
            bullets.append(Bullet(robot_y, robot_damage))
            if sfx_on == 1:
                pygame.mixer.find_channel(True).play(gunshot)
        elif target.hp < 1:
            bullet_robot_tick = 0

    if stage == "level" and game_over == 0:

        if win == 0 and game_over == 0:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                if y > 1:
                    y -= 7

            if keys[pygame.K_s]:
                if y < 400:
                    y += 7

            if keys[pygame.K_DOWN]:
                if y < 400:
                    y += 7

            if keys[pygame.K_UP]:
                if y > 1:
                    y -= 7

            if keys[pygame.K_1] and as_ab_activated == 0 and airplane_summon_bought == 1 and win == 0 and \
                    game_over == 0:
                as_ab_activated = 1
                if sfx_on:
                    pygame.mixer.find_channel(True).play(airplane_sound)

            if keys[pygame.K_2] and mine_placing == 0 and mine_bought == 1 and win == 0 and \
                    game_over == 0 and mines_have > 0:
                mine_placing = 1

            if keys[pygame.K_ESCAPE] and mine_placing == 1:
                mine_placing = 0
            elif mine_placing == 0 and keys[pygame.K_ESCAPE]:
                ctypes.windll.user32.MessageBoxW(0, "Закройте это окно, чтобы продолжить", "Пауза", 0)

        screen.fill((0, 0, 0))
        if loc == 0:
            screen.blit(level_bg, (0, 0))
        elif loc == 1:
            screen.blit(level_bg2, (0, 0))
        pygame.draw.rect(screen, "red", (155, 115, 10, 485))

        for i in bullets:
            i.draw()

        if win == 0:
            for j in zombies:
                j.draw()

        for n in mines:
            n.draw()

        if robot_bought == 1:
            screen.blit(robot, (robot_x, robot_y))
            if len(zombies) > 0 and bullet_robot_tick == 0:
                target = zombies[0]
                if round(zombies[0].y / 5) * 5 != robot_y:
                    if zombies[0].y < robot_y:
                        robot_y -= 5
                    else:
                        robot_y += 5
                else:
                    if bullet_robot_tick == 0:
                        bullet_robot_tick = pygame.time.get_ticks()

        screen.blit(player, (x, y))

        if airplane_summon_bought == 1 and as_ab_activated == 0:
            screen.blit(airplane_summon_ab, (10, 495))

        if mine_bought == 1 and mines_have > 0:
            screen.blit(mine_ab, (130, 495))

        text2 = font.render(f"{bullets_have}/{clip}", True, (0, 0, 0))
        screen.blit(text2, (900 - text2.get_size()[0], 20))
        screen.blit(airplane_shadow, (x_ab1, y_ab1))

        if bomb_is_invisible == 0:
            screen.blit(bomb, (x1_ab1, y1_ab1))

        if barricades_bought == 1:
            if barricade1_hp > 0:
                screen.blit(barricade, (300, 115))
                barricade1_rect = pygame.Rect(300, 115, 50, 600)
            else:
                barricade1_rect = pygame.Rect(0, 0, 0, 0)

        if barricades_bought == 2:
            if barricade1_hp > 0:
                screen.blit(barricade, (300, 115))
                barricade1_rect = pygame.Rect(300, 115, 50, 600)
            else:
                barricade1_rect = pygame.Rect(0, 0, 0, 0)
            if barricade2_hp > 0:
                screen.blit(barricade, (500, 115))
                barricade2_rect = pygame.Rect(500, 115, 50, 600)
            else:
                barricade2_rect = pygame.Rect(0, 0, 0, 0)

        if barricades_bought == 3:
            if barricade1_hp > 0:
                screen.blit(barricade, (300, 115))
                barricade1_rect = pygame.Rect(300, 115, 50, 600)
            else:
                barricade1_rect = pygame.Rect(0, 0, 0, 0)
            if barricade2_hp > 0:
                screen.blit(barricade, (500, 115))
                barricade2_rect = pygame.Rect(500, 115, 50, 600)
            else:
                barricade2_rect = pygame.Rect(0, 0, 0, 0)
            if barricade3_hp > 0:
                screen.blit(barricade, (700, 115))
                barricade3_rect = pygame.Rect(700, 115, 50, 600)
            else:
                barricade3_rect = pygame.Rect(0, 0, 0, 0)

        if explosion_activated == 1:
            screen.blit(explosion, (-50, 0))
            for k in zombies:
                if bomb_rect.colliderect(k.rect):
                    if k.type_of_zombie == "zomboss" and zomboss_airplane_damaged == 0:
                        zomboss_airplane_damaged = 1
                        k.get_damage(200)
                    elif k.type_of_zombie != 'zomboss':
                        k.get_damage(200)

        if explosion_activated3 == 1:
            screen.blit(explosion, (70, 0))

        if pygame.time.get_ticks() - explosion_timer > 3000 and explosion_timer != 0:
            if explosion_alpha > 0:
                explosion_alpha -= 5
                explosion.set_alpha(explosion_alpha)
            else:
                explosion_activated3 = 0
                explosion_timer = 0

        if mine_placing == 1:
            screen.blit(transparent_cube, (0, 0))
            screen.blit(mine, (pygame.mouse.get_pos()[0] - 23, pygame.mouse.get_pos()[1] - 20))

    if (stage == "level" or stage == "special_level") and game_over != 0:
        bullet_robot_tick = 0
        mine_placing = 0
        level_music2.stop()
        level_music_loc2.stop()
        final_level_music.stop()
        final_level_music2.stop()
        target = 0
        explosion_activated2 = 0
        while len(zombies) > 0:
            del zombies[0]
        while len(bullets) > 0:
            del bullets[0]
        while len(mines) > 0:
            del mines[0]
        screen.fill((255, 255, 255))
        reload.stop()
        gunshot.stop()
        screen.blit(font_menu.render("Game over", True, (0, 0, 0)), (200, 200))
        if infinity_mode_timer != 0:
            screen.blit(font.render(f"Получено монет: {zombies_killed * 2}", True, (0, 0, 0)), (300, 280))
            screen.blit(font.render(f"Стало монет: {coins + zombies_killed * 2}", True, (0, 0, 0)), (300, 310))
        back_button.change_cords(20, 20)
        if back_button.draw():
            if infinity_mode_timer != 0:
                coins += zombies_killed * 2
            infinity_mode_timer = 0
            og_zombie_chance = 0.01
            zomboss_airplane_damaged = 0
            con_zombie_chance = 0.001
            bucket_zombie_chance = 0.0001
            football_zombie_chance = 0.00001
            gargantua_zombie_chance = 0.000001
            game_over = 0
            zombies_killed = 0
            zombies_spawned = 0
            bullets_have = clip
            x = 50
            y = 300
            shooting = 0
            as_ab_activated = 0
            stage = "level_selection"
            if music_on == 1:
                menu_music.play(-1)
            lose.stop()

    if (stage == "level" or stage == "special_level") and game_over == 1:
        game_over = 2
        level_music.stop()
        if music_on == 1:
            pygame.mixer.find_channel(True).play(lose)

    if shooting == 1 and reload_tick_activated == 0 and win == 0 and game_over == 0:
        if pygame.time.get_ticks() - bullet_tick > 100 and bullets_have > 0 and win == 0 and game_over == 0:
            bullets.append(Bullet(y + 80, damage))
            if sfx_on == 1:
                pygame.mixer.find_channel(True).play(gunshot)
            bullet_tick = pygame.time.get_ticks()
            bullets_have -= 1

    if pygame.time.get_ticks() - reload_tick > 3000 and reload_tick_activated:
        bullets_have = clip
        reload_tick_activated = False

    if win_tick != 0 and win == 1 and pygame.time.get_ticks() - win_tick > 3000:
        win = 2
        if music_on == 1:
            if level != 20:
                pygame.mixer.find_channel(True).play(win_sound)
            else:
                pygame.mixer.find_channel(True).play(win_sound2)
        coins_count_tick = pygame.time.get_ticks()

    if win == 2:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            coins += get_money
            win_sound.stop()
            win_sound2.stop()
            chaching.stop()
            zomboss_airplane_damaged = 0
            while len(mines) > 0:
                del mines[0]
            while len(zombies) > 0:
                del zombies[0]
            win = 0
            after_win_tick = 0
            zombies_spawned = 0
            zombies_killed = 0
            bullets_have = clip
            y = 300
            x = 50
            explosion_activated2 = 0
            as_ab_activated = 0
            coins_count_tick = 0
            x_text = -300
            if level > max_level_completed:
                max_level_completed = level
            if level != 20:
                stage = "level_selection"
            else:
                stage = "ending"
            if music_on == 1:
                menu_music.play(-1)
        screen.blit(font_menu.render("Победа", True, (255, 255, 255)), (x_text, 100))
        screen.blit(font.render(f"Монет заработано: {get_money}", True, (255, 255, 255)), (x_text, 300))
        screen.blit(font.render(f"Всего монет: {coins}", True, (255, 255, 255)), (x_text, 320))
        screen.blit(font.render("Нажмите S чтобы пропустить", True, (255, 255, 255)), (260, 500))
        if x_text < 300:
            x_text += 10

    if coins_count_tick != 0 and pygame.time.get_ticks() - coins_count_tick > 8000:
        if get_money > 0:
            get_money -= 1
            coins += 1
        else:
            if sfx_on == 1:
                chaching.play()
            coins_count_tick = 0
            after_win_tick = pygame.time.get_ticks()

    if after_win_tick != 0 and pygame.time.get_ticks() - after_win_tick > 4500 and win == 2 and \
            (stage == "level" or stage == "special_level"):
        while len(mines) > 0:
            del mines[0]
        while len(zombies) > 0:
            del zombies[0]
        win = 0
        explosion_activated2 = 0
        after_win_tick = 0
        zomboss_airplane_damaged = 0
        zombies_spawned = 0
        zombies_killed = 0
        bullets_have = clip
        y = 300
        x = 50
        as_ab_activated = 0
        x_text = -300
        if level > max_level_completed:
            max_level_completed = level
        if level != 20:
            stage = "level_selection"
        else:
            stage = "ending"
        if music_on == 1:
            menu_music.play(-1)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and stage == "level" and mine_placing == 0:
            shooting = 1

        if event.type == pygame.KEYDOWN and event.key == pygame.K_w and stage == "special_level":
            if sl_y1 == 475:
                sl_y1 = 300
            elif sl_y1 == 300:
                sl_y1 = 100

        if event.type == pygame.KEYDOWN and event.key == pygame.K_s and stage == "special_level":
            if sl_y1 == 100:
                sl_y1 = 300
            elif sl_y1 == 300:
                sl_y1 = 475

        if event.type == pygame.MOUSEBUTTONDOWN and stage == "level_selection" and tutorial_watched == 0:
            tutorial_watched = 1

        if event.type == pygame.MOUSEBUTTONDOWN and stage == "level" and mine_placing == 1:
            mines.append(Mine())
            mine_placing = 0
            mines_have -= 1

        if event.type == pygame.MOUSEBUTTONUP:
            shooting = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            if slider.rect.collidepoint(event.pos) and stage == "settings":
                slider.change_val_clicked(True)
        if event.type == pygame.MOUSEBUTTONUP:
            slider.change_val_clicked(False)

        if slider.get_val_clicked():
            slider.rect.y = event.pos[1] - slider.rect.height // 2
            if slider.rect.y < 250:
                slider.rect.y = 250
            elif slider.rect.y > 500 - slider.rect.height:
                slider.rect.y = 500 - slider.rect.height

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r and stage == "level" and not reload_tick_activated \
                and win == 0 and game_over == 0:
            reload_tick = pygame.time.get_ticks()
            reload_tick_activated = True
            if sfx_on == 1:
                pygame.mixer.find_channel(True).play(reload)

    clock.tick(60)
    pygame.display.update()

pygame.quit()
file = open("progress.txt", "w")
file.write(f"""{coins}
{airplane_summon_bought}
{damage}
{upgrade_gun_price}
{clip}
{robot_bought}
{mine_bought}
{barricades_bought}
{robot_damage}
{robot_upgrade_price}
{max_level_completed}
{volume}
{slider.rect.y}
{music_on}
{sfx_on}
{tutorial_watched}""")
file.close()
