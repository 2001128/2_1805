import pygame
from GameSprite import *
class PlanMain():
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(CREATE_ENEMY_EVENT,800)
        pygame.time.set_timer(CREATE_BULLET_EVENT,300)

        self.enemy_group = pygame.sprite.Group()#创建敌机精灵组
        self.__create_sprites()
        
    def start_game(self):
        """开始游戏"""
         
        print("开始游戏...")
         
       
        while True:

            # 1. 设置刷新帧率
            self.clock.tick(60)

            # 2. 事件监听
            self.__event_handler()

            # 3. 碰撞检测
            self.__check_collide()

            # 4. 更新精灵组
            self.__update_sprites()

            # 5. 更新屏幕显示
            pygame.display.update()
            
    def __event_handler(self):
        """事件监听"""
              
        for event in pygame.event.get():
           
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = EnemySprite()
                self.enemy_group.add(enemy)
            
            elif event.type == CREATE_BULLET_EVENT:
                self.herosprite.fire()                
   
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.herosprite.speed = 10
        elif keys_pressed[pygame.K_LEFT]:
            self.herosprite.speed = -10
        else:
            self.herosprite.speed = 0
            
             
    def __check_collide(self):
        """碰撞检测"""
        pygame.sprite.groupcollide(self.enemy_group,self.herosprite.bullet_group,True,True)
        enemies = pygame.sprite.spritecollide(self.herosprite,self.enemy_group,True)
        if len(enemies) > 0:
            self.herosprite.kill()
            PlanMain.__game_over()
    def __update_sprites(self):
        """更新精灵组"""
        self.bg_group.update()
        self.bg_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        
        self.herosprite.bullet_group.update()
        self.herosprite.bullet_group.draw(self.screen)
    def __create_sprites(self):
        '''创建精灵组'''
        bg1 = BackGroundSprite()
        bg2 = BackGroundSprite(True)
        self.bg_group = pygame.sprite.Group(bg1,bg2)
        
        self.herosprite = HeroSprite()
        self.hero_group = pygame.sprite.Group(self.herosprite)
    @staticmethod
    def __game_over():
       """游戏结束"""

       print("游戏结束")
       pygame.quit()
       exit()
if __name__ == "__main__":
    planmain = PlanMain()
    planmain.start_game()



