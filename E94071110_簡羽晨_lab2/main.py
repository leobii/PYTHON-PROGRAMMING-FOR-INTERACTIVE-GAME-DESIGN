import pygame
import time

# clock
clock = pygame.time.Clock()

# setup
WIN_WIDTH = 1024
WIN_HEIGHT = 600
BTN_WIDTH = 80
BTN_HEIGHT = 80
HP_WIDTH = 40
HP_HEIGHT = 40
FPS = 30

bcw = BTN_WIDTH*4    # bcw, bch define the width and height of a container that will fill buttons
bch = 80
hcw = HP_WIDTH*5   # hcw, hch define the width and height of a container that will fill hps
hch = 80

# initialization
pygame.init()
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# set the title
pygame.display.set_caption("My first game")

# load image (background, enemy, buttons)
background_image = pygame.transform.scale(pygame.image.load("images/Map.png"), (WIN_WIDTH, WIN_HEIGHT))
enemy_image = pygame.transform.scale(pygame.image.load("images/enemy.png"), (70, 70))
muse_image = pygame.transform.scale(pygame.image.load("images/muse.png"), (BTN_WIDTH, BTN_HEIGHT))
pause_image = pygame.transform.scale(pygame.image.load("images/pause.png"), (BTN_WIDTH, BTN_HEIGHT))
sound_image = pygame.transform.scale(pygame.image.load("images/sound.png"), (BTN_WIDTH, BTN_HEIGHT))
continue_image = pygame.transform.scale(pygame.image.load("images/continue.png"), (BTN_WIDTH, BTN_HEIGHT))
hp_image = pygame.transform.scale(pygame.image.load("images/hp.png"), (HP_WIDTH, HP_HEIGHT))
hp_gray_image = pygame.transform.scale(pygame.image.load("images/hp_gray.png"), (HP_WIDTH, HP_HEIGHT))

# Calculate one's position(x,y)
# i:x軸上的第幾個 / j:y軸上的第幾個 / total_x:x軸上總共有幾個 / total_y:y軸上總共有幾個 /
# cx:container的x座標 / cy:container的y座標 / cw:container的寬(width) / ch:container的長(height) /
# w:物體的寬 / h:物體的高
def position(i, j, total_x, total_y, cx, cy, cw, ch, w, h):
    x = cx + (cw-(w*total_x))/2 + i*w
    y = cy + (ch-(h*total_y))/2 + j*h
    return x, y


class Game:
    def __init__(self):
        # window
        # ...(to be done)

        # hp settings
        self.hp = 7
        self.max_hp = 10

        # get the time when the game start
        #self.now = time.localtime().tm_sec
        self.start_time = time.time()

        pass

    def game_run(self):
        # game loop
        run = True
        while run:
            # event loop
            clock.tick(FPS)
            # event loop (user action)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # draw background
            win.blit(background_image, (0, 0))

            # draw enemy and health bar
            win.blit(enemy_image, (300, 150))
            pygame.draw.rect(win, (255, 0, 0), [285, 135, 100, 8])

            # draw menu
            pygame.draw.rect(win, (0, 0, 0), [0, 0, WIN_WIDTH, 80])

            # draw buttons
            # pygame.draw.rect(win, (255, 0, 0), [WIN_WIDTH - bcw, 0, bcw, bch])        # buttons' container
            for i in range(0, 4):
                x, y = position(i, 0, 4, 1, WIN_WIDTH - bcw, 0, bcw, bch, BTN_WIDTH, BTN_HEIGHT)
                if i == 0:
                    name = muse_image
                elif i == 1:
                    name = sound_image
                elif i == 2:
                    name = continue_image
                elif i == 3:
                    name = pause_image
                win.blit(name, (x, y + 4))

            # draw hps
            # pygame.draw.rect(win, (255, 0, 0), [(WIN_WIDTH-hcw)/2, 0, hcw, hch])        # hps' container
            for j in range(0, 2):
                for i in range(0, int(self.max_hp / 2)):
                    x, y = position(i, j, self.max_hp / 2, 2, (WIN_WIDTH - hcw) / 2, 0, hcw, hch, HP_WIDTH, HP_HEIGHT)
                    if (j == 1) and (i >= self.hp - self.max_hp / 2):
                        win.blit(hp_gray_image, (x, y))
                    else:
                        win.blit(hp_image, (x, y))

            # draw time
            '''
            >> print(time.localtime())
            time.struct_time(tm_year=2021, tm_mon=7, tm_mday=26, tm_hour=23, tm_min=32, tm_sec=3, tm_wday=0, tm_yday=207, tm_isdst=0)
            
            >> print(time.strftime("%M:%S", time.localtime()))
            32:03
            
            >> print(time.time())
            1627313523.2717025
            '''

            # time_interval = time.localtime(time.time()).tm_sec-self.now
            # ---> ERROR: 如果只取秒數相減，time_interval會受self.now的秒數影響，因此time_interval並非經過的時間

            time_interval = int(time.time()-self.start_time)//1
            print("%01.0f:%02.0f" % ((time_interval // 60), (time_interval % 60)))     # 用0填充空白

            '''
            # 改字體、大小：
            字體變數 = pygame.font.SysFont(字體名稱, 字體尺寸)
            # 繪製：
            文字變數 = 字體變數.render(文字, 平滑值, 文字顏色, 背景顏色)
            '''

            font = pygame.font.SysFont("simhei", 30)
            text = font.render("%01.0f:%02.0f" % ((time_interval // 60), (time_interval % 60)), True, (255, 255, 255), (0, 0, 0))
            # print(text.get_width(), text.get_height())
            pygame.draw.rect(win, (0, 0, 0), [0, 560, 80, 40])      # 文字底框
            x, y = position(0, 0, 1, 1, 0, 560, 80, 40, text.get_width(), text.get_height())
            win.blit(text, (x, y))        # 印出文字


            pygame.display.update()


if __name__ == "__main__":
    covid_game = Game()
    covid_game.game_run()
