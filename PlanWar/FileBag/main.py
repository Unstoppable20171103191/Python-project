
#引入 pygame
import pygame
#pygame 常量
from pygame.locals import *
from sys import exit

#设置游戏屏幕大小
SCREEN_WIDTH= 480
SCREEN_HRIGHT= 800

#子弹类
class Bullet(pygame.sprite.Sprite):
    #子弹图片和位置
    def __init__(self,bullet_img,init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=bullet_img  #设置子弹图片
        self.rect=self.image.get_rect()   #设置图片位置
        self.rect.midbootom=init_pos   #子弹起始位置
        self.speed = 10

    #子弹移动-1
    def move(self):
        self.rect.top -=self.speed

#玩家飞机类
class Player(pygame.sprite.Sprite):
    def _init_(self,plan_img,player_rect,init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=[]
        for i in range(len(player_rect)):
            self.image.append(plan_img.subsurface(player_rect[i]).convert_alpha())
        self.rect=player_rect[0]
        self.rect.topleft= init_pos
        self.speed=8
        self.bullets=pygame.sprite.Group()
        self.image_index=0  #索引定义图片
        self.is_hit=False

    #发射子弹
    def shoot(self,bullet_img):
        bullet=Bullet(bullet_img,self.rect.midbootom)
        self.bullets.add(bullet)


# 飞机移动
    #向上移动
    def moveUp(self):
        if self.rect.top<=0:
            self.rect.top=0
        else:
            self.rect.top -=self.speed

    #向下
    def moveDown(self):
        if self.rect.top>=SCREEN_HRIGHT-self.rect.height:
            self.top=SCREEN_HRIGHT-self.trct.height   #表示最低点
        else:
            self.rect.top +=self.speed

    #向左
    def moveLeft(self):
        if self.rect.topleft<=0:
            self.rect.topleft=0
        else:
            self.rect.left -=self.speed

    #向右
    def moveRight(self):
        if self.rect.left>=SCREEN_WIDTH-self.rect.width:
            self.rect.left=SCREEN_WIDTH-self.rect.width
        else:
            self.rect.left +=self.speed


#敌机类 左上角是基准点
class Enemy(pygame.sprite.Sprite):
    def _init_(self,enemy_img,enemy_down_imgs,init_pos):
        pygame.sprite.Sprite.__init__(self)   #继承父类
        self.image=enemy_img
        self.rect=self.image.get_rect()
        self.rect.topleft=init_pos
        self.down_imgs = enemy_down_imgs
        self.speed=2
        self.down_index=0

    #敌机移动相反
    def move(self):
        self.rect.top+=self.speed

#初始化pygame
pygame.init()
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HRIGHT))  #pygame内置方法设置窗体大小
#设置名称
pygame.display.set_caption('PlanWar')   #pygame内置方法设置名称
ic_launcher=pygame.image.load('resources/image/ic_launcher.png').convert_alpha()  #加载图片
pygame.display.set_icon(ic_launcher)  #设置使用左上角图片
#设置背景图片
background=pygame.image.load('resources/image/background.png')
#游戏结束图片
game_over=pygame.image.load('resources/image/gameover.jpg')
#玩家飞机，子弹，敌机
plan_img=pygame.image.load('resources/image/shoot.png')


def startGame():
    player_rect=[]
    player_rect.append(pygame.Rect(0,99,100,120))
    player_rect.append(pygame.Rect(165, 360, 102, 126))
    player_rect.append(pygame.Rect(165, 234, 102, 126))
    player_rect.append(pygame.Rect(330, 498, 102, 126))
    player_rect.append(pygame.Rect(330, 498, 102, 126))
    player_rect.append(pygame.Rect(432, 624, 102, 126))
    player_pos=[200,600]
    player=Player(plan_img,player_pos)
    # 游戏主循环
    running = True
    # 保持屏幕
    while running:
        screen.fill(0)
        screen.blit(background, (0, 0))

        if not player.is_hit:
            screen.blit(player.image[player.image_index],player.rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                pygame.quit()
                exit()
        key_pressed = pygame.key.get_pressed()
        # 向上
        if key_pressed[K_w] or key_pressed[K_UP]:
            player.moveUp()
        # 向下
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            player.moveDown()
        # 向左
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            player.moveLeft()
        # 向右
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            player.moveRight()
startGame()

















