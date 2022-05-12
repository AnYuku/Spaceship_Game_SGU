# Thư viện ========================================================================================================================================================#
import pygame as pg
import os
import sys
from button import Button
pg.init()
pg.font.init()
pg.mixer.init()
#==================================================================================================================================================================#

# Cac chuan khung hinh 
# 1280 x 720
# 1920 x 1080
# 1440 x 900

# Setting cửa sổ:
#==================================================================================================================================================================#
## Chiều dài
SCREEN_WIDTH = 1200
## Chiều rộng
SCREEN_HEIGHT = 700
#==================================================================================================================================================================#

# Setting colour:
#==================================================================================================================================================================#
color_black =(0, 0, 0)
color_white = (255, 255, 255)
color_red = ((255, 0 ,0))
color_lime = (0,255,0)
color_blue = (0,0,255)
color_cyan = (0,255,255)
color_yellow = (255,255,0)
color_magenta = (255,0,255)
color_purple = (128,0,128)
#==================================================================================================================================================================#

# Setting phi thuyền:
#==================================================================================================================================================================#
# Kích thước phi thuyền
space_ship_WIDTH = 55
space_ship_HEIGHT = 40
# Tốc độ phi thuyền
SPEED_SPACESHIP = 4
#
MAX_HEALTH = 10
# Số lượng đạn
MAX_BULLET = 3
# Tốc độ đạn
SPEED_BULLET = 9
#==================================================================================================================================================================#


# Setting khung hình chạy bao nhiêu frame:
#==================================================================================================================================================================#
clock = pg.time.Clock()
FPS = 60 # Frame Per Second

WINDOW = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("SPACESHIP")
#==================================================================================================================================================================#


# Load image:
#==================================================================================================================================================================#

# Background #
#-------------------------------------------------------------------------------------------------------------------#
background = pg.transform.scale(
    pg.image.load(
        os.path.join('Put files image here', 'space.png')), (SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND_MENU = pg.transform.scale(
    pg.image.load(
        os.path.join('Put files image here', 'menu.jpg')), (SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND_PLAY = pg.transform.scale(
    pg.image.load(
        os.path.join('Put files image here', 'Play Rect.png')), (200, 80))

BACKGROUND_SETTING = pg.transform.scale(
    pg.image.load(
            os.path.join('Put files image here', 'Setting Rect.png')), (300, 80))

BACKGROUND_QUIT = pg.transform.scale(
    pg.image.load(
            os.path.join('Put files image here', 'Quit Rect.png')), (180, 80))

BACKGROUND_VICTORY_MENU = pg.transform.scale(
    pg.image.load(
        os.path.join('Put files image here', 'victory.png')), (SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND_BACK = pg.transform.scale(
    pg.image.load(
            os.path.join('Put files image here', 'Setting Rect.png')), (450, 80))

BACKGROUND_TRY_AGAIN = pg.transform.scale(
    pg.image.load(
            os.path.join('Put files image here', 'Setting Rect.png')), (300, 80))

BACKGROUND_PLAY_MENU = pg.transform.scale(
    pg.image.load(
        os.path.join('Put files image here', 'play menu.png')), (SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND_PASS_5_LEVEL = pg.transform.scale(
    pg.image.load(
        os.path.join('Put files image here', 'Setting Rect.png')), (300, 80))
BACKGROUND_SURVIVAL = pg.transform.scale(
    pg.image.load(
        os.path.join('Put files image here', 'Setting Rect.png')), (300, 80))
BACKGROUND_VS_2_PLAYER = pg.transform.scale(
    pg.image.load(
        os.path.join('Put files image here', 'Setting Rect.png')), (300, 80))
BACKGROUND_PAUSE = pg.transform.scale(
    pg.image.load(
        os.path.join('Put files image here', 'Setting Rect.png')), (100, 40))
#-------------------------------------------------------------------------------------------------------------------#

# Player 1 #
#-------------------------------------------------------------------------------------------------------------------#
yellow_spaceship_image = pg.image.load(
    os.path.join('Put files image here', 'spaceship_yellow.png'))

YELLOW_SPACESHIP = pg.transform.rotate(
    pg.transform.scale(yellow_spaceship_image, (space_ship_WIDTH, space_ship_HEIGHT)), 90)
#-------------------------------------------------------------------------------------------------------------------#

# Player 2 #
#-------------------------------------------------------------------------------------------------------------------#
red_spaceship_image = pg.image.load(
    os.path.join('Put files image here', 'spaceship_red.png'))

RED_SPACESHIP = pg.transform.rotate(
    pg.transform.scale(red_spaceship_image, (space_ship_WIDTH, space_ship_HEIGHT)), 270)
#-------------------------------------------------------------------------------------------------------------------#

# Yellow Bullets
#-------------------------------------------------------------------------------------------------------------------#
yellow_bullets_image = pg.image.load(
    os.path.join('Put files image here', 'bullet_spaceship.png'))
YELLOW_BULLET = pg.transform.scale(yellow_bullets_image, (10, 5))
#-------------------------------------------------------------------------------------------------------------------#

# Red Bullets
#-------------------------------------------------------------------------------------------------------------------#
red_bullets_image = pg.image.load(
    os.path.join('Put files image here', 'bullet_spaceship 1.png'))
RED_BULLET = pg.transform.scale(red_bullets_image, (10, 5))
#-------------------------------------------------------------------------------------------------------------------#

# Khung chữ nhật của ranh giới
#-------------------------------------------------------------------------------------------------------------------#
BORDER = pg.Rect(SCREEN_WIDTH//2 - 5, 0, 10, SCREEN_HEIGHT)
#-------------------------------------------------------------------------------------------------------------------#

# Sound
# Âm thanh đạn khi bắn trúng
BULLET_HIT_SOUND = pg.mixer.Sound(os.path.join('Put files audio here', 'Grenade+1.mp3'))
# Âm thanh đạn khi khai hỏa
BULLET_FIRE_SOUND = pg.mixer.Sound(os.path.join('Put files audio here', 'Gun+Silencer.mp3'))
#
EXPLORE_SPACESHIP_SOUND = pg.mixer.Sound(os.path.join('Put files audio here', 'Explosion_1.mp3'))
#==================================================================================================================================================================#

# Đối tượng phi thuyền vàng và các phương thức của nó --- PLAYER 1
class Spaceship_yellow(pg.sprite.Sprite):
    def __init__ (self, x, y, health):
        pg.sprite.Sprite.__init__(self)
        self.image = YELLOW_SPACESHIP
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.health_max = MAX_HEALTH
        self.health_remainning = health
        self.last_shot = pg.time.get_ticks()
        self.last_burst = pg.time.get_ticks()
        self.mode_shot = 1 # set mode bắn đạn
        self.num_bullet = 0 # set số lượng đạn bắn ban đầu
    def update(self):
        key = pg.key.get_pressed()
        # Set cooldown
        cooldown_bullet = 100 # đơn vị tính là mili giây. 1000 mili giây = 1 giây 
        cooldown_burst = 600
        
        # move
        if key[pg.K_a] and self.rect.left > 0 + 10:
            self.rect.x -= SPEED_SPACESHIP
        if key[pg.K_d] and self.rect.right < SCREEN_WIDTH/2 - 10:
            self.rect.x += SPEED_SPACESHIP
        if key[pg.K_w] and self.rect.top > 0 + 10:
            self.rect.y -= SPEED_SPACESHIP
        if key[pg.K_s] and self.rect.bottom < SCREEN_HEIGHT - 10:
            self.rect.y += SPEED_SPACESHIP   
        # mode
        # Bắn từng viên 1
        if key[pg.K_c]:
            self.mode_shot = 1
        # Bắn 3 viên 1 lúc
        if key[pg.K_v]:
            self.mode_shot = 0
        
        # get time
        time_now = pg.time.get_ticks()
        
        # shot    
        # Bắn 3 viên 1 lúc
        if self.mode_shot == 0:
            cooldown_bullet = 100
            if key[pg.K_SPACE]:
                if time_now - self.last_burst > cooldown_burst:
                    if time_now - self.last_shot > cooldown_bullet:
                        if self.num_bullet < MAX_BULLET:
                            bullet = Bullets_yellow(self.rect.centerx + 20, self.rect.top + 27)
                            bullet_group.add(bullet)
                            BULLET_FIRE_SOUND.play()
                            self.num_bullet += 1
                            self.last_shot = time_now
                        else:
                            self.last_burst = time_now
                else:
                    self.num_bullet = 0
                
                
        # Bắn từng viên 1
        if self.mode_shot == 1:
            cooldown_bullet = 500
            if key[pg.K_SPACE] and time_now - self.last_shot > cooldown_bullet:
                bullet = Bullets_yellow(self.rect.centerx + 20, self.rect.top + 27)
                bullet_group.add(bullet)
                BULLET_FIRE_SOUND.play()
                self.last_shot = time_now
    
    def reset_yellow(self):
        self.health_remainning = self.health_max
        bullet_group.empty()
        self.rect.center = [50, int(SCREEN_HEIGHT / 2)]
                  
    def health_bar(self):
        pos_size_bar_red = (self.rect.left, self.rect.bottom + 10, self.rect.width, 15) 
        pg.draw.rect(WINDOW, color_red, pos_size_bar_red)
        if self.health_remainning > 0:
            ratio_health = (self.health_remainning / self.health_max)
            pos_size_bar_green = (self.rect.left, self.rect.bottom + 10, int(self.rect.width * ratio_health), 15)
            pg.draw.rect(WINDOW, color_lime, pos_size_bar_green)
        if self.health_remainning <= 0:
            EXPLORE_SPACESHIP_SOUND.play()
            self.health_remainning = self.health_max
            bullet_group.empty()
            Spaceship_yellow.reset_yellow(self)
            red_spaceship.reset_red()
            winner_menu("RED WIN")
        
class Bullets_yellow(pg.sprite.Sprite):
    def __init__ (self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = YELLOW_BULLET
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    def update(self):
        self.rect.centerx += SPEED_BULLET
        if self.rect.right > SCREEN_WIDTH:
            self.kill()
        if pg.sprite.spritecollide(self, spaceship_group, False):
            self.kill()
            BULLET_HIT_SOUND.play()
            red_spaceship.health_remainning -= 1

# Đối tượng phi thuyền đỏ và các phương thức của nó --- PLAYER 2
class Spaceship_red(pg.sprite.Sprite):
    def __init__ (self, x, y, health):
        pg.sprite.Sprite.__init__(self)
        self.image = RED_SPACESHIP
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.health_max = health
        self.health_remainning = health
        self.last_shot = pg.time.get_ticks()
        self.last_burst = pg.time.get_ticks()
        self.mode_shot = 1 # set mode bắn đạn
        self.num_bullet = 0 # set số lượng đạn bắn ban đầu
        
    def update(self):
        key = pg.key.get_pressed()
        # Set cooldown
        cooldown_bullet = 100 # đơn vị tính là mili giây. 1000 mili giây = 1 giây 
        cooldown_burst = 600
        
        if key[pg.K_LEFT] and self.rect.left > int(SCREEN_WIDTH/2) + 10:
            self.rect.x -= SPEED_SPACESHIP
        if key[pg.K_RIGHT] and self.rect.right < SCREEN_WIDTH - 10:
            self.rect.x += SPEED_SPACESHIP
        if key[pg.K_UP] and self.rect.top > 0 + 10:
            self.rect.y -= SPEED_SPACESHIP
        if key[pg.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT - 10:
            self.rect.y += SPEED_SPACESHIP           

        # mode
        # Bắn từng viên 1
        if key[pg.K_INSERT]:
            self.mode_shot = 1
        # Bắn 3 viên 1 lúc
        if key[pg.K_DELETE]:
            self.mode_shot = 0
        
        # get time
        time_now = pg.time.get_ticks()
        
        # shot    
        # Bắn 3 viên 1 lúc
        if self.mode_shot == 0:
            cooldown_bullet = 100
            if key[pg.K_RCTRL]:
                if time_now - self.last_burst > cooldown_burst:
                    if time_now - self.last_shot > cooldown_bullet:
                        if self.num_bullet < MAX_BULLET:
                            bullet = Bullets_red(self.rect.centerx - 20, self.rect.top + 27)
                            bullet_group.add(bullet)
                            BULLET_FIRE_SOUND.play()
                            self.num_bullet += 1
                            self.last_shot = time_now
                        else:
                            self.last_burst = time_now
                else:
                    self.num_bullet = 0
                                
        # Bắn từng viên 1
        if self.mode_shot == 1:
            cooldown_bullet = 500
            if key[pg.K_RCTRL] and time_now - self.last_shot > cooldown_bullet:
                bullet = Bullets_red(self.rect.centerx - 20, self.rect.top + 27)
                bullet_group.add(bullet)
                BULLET_FIRE_SOUND.play()
                self.last_shot = time_now
    
    def reset_red(self):
        self.health_remainning = self.health_max
        bullet_group.empty()
        self.rect.center = [SCREEN_WIDTH - 50, int(SCREEN_HEIGHT / 2)]
        
    def health_bar(self):
        pos_size_bar_red = (self.rect.left, self.rect.bottom + 10, self.rect.width, 15) 
        pg.draw.rect(WINDOW, color_red, pos_size_bar_red)
        if self.health_remainning > 0:
            ratio_health = (self.health_remainning / self.health_max)
            pos_size_bar_green = (self.rect.left, self.rect.bottom + 10, int(self.rect.width * ratio_health), 15)
            pg.draw.rect(WINDOW, color_lime, pos_size_bar_green)
        if self.health_remainning <= 0:
            EXPLORE_SPACESHIP_SOUND.play()
            self.health_remainning = self.health_max
            bullet_group.empty()
            Spaceship_red.reset_red(self)
            yellow_spaceship.reset_yellow()
            winner_menu("YELLOW WIN")
            

class Bullets_red(pg.sprite.Sprite):
    def __init__ (self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = RED_BULLET
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    def update(self):
        self.rect.centerx -= SPEED_BULLET
        if self.rect.left <= 0:
            self.kill()
        if pg.sprite.spritecollide(self, spaceship_group, False):
            BULLET_HIT_SOUND.play()
            self.kill()
            yellow_spaceship.health_remainning -= 1
    def kill_bullet(self):
        self.kill()
        
    
# Nhóm ảnh các phi thuyền:
spaceship_group = pg.sprite.Group()
# Nhóm ảnh đạn:
bullet_group = pg.sprite.Group()

# Khởi tạo 1 ảnh phi thuyền
yellow_spaceship = Spaceship_yellow(50, int(SCREEN_HEIGHT / 2), MAX_HEALTH)
red_spaceship = Spaceship_red(SCREEN_WIDTH - 50, int(SCREEN_HEIGHT / 2), MAX_HEALTH)

# Thêm ảnh 2 phi thuyền vào group ảnh
spaceship_group.add(yellow_spaceship)
spaceship_group.add(red_spaceship)

def paused():
    run = True
    while(run):
        clock.tick(FPS)      
        MOUSE_POS = pg.mouse.get_pos()
        
        COUNTINUE_BUTTON = Button(image=BACKGROUND_PASS_5_LEVEL, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 100), text_input="COUNTINUE", font=get_font_comicsans(55), base_color=color_cyan, hovering_color=color_lime)
        BACK_BUTTON = Button(image=BACKGROUND_SURVIVAL, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), text_input="BACK TO MENU", font=get_font_comicsans(50), base_color=color_yellow, hovering_color=color_magenta)
        
        for button in [COUNTINUE_BUTTON, BACK_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(WINDOW)
        
        pg.display.update()
        
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if COUNTINUE_BUTTON.checkForInput(MOUSE_POS):
                    run = False
                if BACK_BUTTON.checkForInput(MOUSE_POS):
                    main()

def draw_mode_2():
    # Hiển thị background
    WINDOW.blit(background, (0, 0))
    # Hiển thị ranh giới giữa màn hình
    pg.draw.rect(WINDOW, color_purple, BORDER)

    # Yellow spaceship
    yellow_spaceship.update()
    yellow_spaceship.health_bar()
    
    # Red spaceship
    red_spaceship.update()
    red_spaceship.health_bar()
    
    # Group
    bullet_group.update()
    
    spaceship_group.draw(WINDOW)
    bullet_group.draw(WINDOW)
    
def get_font_comicsans(size):
    return pg.font.SysFont('font-times-new-roman', size)

def draw_menu_title (text):
    font = get_font_comicsans(50)
    draw_text = font.render(text, 1, color_cyan)
    x = 105
    y = 40
    WINDOW.blit(draw_text, (x, y))

def draw_text (text, size, x, y, color):
    font = get_font_comicsans(size)
    draw_text = font.render(text, 1, color)
    text_rect = draw_text.get_rect(center=(x, y))
    WINDOW.blit(draw_text, text_rect)

def draw_menu():
    WINDOW.blit(BACKGROUND_MENU, (0, 0))
    draw_menu_title("SPACESHIP")

def play_menu():
    run = True
    while(run):
        WINDOW.blit(BACKGROUND_PLAY_MENU, (0, 0))
        MOUSE_POS = pg.mouse.get_pos()
        
        draw_text(text="MODE",size=100,x=SCREEN_WIDTH/2,y=100,color=color_red)
        PASS_5_LEVEP_BUTTON = Button(image=BACKGROUND_PASS_5_LEVEL, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 100), text_input="PASS 5 LEVEL", font=get_font_comicsans(55), base_color=color_cyan, hovering_color=color_lime)
        SURVIVAL_BUTTON = Button(image=BACKGROUND_SURVIVAL, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), text_input="SURVIVAL", font=get_font_comicsans(55), base_color=color_cyan, hovering_color=color_lime)
        PLAY_2_PLAYER_BUTTON = Button(image=BACKGROUND_VS_2_PLAYER, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 100), text_input="VS 2 PLAYER", font=get_font_comicsans(55), base_color=color_cyan, hovering_color=color_lime)
        BACK_BUTTON = Button(image=BACKGROUND_SURVIVAL, pos=(170, 50), text_input="BACK TO MENU", font=get_font_comicsans(50), base_color=color_yellow, hovering_color=color_magenta)
        for button in [PASS_5_LEVEP_BUTTON, SURVIVAL_BUTTON, PLAY_2_PLAYER_BUTTON, BACK_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(WINDOW)
        
        pg.display.update()
        
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if  PASS_5_LEVEP_BUTTON.checkForInput(MOUSE_POS):
                    run = False
                    pass_5_level
                if  SURVIVAL_BUTTON.checkForInput(MOUSE_POS):
                    run = False
                    survival()
                if PLAY_2_PLAYER_BUTTON.checkForInput(MOUSE_POS):
                    run = False
                    yellow_spaceship.reset_yellow()
                    red_spaceship.reset_red()
                    play_2_player()
                if BACK_BUTTON.checkForInput(MOUSE_POS):
                    run=False
                    main()

def pass_5_level():
    run = True
    while(run):
        # Quy định số khung hình load trên 1 giây để ổn định khung hình
        clock.tick(FPS)
        
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                sys.exit()

def survival():
    a=0

def play_2_player():
    run = True
    while(run):
        # Quy định số khung hình load trên 1 giây để ổn định khung hình
        clock.tick(FPS)
        
        draw_mode_2()
        
        MOUSE_POS = pg.mouse.get_pos()
        PAUSE_BUTTON = Button(image=BACKGROUND_PAUSE, pos=(50, 30), text_input="PAUSE", font=get_font_comicsans(35), base_color=color_cyan, hovering_color=color_lime)
        PAUSE_BUTTON.changeColor(MOUSE_POS)
        PAUSE_BUTTON.update(WINDOW)
        
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:    
                if PAUSE_BUTTON.checkForInput(MOUSE_POS):
                    paused()
                
        pg.display.update()
        
def winner_menu(winner):
    run = True
    while(run):
        WINDOW.blit(BACKGROUND_VICTORY_MENU, (0, 0))
        
        MOUSE_POS = pg.mouse.get_pos()
        
        draw_text(text=winner, size=150, x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2 - 200, color=color_yellow)
        TRY_AGAIN_BUTTON = Button(image=BACKGROUND_TRY_AGAIN, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), text_input="TRY AGAIN", font=get_font_comicsans(75), base_color=color_cyan, hovering_color=color_lime)
        BACK_BUTTON = Button(image=BACKGROUND_BACK, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 100), text_input="BACK TO MENU", font=get_font_comicsans(75), base_color=color_cyan, hovering_color=color_lime)
        
        for button in [TRY_AGAIN_BUTTON, BACK_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(WINDOW)
        
        pg.display.update()
        
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if TRY_AGAIN_BUTTON.checkForInput(MOUSE_POS):
                    run = False
                    play_2_player()
                if BACK_BUTTON.checkForInput(MOUSE_POS):
                    run = False
                    main()
                    

def play():
    run = True
    while(run):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                sys.exit()
        play_menu()

def setting():
    run = True
    while(run):
        # Quy định số khung hình load trên 1 giây để ổn định khung hình
        clock.tick(FPS)
        
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                sys.exit()


def main ():
    run = True
    while(run):
        MOUSE_POS = pg.mouse.get_pos()
        
        draw_menu()
        
        PLAY_BUTTON = Button(image=BACKGROUND_PLAY, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 100), text_input="PLAY", font=get_font_comicsans(75), base_color=color_cyan, hovering_color=color_lime)
        OPTIONS_BUTTON = Button(image=BACKGROUND_SETTING, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), text_input="SETTING", font=get_font_comicsans(75), base_color=color_cyan, hovering_color=color_lime)
        QUIT_BUTTON = Button(image=BACKGROUND_QUIT, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 100), text_input="QUIT", font=get_font_comicsans(75), base_color=color_cyan, hovering_color=color_lime)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(WINDOW)
        
        pg.display.update()
        
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MOUSE_POS):
                    setting()
                if QUIT_BUTTON.checkForInput(MOUSE_POS):
                    pg.quit()
                    sys.exit()
    main()
    
if __name__ == "__main__":
    main()