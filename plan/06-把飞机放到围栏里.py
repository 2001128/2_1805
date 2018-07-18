import pygame
pygame.init()

#创建游戏窗口
screen = pygame.display.set_mode((480, 700))
#把图片加载进来
bg =pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))
#把图片加载进来
hero =pygame.image.load("./images/hero_blowup_n1.png")
#创建一个围栏
rect = pygame.Rect(150,500,102,126)

screen.blit(bg,rect)
#更新的意思
pygame.display.update()
#游戏时钟
clock = pygame.time.Clock()
i = 0
while True:
    clock.tick(60)
    i+=1    
    rect.y-=3
    screen.blit(bg,(0,0))
    screen.blit(hero,rect)
    if rect.bottom ==0:
        rect.top = 700  
    #监听
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
pygame.quit()

