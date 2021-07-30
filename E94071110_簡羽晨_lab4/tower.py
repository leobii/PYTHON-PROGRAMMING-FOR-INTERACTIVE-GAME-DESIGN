import pygame
import os
import math
from settings import WIN_WIDTH, WIN_HEIGHT
from enemy import Enemy

TOWER_IMAGE = pygame.image.load(os.path.join("images", "rapid_test.png"))

class TowerGroup:
    def __init__(self):
        self.constructed_tower = [Tower(250, 380), Tower(420, 400), Tower(600, 400)]

    def get(self):
        return self.constructed_tower


class Tower:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(TOWER_IMAGE, (70, 70))  # image of the tower
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # center of the tower
        self.range = 150  # tower attack range
        self.damage = 2   # tower damage
        self.range_circle = Circle(self.rect.center, self.range)  # attack range circle (class Circle())
        self.cd_count = 0  # used in self.is_cool_down()
        self.cd_max_count = 60  # used in self.is_cool_down()
        self.is_selected = False  # the state of whether the tower is selected
        self.type = "tower"

    def is_cool_down(self):
        """
        Q2.1) Return whether the tower is cooling down
        (1) Use a counter(self.cd_count) to compute whether the tower is cooling down
        :return: Bool
        """
        if self.cd_count < self.cd_max_count:
            self.cd_count += 1
            return False
        else:
            self.cd_count = 0
            return True

    def attack(self, enemy_group):
        """
        Q2.3) Attack the enemy.
        (1) check the the tower is cool down ((self.is_cool_down()
        (2) if the enemy is in attack range, then enemy get hurt. ((Circle.collide(), enemy.get_hurt()
        :param enemy_group: EnemyGroup()
        :return: None
        """
        '''
        if enemy_group.get():
            if self.is_cool_down() & self.range_circle.collide(enemy_group.get()[0]):
                enemy_group.get()[0].get_hurt(self.damage)
        '''
        u = Enemy()
        if self.is_cool_down():
            for en in enemy_group.get():
                if self.range_circle.collide(en):
                    u = en
                    u.get_hurt(self.damage)
                    break

    def is_clicked(self, x, y):
        """
        Bonus) Return whether the tower is clicked
        (1) If the mouse position is on the tower image, return True
        :param x: mouse pos x
        :param y: mouse pos y
        :return: Bool
        """
        if math.sqrt((x - self.rect.center[0])**2 + (y - self.rect.center[1])**2) < 35:         # 如果mouse點擊的地方和tower中心的距離<35
            return True                                                                         # 代表mouse點到了
        else:
            return False

    def get_selected(self, is_selected):
        """
        Bonus) Change the attribute self.is_selected
        :param is_selected: Bool
        :return: None
        """
        self.is_selected = is_selected

    def draw(self, win):
        """
        Draw the tower and the range circle
        :param win:
        :return:
        """
        # draw range circle
        if self.is_selected:
            self.range_circle.draw_transparent(win)
        # draw tower
        win.blit(self.image, self.rect)


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def draw_transparent(self, win):
        """
        Q1) draw the tower effect range, which is a transparent circle.
        :param win: window surface
        :return: None
        """
        # create semi-transparent surface
        transparent_surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)          # 設定畫布大小
        transparency = 90                               # define transparency: 0~255, 0 is fully transparent
        # draw the rectangle on the transparent surface
        # pygame.draw.circle(畫布, 顏色, [x坐標, y坐標], 半徑, 線寬)
        pygame.draw.circle(transparent_surface, (127, 127, 127, transparency), self.center, self.radius, 0)
        win.blit(transparent_surface, (0, 0))                                   # 畫出整個畫布，並設定畫在哪裡(位置)

    def collide(self, enemy):
        """
        Q2.2)check whether the enemy is in the circle (attack range), if the enemy is in range return True
        :param enemy: Enemy() object
        :return: Bool
        """
        x1, y1 = enemy.get_pos()        # 取得enemy的位置
        '''
        for i in range(self.radius):
            if ((x1 < self.center[0] - i) & (y1 < self.center[1] - self.radius + i)) \
            | ((x1 < self.center[0] - i) & (y1 < self.center[1] + self.radius + i)) \
            | ((x1 > self.center[0] - i) & (y1 < self.center[1] - self.radius + i)) \
            | ((x1 > self.center[0] - i) & (y1 < self.center[1] + self.radius + i)):
                return True
            else:
                return False
        '''
        if math.sqrt((x1-self.center[0])**2 + (y1-self.center[1])**2) < self.radius:            # 如果enemy的位置和tower中心的距離<圓圈半徑內
            return True                                                                         # 表示enemy在暴風範圍內
        else:
            return False
