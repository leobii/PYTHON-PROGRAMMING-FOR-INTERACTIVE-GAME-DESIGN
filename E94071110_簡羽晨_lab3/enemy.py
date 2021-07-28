import pygame
import math
import os
from settings import PATH_l, PATH_r

pygame.init()
ENEMY_IMAGE = pygame.image.load(os.path.join("images", "enemy.png"))

# 這個class是在定義Enemy本身的東西，包含位置、繪圖、移動位置...
class Enemy:
    def __init__(self, dir):
        self.width = 50
        self.height = 50
        self.image = pygame.transform.scale(ENEMY_IMAGE, (self.width, self.height))
        self.life = 5
        self.max_life = 10
        self.lifebar_length = 50
        self.path_position = 0
        self.counter = 0
        self.max_counter = 0
        self.stride = 1         # 每步步長
        # 選擇使用左邊路還是右邊路
        if dir == 0:
            self.path = PATH_l
            self.x, self.y = PATH_l[0]
        elif dir == 1:
            self.path = PATH_r
            self.x, self.y = PATH_r[0]

    def draw(self, win):
        # draw enemy
        win.blit(self.image, (self.x - self.width // 2, self.y - self.height // 2))
        # draw enemy health bar
        self.draw_lifebar(win)

    def draw_lifebar(self, win):
        """
        Draw life bar above an enemy
        :param win: window
        :return: None
        """
        ratio_of_life = self.life / self.max_life
        pygame.draw.rect(win, (0, 255, 0), [self.x - self.width // 2, (self.y - self.height // 2) - 10, self.lifebar_length * ratio_of_life, 7])
        pygame.draw.rect(win, (255, 0, 0), [(self.x - self.width // 2) + self.lifebar_length * ratio_of_life, (self.y - self.height // 2) - 10, self.lifebar_length * (1-ratio_of_life), 7])

    def move(self):
        """
        Enemy move toward path points every frame
        :return: None
        """
        ax, ay = self.path[self.path_position]                              # x, y position of start point "a" and end point "b"
        bx, by = self.path[self.path_position + 1]
        distance_of_ba = math.sqrt((bx - ax) ** 2 + (by - ay) ** 2)         # calculate the distance between a and b
        self.max_counter = int(distance_of_ba / self.stride)                # total footsteps that needed from A to B
        unit_vector_x = (bx - ax) / distance_of_ba
        unit_vector_y = (by - ay) / distance_of_ba

        if self.counter == self.max_counter:                    # 若self.counter == self.max_counter，表示已經走到end point了
            self.counter = 0                                    # 所以讓self.counter歸零
            if self.path_position <= len(self.path) - 3:        # 若self.path_position <= len(self.path) - 3，表示還沒走到整條path的終點
                self.path_position += 1                         # 所以可以再往前到path的下一個位置
        elif self.counter < self.max_counter:           # update the coordinate
            delta_x = unit_vector_x * self.stride
            delta_y = unit_vector_y * self.stride
            self.x += delta_x
            self.y += delta_y
            self.counter += 1


# 這個class是在定義EnemyGroup的產生和輸出...
class EnemyGroup:
    def __init__(self):
        self.camp_count = 0
        self.gen_count = 0
        self.camp_period = 120   # (unit: frame)
        self.reserved_members = []
        self.dir = 0            # 用來辨別enemy要走左邊(self.dir == 0)還是右邊(self.dir == 1)
        self.expedition = []  # don't change this line until you do the EX.3

    def campaign(self):
        """
        Send an enemy to go on an expedition once 120 frame
        :return: None
        """
        if self.reserved_members:                           # 如果self.reserved_members裡面還有人在排隊，才會繼續跑下去
            self.camp_count += 1                            # 跑了一次
            if self.camp_count == self.camp_period:         # 直到跑到self.camp_period次的時候
                self.expedition.append(self.reserved_members.pop())                 # 才會產生enemy：把self.reserved_members裡的最後一項pop出來，append到self.expedition裡［因為datatype都是Energy(self.dir)這個object］
                self.camp_count = 0
                if self.reserved_members == []:             # 當reserved_members清空，表示下一次enemy要換邊跑出來
                    if self.dir == 0:                       # 底下判斷enemy要換哪邊
                        self.dir = 1
                    elif self.dir == 1:
                        self.dir = 0

    def generate(self, num):                                    # 從main.py可以知道，當玩家按下鍵盤'n'後會跑來這裡
        """
        Generate the enemies in this wave
        :param num: enemy number
        :return: None
        """
        for i in range(num):
            self.reserved_members.append(Enemy(self.dir))       # 將num個enemy放進self.reserved_members排隊，等待在campaign裡輸出
        self.gen_count += 1

    def get(self):
        """
        Get the enemy list
        """
        return self.expedition                                      # 知道現在self.expedition裡有幾個enemy

    def is_empty(self):
        """
        Return whether the enemy is empty (so that we can move on to next wave)
        """
        return False if self.reserved_members else True             # 判斷self.reserved_members空了嗎(還有沒有人排隊)

    def retreat(self, enemy):
        """
        Remove the enemy from the expedition
        :param enemy: class Enemy()
        :return: None
        """
        self.expedition.remove(enemy)
