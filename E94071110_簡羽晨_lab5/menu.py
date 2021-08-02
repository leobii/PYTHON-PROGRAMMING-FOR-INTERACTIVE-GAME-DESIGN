import pygame
import os

MENU_IMAGE = pygame.image.load(os.path.join("images", "upgrade_menu.png"))
UPGRADE_BTN_IMAGE = pygame.image.load(os.path.join("images", "upgrade.png"))
SELL_BTN_IMAGE = pygame.image.load(os.path.join("images", "sell.png"))
# the width and the height of menu, upgrade button and sell button
MENU_IMAGE_w = 170
MENU_IMAGE_h = 170
UPGRADE_BTN_IMAGE_w = 50
UPGRADE_BTN_IMAGE_h = 20
SELL_BTN_IMAGE_w = 30
SELL_BTN_IMAGE_h = 30


class UpgradeMenu:
    def __init__(self, x, y):       # x and y are set for the center of the menu
        self.__buttons = [Button(UPGRADE_BTN_IMAGE, "upgrade", x, y - 60), Button(SELL_BTN_IMAGE, "sell", x, y + 64)]  # (Q2) Add buttons here
        self.image = pygame.transform.scale(MENU_IMAGE, (MENU_IMAGE_w, MENU_IMAGE_h))
        self.x = x
        self.y = y

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons (因為這兩個不會分開顯示所以放在同一個地方畫)
        (This method is called in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.image, (self.x - MENU_IMAGE_w/2, self.y - MENU_IMAGE_h/2))
        # draw button
        win.blit(self.__buttons[0].image, (self.__buttons[0].rect))
        win.blit(self.__buttons[1].image, (self.__buttons[1].rect))

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons


class Button:
    def __init__(self, image, name, x, y):      # x and y are set for the center of buttons
        self.name = name
        if name == "sell":
            self.image = pygame.transform.scale(image, (SELL_BTN_IMAGE_w, SELL_BTN_IMAGE_h))
        elif name == "upgrade":
            self.image = pygame.transform.scale(image, (UPGRADE_BTN_IMAGE_w, UPGRADE_BTN_IMAGE_h))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        if self.rect.collidepoint(x, y) == 1:
            #print(self.rect.collidepoint(x, y))
            return True
        else:
            #print(self.rect.collidepoint(x, y))
            return False

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name