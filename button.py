import pygame


class Button():

    #Arguments, image = png/jpg path, x & y are coordinates to place the image, scale_x & y are values that scale image
    def __init__(self, image, x, y, scale_x, scale_y):
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.image = pygame.transform.scale(image, (scale_x, scale_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        