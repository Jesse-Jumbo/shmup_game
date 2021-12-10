# Shmup game
# Frozen Jam by tgfcoder <https://twitter.com/tgfcoder> licensed under CC-BY-3
# Art from Kenney.n1

import random  # 預先引用random，你可能會用到它，在做pygame時
from os import path  # the function os.path it's mean where is the correct location and path for our files

import pygame  # 引用pygame

img_dir = path.join(path.dirname(__file__), 'img') # define img_dir function equals path join from the file name, img name
snd_dir = path.join(path.dirname(__file__), 'snd')

# 設螢幕寬480，高600適合射擊遊戲，並且將幀數設成60，讓動作順暢快速
WIDTH = 480
HEIGHT = 600
FPS = 60

# define colors                                    #(red, green, blue)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# initialize pygame and create window
pygame.init()                                      # 初始化並啟動遊戲
pygame.mixer.init()                                # 初始化混音器，啟動聲音
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # 設定我們的螢幕變數名:screen和視窗的(寬，高)
pygame.display.set_caption("Shump!")               # 設定任何我們想要的標題在視窗最上面
clock = pygame.time.Clock()                        # 設定一個測定遊戲時間，用來確保我們運行的每一幀都是正確的

font_name = pygame.font.match_font('arial')        # the function can searches the system for the closest matching font.
def draw_text(surf, text, size, x, y):             # define the draw_text
    font = pygame.font.Font(font_name, size)       # defing a variable(font) to draw text in screen
    text_surface = font.render(text, True, WHITE)  # font.render(): calculating what pattern of pixels is needed (True means Anti-aliasing)
    text_rect = text_surface.get_rect()            # get rect of text
    text_rect.midtop = (x, y)                      # Align text_rect.midtop with location of draw_text
    surf.blit(text_surface, text_rect)             # Set text_surface onto surf(draw_text on the there) from text_rect with blit()

class Player(pygame.sprite.Sprite):                # 宣告一個class Player把pygame.sprite.Sprite賦予給它
    def __init__(self):                            # 必須要有的初始化函式__init__你才能啟動整個函式
        pygame.sprite.Sprite.__init__(self)        # __init__初始化Sprite你才能引用它
        self.image = pygame.transform.scale(player_img, (50, 38))       # Declare a image of self equals transform to 50 width and 38 height scale of player_img in pygame
        self.image.set_colorkey(BLACK)             # Set to ignore the black color of that image
        self.rect = self.image.get_rect()          # 設一個rect用.get_rect()計算image的rectangle去抓住它
        self.radius = 20                           # Set the redius of that rectangle to 20 of size so the rect will become a circle
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2              # 設rect的centerx在寬度的正中心
        self.rect.bottom = HEIGHT - 10             # 設rect的bottom在高度的-10處
        self.speedx = 0                            # x軸速度初始化為零

    def update(self):                              # 宣告一個update函式，在下面game loop引用到它
        self.speedx = 0                            # 將X軸速度固定在0
        keystate = pygame.key.get_pressed()        # 宣告keystate將引用Pygame裡的函式pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:                # 如果按下LEFT鍵
            self.speedx = -5                       # X軸速度減5(往左)
        if keystate[pygame.K_a]:                   # 如果按下a鍵
            self.speedx = -8                       # X軸速度減8(往左)
        if keystate[pygame.K_RIGHT]:               # 如果按下RIGHT鍵
            self.speedx = 5                        # X軸速度5(往右)
        if keystate[pygame.K_d]:                   # 如果按下d鍵
            self.speedx = 8                        # X軸速度8(往右)
        self.rect.x += self.speedx                 # 設定rect.x軸跟著self.X軸的speed變動
        if self.rect.right > WIDTH:                # 如果rect.right大於螢幕寬
            self.rect.right = WIDTH                # 把rect.right固定在螢幕寬
        if self.rect.left < 0:                     # 如果rect.left小於0
            self.rect.left = 0                     # 將rect.left等於0

    def shoot(self):                               # 在玩家這裡新增一項物件shoot子彈用來讓我們射擊
        bullet = Bullet(self.rect.centerx, self.rect.top)               # 產生一個新的bullet它是來自Bullet(x, y)，它是從self玩家的rect的centerx(x軸中心)和top(最上方)生成
        all_sprites.add(bullet)                    # 將bullet加入到all_sprites(方便被繪製和更新)
        bullets.add(bullet)                        # 把bullet加入bullets(用於下面hits判斷)
        shoot_sound.play()

class Mob(pygame.sprite.Sprite):                   # pygame.sprite for Sprite for class Mob
    def __init__(self):                            # 初始化函式，用於啟動函式
        pygame.sprite.Sprite.__init__(self)        # 初始化Sprite引用到pygame.sprite
        self.image_orig = random.choice(meteor_images)                  # Declare the image_orig = randomly choice the meteor_images list
        self.image_orig.set_colorkey(BLACK)        # Set to ignore the black color of that image_orig
        self.image = self.image_orig.copy()        # Declare the image is copied form image_orig
        self.rect = self.image.get_rect()          # 創建一個rect，用get_rect去計算抓住image的rectangle
        self.radius = int(self.rect.width * .85 / 2)                    # Declare that the radius of the image is 85%/2 width
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)      # rect隨機出現在X軸的(0到螢幕寬- rect寬)範圍內
        self.rect.y = random.randrange(-150, -100)                      # rect隨機出現在Y軸的(螢幕外-100到-40)範圍內(落下時更為分散、隨機，而不是直接一次出現在螢幕的上界限)
        self.speed_y = random.randrange(1, 8)                           # Y軸的速度隨機範圍在(1到8)掉落
        self.speed_x = random.randrange(-3, 3)                          # X軸的速度隨機範圍在(-3到3)橫移
        self.rot = 0                                                    # Declare the rot of rect is equals zero
        self.rot_speed = random.randrange(-8, 8)                        # Declare that the speed of rotation is ramdom in the range of -8 to 8
        self.last_update = pygame.time.get_ticks()                      # Declare a last_update, that is get ticks from time of pygame

    def rotate(self):                                                   # define self of rotate
        now = pygame.time.get_ticks()                                   # Declare now equals get ticks from time of pygame
        if now - self.last_update > 50:                                 # if the now minus the last_update of self is graeter than fifteen
            self.last_update = now                                      # then it will put the velue of now in the last_update of self
            self.rot = (self.rot + self.rot_speed) % 360                # Declare that the rot of self is equal to the rot plus the rot_speed is an integer less than 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)  # Declare a new_image is equal to transform the image_orig and the rot to rotate in pygame
            old_center = self.rect.center                               # Declare the old_center is equal to rect center of self
            self.image = new_image                                      # Declare the image of self is equals new_image
            self.rect = self.image.get_rect()                           # Declare the rect is equal to get the rectangle of image
            self.rect.center = old_center                               # Declare the center of rect is equals the ole_center

    def update(self):                              # 宣告一個update用於game loop裡更新
        self.rotate()                              # put the rotate of class in the self of update
        self.rect.y += self.speed_y                # 將rect的Y軸跟著speed_y更新
        self.rect.x += self.speed_x                # 將rect的X軸跟著speed_x更新
        if self.rect.top > HEIGHT + 10 or self.rect.left < - 25 or self.rect.right > WIDTH + 20:  # 如果rect的頂端超出底部或左邊超出右邊或右邊超出左邊
            self.rect.x = random.randrange(WIDTH - self.rect.width)     # rect隨機出現在X軸的0(默認值，可省略)到螢幕寬- rect寬的範圍內
            self.rect.y = random.randrange(-100, -40)                   # rect隨機出現在Y軸的(-100到-40)範圍內
            self.speed_y = random.randrange(1, 8)                       # Y軸的速度隨機範圍在(1到8)掉落

class Bullet(pygame.sprite.Sprite):                # 宣告一個Bullet類別屬於pygame.sprite.Sprite
    def __init__(self, x, y):                      # 初始化Bullet的self, x, y，用於啟動、更新它
        pygame.sprite.Sprite.__init__(self)        # 初始化Sprite引用到pygame.sprite
        self.image = bullet_img                    # Declare the image of self equals bullet_img
        self.image.set_colorkey(BLACK)             # set to ignore the black color of image
        self.rect = self.image.get_rect()          # 宣告rect為用get_rect()計算image的rectangle大小、位置去抓住它
        self.rect.bottom = y                       # 將image的rect的bottom(底部)定義為y
        self.rect.centerx = x                      # 將rect的centerx(x軸(上限)中心)定義為x
        self.speed_y = -10                         # 將Bullet的speedy設為 -10，讓他極快筆直地往上射擊

    def update(self):                              # 定義Bullet的update，用於下面的game loop
        self.rect.y += self.speed_y                # 將Bullet的rect的Y軸隨著speed_y變化
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:                   # 如果rect的bottom小於0(也就是X<0 => 超出螢幕上方界限)
            self.kill()                            # pygame內建函數.kill()可從任何Group中刪除sprite(在這就是刪除Bullet)

# Load all game graphics                           # we have to use the convert function to load all graphics in the pygame
background = pygame.image.load(path.join(img_dir, "Space Shooter Background - Imgur.png")).convert()
background_rect = background.get_rect()            # define the background_rect equals the rectangle of background
player_img = pygame.image.load(path.join(img_dir, "playerShip3_red.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "laserBlue16.png")).convert()
meteor_images = []                                 # Declare a empty list, then declare a other list and define there were all meteor_images
meteor_list = ['meteorBrown_big1.png', 'meteorBrown_big2.png', 'meteorBrown_big3.png', 'meteorBrown_big4.png',
               'meteorBrown_med1.png', 'meteorBrown_med3.png', 'meteorBrown_small1.png', 'meteorBrown_small2.png',
               'meteorBrown_tiny1.png', 'meteorBrown_tiny2.png', 'meteorGrey_big1.png', 'meteorGrey_big2.png',
               'meteorGrey_big3.png', 'meteorGrey_big4.png', 'meteorGrey_med1.png', 'meteorGrey_med2.png',
               'meteorGrey_small1.png', 'meteorGrey_small2.png', 'meteorGrey_tiny1.png', 'meteorGrey_tiny2.png']
for img in meteor_list:                            # declare a circle to append the all img from img_dir to loop in the meteor_list
    meteor_images.append(pygame.image.load(path.join(img_dir, img)).convert())

# Load all game sounds
shoot_sound = pygame.mixer.Sound(path.join(snd_dir, 'pew.wav'))
expl_sounds = []
for snd in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(path.join(snd_dir, snd)))
pygame.mixer.music.load(path.join(snd_dir, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
pygame.mixer.music.set_volume(0.4)

all_sprites = pygame.sprite.Group()                # 使用Group宣告物件all_sprites # all_sprites拿來做為所有sprite物件的集合
mobs = pygame.sprite.Group()                       # 宣告一個mobs，將它加入到pygame.sprite.Group
bullets = pygame.sprite.Group()                    # 將bullets添加到pygame.sprite.Group作儲存
player = Player()                                  # 用Player class宣告物件player
all_sprites.add(player)                            # 把player加入all_sprites，並且因為player是一個Group()也是一個class才成立
for i in range(8):                                 # 讓 i 循環8次，執行以下(使螢幕內的Mob總是維持在8位):
    m = Mob()                                      # 宣告一個m到Mob()這個class，使其生成
    all_sprites.add(m)                             # 將是Group()屬於class Mob()的m加到all_sprites中，使其更新
    mobs.add(m)                                    # 將m加到mobs這個Group()中，使m在mobs這個Group，方便一次被判斷

score = 0                                          # initialize our score to 0 after game loop
pygame.mixer.music.play(loops=-1)

# Game loop
running = True                                     # 設定一個變數running，他的初始值是Ture，所以只要我們設定running是False循環就會結束
while running:                                     # 執行running是True的時候(肯定句)
    # keep loop running at the right speed
    clock.tick(FPS)                                # 檢查遊戲時間內的FPS是否保持在我們所宣告的
    # Process input (events)  #events是任何遊戲之外的輸入，你希望電腦能知道的(然後才能選擇做出甚麼反應)
    for event in pygame.event.get():               # event在pygame.event.get()裡，event.get()的回傳值是list(Eventlist)
        # check for closing window
        if event.type == pygame.QUIT:              # event按下 是 pygame.QUIT時
            running = False                        # running會錯誤，也就是while running程式會關閉
        elif event.type == pygame.KEYDOWN:         # 又如果按下的事件是KEYDOWN(pygame內建函數，意思是鍵盤上有鍵被按下)
            if event.key == pygame.K_SPACE:        # 且key為K_SPACE空白鍵
                player.shoot()                     # 引用上面在player定義的shoot()

    # Update
    all_sprites.update()                           # 在game loop裡update我們在上面所宣告的sprites

    # check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)        # 定義hits為引用pygame內建函數groupcollide(前兩個參數為要檢查碰撞的Group類別, 後兩個分別與之對應, 回傳值是list(儲存所有碰撞到的所有事件(如果沒有則為空list))，True代表kill，False代表保留)來判斷重疊
    for hit in hits:                               # 創建一個for迴圈hit是在hits裡循環(如果hits回傳的list裡有東西)，只要你一直有在攻擊，那麼就會一直循環(使上面的hits的Mobs不會全被bullets消除完)
        score += 50 - hit.radius                   # scroe const
        random.choice(expl_sounds).play()
        m = Mob()                                  # 宣告一個m是Mob()這個class，使m會在Mob()內生成mob
        all_sprites.add(m)                         # 將在Mob()的m加入到all_sprites，使m會在all_sprites裡屬於Mob()的update裡更新
        mobs.add(m)                                # 將是all_sprites的m加入到mobs，使mobs內會不斷生成m，讓hits內的mobs可以被不斷的檢查

    # check to see if a mob hit the player         # 第四個參數甚麼都不寫就默認是rect，你可以輸入你要判定的是甚麼，這裡更正為collide_circle
    hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)             # 定義hits為引用pygame內建函數spritecollide(前兩個參數，為sprite(前者)與要檢查是否碰撞到它的Group(後者), 回傳list(儲存所有碰撞到的所有事件(如果沒有則為空list))，後參數True代表kill，False代表保留)來判斷重疊
    if hits:                                       # 如果hits是...(如果if判斷式內的參數有東西，默認為真 => 執行要求)
        running = False                            # runing為False(也就是將執行while迴圈的條件設為不成立 = 停止更新遊戲結束)

    # Draw / render
    screen.fill(BLACK)                             # 設定螢幕填滿(你想要的XX色)
    screen.blit(background, background_rect)       # set the background onto our screen, the backgroud is copy from background_rect with the blit function
    all_sprites.draw(screen)                       # 將sprites繪上螢幕
    draw_text(screen, str(score), 18, WIDTH / 2, 10)                   # (location, string of score, the font size, X, Y)
    # *after* drawing everything, flip the display
    pygame.display.flip()                          # 更新畫面，把我們所做的事讓電腦存取

pygame.quit()                          # 程式結束