# Thư viện ========================================================================================================================================================#
import pygame as pg
import os
import sys
import random
from button import Button
pg.init()
pg.font.init()
pg.mixer.init()
#==================================================================================================================================================================#

# Các chuẩn khung hình
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
# Setting về quái cơ bản
# Chỉnh số hàng, cột quái xuất hiện
rows = 9
cols = 5
# rows * cols = số lượng quái tổng cộng (45)

# Tốc độ đạn của quái
SPEED_ALIEN_BULLET = 10

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

BACKGROUND_HOW_TO_PLAY = pg.transform.scale(
    pg.image.load(
            os.path.join('Put files image here', 'Setting Rect.png')), (400, 80))

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
BACKGROUND_VS_BOTS = pg.transform.scale(
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

# Hàm in chữ lên màn hình

# Hàm lấy font chữ
def get_font_comicsans(size):
    return pg.font.SysFont('font-times-new-roman', size)

# In tiêu đề menu
def draw_menu_title (text):
    font = get_font_comicsans(50)
    draw_text = font.render(text, 1, color_cyan)
    x = 105
    y = 40
    WINDOW.blit(draw_text, (x, y))

# In lấy vị trí đặt là chính giữa box chứa chữ
def draw_text (text, size, x, y, color):
    font = get_font_comicsans(size)
    draw_text = font.render(text, 1, color)
    text_rect = draw_text.get_rect(center=(x, y))
    WINDOW.blit(draw_text, text_rect)

# In lấy vị trí đặt là góc trên bên trái box chứa chữ
def draw_text_guide (text, size, x, y, color):
    font = get_font_comicsans(size)
    draw_text = font.render(text, 1, color)
    WINDOW.blit(draw_text, (x, y))

#==================================================================================================================================================================#

# Đối tượng phi thuyền vàng và các phương thức của nó --- PLAYER 1
class Spaceship_yellow(pg.sprite.Sprite):
    def __init__ (self, x, y, health):
        pg.sprite.Sprite.__init__(self)
        self.image = YELLOW_SPACESHIP
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.health_max = MAX_HEALTH
        self.health_remaining = health
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
        self.health_remaining = self.health_max
        bullet_group.empty()
        self.rect.center = [50, int(SCREEN_HEIGHT / 2)]
                  
    def health_bar(self):
        pos_size_bar_red = (self.rect.left, self.rect.bottom + 10, self.rect.width, 15) 
        pg.draw.rect(WINDOW, color_red, pos_size_bar_red)
        if self.health_remaining > 0:
            ratio_health = (self.health_remaining / self.health_max)
            pos_size_bar_green = (self.rect.left, self.rect.bottom + 10, int(self.rect.width * ratio_health), 15)
            pg.draw.rect(WINDOW, color_lime, pos_size_bar_green)
        if self.health_remaining <= 0:
            EXPLORE_SPACESHIP_SOUND.play()
            self.health_remaining = self.health_max
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
            red_spaceship.health_remaining -= 1

# Đối tượng phi thuyền đỏ và các phương thức của nó --- PLAYER 2
class Spaceship_red(pg.sprite.Sprite):
    def __init__ (self, x, y, health):
        pg.sprite.Sprite.__init__(self)
        self.image = RED_SPACESHIP
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.health_max = health
        self.health_remaining = health
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
        self.health_remaining = self.health_max
        bullet_group.empty()
        self.rect.center = [SCREEN_WIDTH - 50, int(SCREEN_HEIGHT / 2)]
        
    def health_bar(self):
        pos_size_bar_red = (self.rect.left, self.rect.bottom + 10, self.rect.width, 15) 
        pg.draw.rect(WINDOW, color_red, pos_size_bar_red)
        if self.health_remaining > 0:
            ratio_health = (self.health_remaining / self.health_max)
            pos_size_bar_green = (self.rect.left, self.rect.bottom + 10, int(self.rect.width * ratio_health), 15)
            pg.draw.rect(WINDOW, color_lime, pos_size_bar_green)
        if self.health_remaining <= 0:
            EXPLORE_SPACESHIP_SOUND.play()
            self.health_remaining = self.health_max
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
        if self.rect.left <= 0: # Khi viên đạn rời khỏi màn hình sẽ tự biến mất
            self.kill()
        if pg.sprite.spritecollide(self, spaceship_group, False): # Khi viên đạn bắn trúng vật thể sẽ tự biến mất và kém âm thanh vật thể trúng đạn
            BULLET_HIT_SOUND.play()
            self.kill()
            yellow_spaceship.health_remaining -= 1 # Giảm máu khi trúng đạn
    def kill_bullet(self):
        self.kill()

class Spaceship(pg.sprite.Sprite):
    def __init__ (self, x, y, health):
        pg.sprite.Sprite.__init__(self)
        self.image = YELLOW_SPACESHIP
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.health_max = MAX_HEALTH
        self.health_remaining = health
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
        if key[pg.K_a] and self.rect.left > 10:
            self.rect.x -= SPEED_SPACESHIP
        if key[pg.K_d] and self.rect.right < SCREEN_WIDTH - 10:
            self.rect.x += SPEED_SPACESHIP
        if key[pg.K_w] and self.rect.top > 10:
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
                            bullet = Bullets(self.rect.centerx + 20, self.rect.top + 27)
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
                bullet = Bullets(self.rect.centerx + 20, self.rect.top + 27)
                bullet_group.add(bullet)
                BULLET_FIRE_SOUND.play()
                self.last_shot = time_now
    
    def health_bar(self):
        pos_size_bar_red = (self.rect.left, self.rect.bottom + 10, self.rect.width, 15) 
        pg.draw.rect(WINDOW, color_red, pos_size_bar_red)
        if self.health_remaining > 0:
            ratio_health = (self.health_remaining / self.health_max)
            pos_size_bar_green = (self.rect.left, self.rect.bottom + 10, int(self.rect.width * ratio_health), 15)
            pg.draw.rect(WINDOW, color_lime, pos_size_bar_green)
        if self.health_remaining <= 0:
            EXPLORE_SPACESHIP_SOUND.play()
            self.health_remaining = self.health_max
            alien_group.empty()
            alien_bullet_group.empty()
            menu("YOU DIED")

class Bullets(pg.sprite.Sprite):
    def __init__ (self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = RED_BULLET
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    def update(self):
        self.rect.centerx += SPEED_BULLET
        if self.rect.right > SCREEN_WIDTH:
            self.kill()
        if pg.sprite.spritecollide(self, alien_group, True):
            self.kill()

class Aliens(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("Put files image here/alien" + str(random.randint(1, 5)) + ".png") # tạo hình ảnh quái vật một cách random
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.move_counter = 0 # Đếm số lượng dịch chuyển của hình ảnh
        self.move_direction = 1 # Khoảnh cách hình ảnh di chuyển

    def update(self):
        self.rect.y += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 40: # Khi di chuyển qua 40 pixel
            self.move_direction *= -1 # Thì sẽ đảo ngược lại hướng di chuyển ban đầu
            self.move_counter *= self.move_direction
            # Để khi move_counter = 39 hoặc -39 thì sẽ đảo ngược lại về -39 hoặc 39
            # Giá trị move_counter sẽ di chuyển trong khoảng (39 -> 0 -> -39) hoặc (-39 -> 0 -> 39)
            # Hình ảnh quái vật sẽ di chuyển xuống dưới (0 -> 39) rồi di chuyển về ban đầu (39 -> 0)
            # rồi di chuyển lên trên (0 -> -39) rồi di chuyển ban đầu (-39 -> 0) rồi lặp lại như ban đầu
            # Làm như trên mỗi khi khung hình được tạo ra hình ảnh quái vật sẽ trông như di chuyển lên xuống

class Alien_Bullets(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("Put files image here/alien_bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.x -= SPEED_ALIEN_BULLET # Giảm tọa độ x
        if self.rect.right <= 0: # Khi đạn ra khỏi màn hình hiển thị
            self.kill() # thì sẽ biến mất
        if pg.sprite.spritecollide(self, spaceship_group_2, False, pg.sprite.collide_mask):
            self.kill()
            # Giảm hp người chơi khi bị trúng đạn
            spaceship.health_remaining -= 1

# Nhóm ảnh các phi thuyền:
spaceship_group = pg.sprite.Group()
spaceship_group_2 = pg.sprite.Group()
alien_group = pg.sprite.Group()
# Nhóm ảnh đạn:
bullet_group = pg.sprite.Group()
alien_bullet_group = pg.sprite.Group()

# Khởi tạo 1 ảnh phi thuyền
spaceship = Spaceship(50, int(SCREEN_HEIGHT / 2), MAX_HEALTH)
yellow_spaceship = Spaceship_yellow(50, int(SCREEN_HEIGHT / 2), MAX_HEALTH)
red_spaceship = Spaceship_red(SCREEN_WIDTH - 50, int(SCREEN_HEIGHT / 2), MAX_HEALTH)

# Thêm ảnh 2 phi thuyền vào group ảnh
spaceship_group.add(yellow_spaceship)
spaceship_group.add(red_spaceship)
spaceship_group_2.add(spaceship)

# Tạo ra các con quái
def create_aliens():
    for row in range(rows):
        for item in range(cols):
            alien = Aliens(SCREEN_WIDTH/2 + 100 + item * 100, 70 + row * 70)
            alien_group.add(alien)

# Làm mới lại màn hình như lúc mới vào chơi
def reset_level():
    alien_group.empty()
    alien_bullet_group.empty()
    bullet_group.empty()
    spaceship.rect.center = (50, int(SCREEN_HEIGHT / 2))
    spaceship.health_remaining = MAX_HEALTH

# Chế độ player bắn với quái
def vs_bots():
    run = True
    last_alien_shot = pg.time.get_ticks()
    alien_cooldown = 500
    create_aliens()
    while(run): # vòng lặp while để để ảnh cập nhật liên tục khung hình sau sẽ đè lên khung hình trước
        # Quy định số khung hình load trên 1 giây để ổn định khung hình
        clock.tick(FPS)
        # Hiển thị background
        WINDOW.blit(background, (0, 0))
        
        # Hiển thị các dòng chữ
        text_enemy = "Enemy: "+str(len(alien_group))+"/45"
        draw_text(text=text_enemy,size=40,x=230,y=30, color=color_yellow)
        text_hp = "My hp: "+str(spaceship.health_remaining)+"/10"
        draw_text(text=text_hp,size=40,x=430,y=30, color=color_yellow)
        
        # Nếu hết quái thì sẽ hiển ra màn hình "Bạn thắng"
        if(len(alien_group) <= 0):
            reset_level()
            menu("YOU WON")
        
        # Lấy thời gian hiện tại
        time_now = pg.time.get_ticks()
        
        # Quái bắn đạn
        if time_now - last_alien_shot > alien_cooldown and len(alien_group) > 0: # Sau một khoảng thời gian nhất định bạn sẽ được bắn ra
            attacking_alien = random.choice(alien_group.sprites()) # Chọn ngẫu nhiên quái nào sẽ bắn ra đạn
            alien_bullet = Alien_Bullets(attacking_alien.rect.centerx, attacking_alien.rect.bottom) # Tạo ra đạn ở vị trí quái đã chọn
            alien_bullet_group.add(alien_bullet)
            last_alien_shot = time_now # đặt lại thời gian mà đạn đã bắn
        
        # Yellow spaceship
        spaceship.update()
        spaceship.health_bar()
        
        # Group
        bullet_group.update()
        alien_bullet_group.update()
        alien_group.update()
        
        spaceship_group_2.draw(WINDOW)
        bullet_group.draw(WINDOW)
        alien_group.draw(WINDOW)
        alien_bullet_group.draw(WINDOW)
        
        MOUSE_POS = pg.mouse.get_pos()
        PAUSE_BUTTON = Button(image=BACKGROUND_PAUSE, pos=(50, 30), text_input="PAUSE", font=get_font_comicsans(35), base_color=color_cyan, hovering_color=color_lime)
        PAUSE_BUTTON.changeColor(MOUSE_POS) # Đổi màu khi di chuyển vào nút PAUSE
        PAUSE_BUTTON.update(WINDOW) # update lại hình ảnh

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

def menu(message):
    run = True
    while(run):
        WINDOW.blit(BACKGROUND_VICTORY_MENU, (0, 0))
        
        MOUSE_POS = pg.mouse.get_pos()
        
        draw_text(text=message, size=150, x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2 - 200, color=color_yellow)
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
                    vs_bots()
                if BACK_BUTTON.checkForInput(MOUSE_POS):
                    run = False
                    main()

# Chế độ 2 player bắn nhau
def vs_2_player():
    run = True
    while(run):
        # Quy định số khung hình load trên 1 giây để ổn định khung hình
        clock.tick(FPS)
        
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

# Chức năng nút pause
def paused():
    run = True
    while(run):
        MOUSE_POS = pg.mouse.get_pos()
        
        COUNTINUE_BUTTON = Button(image=BACKGROUND_VS_BOTS, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 100), text_input="COUNTINUE", font=get_font_comicsans(55), 
                                  base_color=color_cyan, hovering_color=color_lime)
        BACK_BUTTON = Button(image=BACKGROUND_SURVIVAL, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), text_input="BACK TO MENU", font=get_font_comicsans(50), 
                             base_color=color_yellow, hovering_color=color_magenta)
        
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
                if COUNTINUE_BUTTON.checkForInput(MOUSE_POS): # Nếu nhấn nút "COUNTINUE" thì thoát khỏi vòng lặp
                    run = False
                if BACK_BUTTON.checkForInput(MOUSE_POS): # Nếu nhấn nút "BACK" thì reset lại màn hình đang chơi, trở lại về main
                    reset_level()
                    main()

# Màn hình hiển thị sau khi chiến thắng
def winner_menu(winner):
    run = True
    while(run):
        WINDOW.blit(BACKGROUND_VICTORY_MENU, (0, 0))
        
        MOUSE_POS = pg.mouse.get_pos()
        
        draw_text(text=winner, size=150, x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2 - 200, color=color_yellow)
        TRY_AGAIN_BUTTON = Button(image=BACKGROUND_TRY_AGAIN, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), text_input="TRY AGAIN", font=get_font_comicsans(75), 
                                  base_color=color_cyan, hovering_color=color_lime)
        BACK_BUTTON = Button(image=BACKGROUND_BACK, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 100), text_input="BACK TO MENU", font=get_font_comicsans(75), 
                             base_color=color_cyan, hovering_color=color_lime)
        
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
                    vs_2_player()
                if BACK_BUTTON.checkForInput(MOUSE_POS):
                    run = False
                    main()
                    
# Chức năng nút play
def play():
    run = True
    while(run):
        WINDOW.blit(BACKGROUND_PLAY_MENU, (0, 0))
        MOUSE_POS = pg.mouse.get_pos()
        
        draw_text(text="MODE",size=100,x=SCREEN_WIDTH/2,y=100,color=color_red)
        VS_BOTS_BUTTON = Button(image=BACKGROUND_VS_BOTS, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50), text_input="VS BOTS", font=get_font_comicsans(55), 
                                     base_color=color_cyan, hovering_color=color_lime)
        PLAY_2_PLAYER_BUTTON = Button(image=BACKGROUND_VS_2_PLAYER, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50), text_input="VS 2 PLAYER", font=get_font_comicsans(55), 
                                      base_color=color_cyan, hovering_color=color_lime)
        BACK_BUTTON = Button(image=BACKGROUND_SURVIVAL, pos=(170, 50), text_input="BACK TO MENU", font=get_font_comicsans(50), 
                             base_color=color_yellow, hovering_color=color_magenta)
        
        for button in [VS_BOTS_BUTTON, PLAY_2_PLAYER_BUTTON, BACK_BUTTON]:
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
                if  VS_BOTS_BUTTON.checkForInput(MOUSE_POS):
                    run = False
                    yellow_spaceship.reset_yellow()
                    vs_bots()
                if PLAY_2_PLAYER_BUTTON.checkForInput(MOUSE_POS):
                    run = False
                    yellow_spaceship.reset_yellow()
                    red_spaceship.reset_red()
                    vs_2_player()
                if BACK_BUTTON.checkForInput(MOUSE_POS):
                    run=False
                    main()

# Chức năng how to play: hướng dẫn chơi
def guide():
    run = True
    while(run):
        # Quy định số khung hình load trên 1 giây để ổn định khung hình
        clock.tick(FPS)
        
        WINDOW.blit(BACKGROUND_PLAY_MENU, (0, 0))
        
        MOUSE_POS = pg.mouse.get_pos()
        BACK_BUTTON = Button(image=BACKGROUND_SURVIVAL, pos=(170, 50), text_input="BACK TO MENU", font=get_font_comicsans(50), 
                             base_color=color_yellow, hovering_color=color_magenta)
        BACK_BUTTON.changeColor(MOUSE_POS)
        BACK_BUTTON.update(WINDOW)
        
        draw_text(text="How To Play", size=70, x=SCREEN_WIDTH/2, y=40, color=color_red)
        
        draw_guide_player_1()
        draw_guide_player_2()
        draw_guide_mode()

        pg.display.update()
        
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                sys.exit()   
            if event.type == pg.MOUSEBUTTONDOWN:
                    if BACK_BUTTON.checkForInput(MOUSE_POS):
                        run=False
                        main()

# In ra các dòng chữ hướng dẫn player 1
def draw_guide_player_1():
    draw_text_guide(text="Player 1", size=50, x=30, y=120,color=color_red)
    
    draw_text_guide(text="W: move up", size=50, x=30, y=200,color=color_red)
    draw_text_guide(text="S: move down", size=50, x=30, y=240,color=color_red)
    draw_text_guide(text="A: move left", size=50, x=30, y=280,color=color_red)
    draw_text_guide(text="D: move right", size=50, x=30, y=320,color=color_red)
    
    draw_text_guide(text="SPACE: shot", size=50, x=30, y=400,color=color_red)
    draw_text_guide(text="C: switch to single", size=50, x=30, y=440,color=color_red)
    draw_text_guide(text="V: switch to burst", size=50, x=30, y=480,color=color_red)

# In ra các dòng chữ hướng dẫn player 2
def draw_guide_player_2():
    draw_text_guide(text="Player 2", size=50, x=530, y=120,color=color_red)
    
    draw_text_guide(text="arrow up: move up", size=50, x=530, y=200,color=color_red)
    draw_text_guide(text="arrow down: move down", size=50, x=530, y=240,color=color_red)
    draw_text_guide(text="arrow left: move left", size=50, x=530, y=280,color=color_red)
    draw_text_guide(text="arrow right: move right", size=50, x=530, y=320,color=color_red)
    
    draw_text_guide(text="CTRL RIGHT: shot", size=50, x=530, y=400,color=color_red)
    draw_text_guide(text="INS: switch to single", size=50, x=530, y=440,color=color_red)
    draw_text_guide(text="DEL: switch to burst", size=50, x=530, y=480,color=color_red)

# In ra các dòng chữ giải thích 2 mode
def draw_guide_mode():
    draw_text_guide(text="VS BOTS: You will have some enemy. They will shoot you so try to dodge and shoot back", size=30, x=30, y=560,color=color_red)
    draw_text_guide(text="You will win when all your enemy is gone", size=30, x=130, y=590,color=color_red)
    draw_text_guide(text="VS 2 Player: 2 players will shoot each other until 1 player runs out of health bars. The other will win.", size=30, x=30, y=640,color=color_red)
    
def main ():
    run = True
    while(run):
        # Lấy vị trí chuột hiển thị
        MOUSE_POS = pg.mouse.get_pos()
        
        # Hiển thị background sau menu chính
        WINDOW.blit(BACKGROUND_MENU, (0, 0))
        # In tiêu đề tên game
        draw_menu_title("SPACESHIP")
        # Khởi tạo Các nút
        PLAY_BUTTON = Button(image=BACKGROUND_PLAY, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 100), text_input="PLAY", font=get_font_comicsans(75), 
                             base_color=color_cyan, hovering_color=color_lime)
        HOW_TO_PLAY_BUTTON = Button(image=BACKGROUND_HOW_TO_PLAY, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), text_input="HOW TO PLAY", font=get_font_comicsans(75), 
                                    base_color=color_cyan, hovering_color=color_lime)
        QUIT_BUTTON = Button(image=BACKGROUND_QUIT, pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 100), text_input="QUIT", font=get_font_comicsans(75), 
                             base_color=color_cyan, hovering_color=color_lime)

        # Thay đổi màu khi di chuyển chuột vào nút
        for button in [PLAY_BUTTON, HOW_TO_PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(WINDOW)
        
        pg.display.update()
        
        # Tạo chức năng cho các nút
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MOUSE_POS):
                    play()
                if HOW_TO_PLAY_BUTTON.checkForInput(MOUSE_POS):
                    guide()
                if QUIT_BUTTON.checkForInput(MOUSE_POS):
                    pg.quit()
                    sys.exit()
    
if __name__ == "__main__":
    main()