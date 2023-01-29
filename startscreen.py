import pygame 
import os
from button import *
from constants import *




real_path = os.path.dirname(os.path.realpath(__file__))

background_image = pygame.image.load(os.path.join(real_path, 'startscreen-images', 'pygame_background2.png'))
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
title_image = pygame.image.load(os.path.join(real_path, 'startscreen-images', 'title_image2.png'))
singleplayer_image = pygame.image.load(os.path.join(real_path, 'startscreen-images', 'singleplayer_image.png'))
multiplayer_image = pygame.image.load(os.path.join(real_path, 'startscreen-images', 'multiplayer_image.png'))
gameover_image = pygame.image.load(os.path.join(real_path, 'startscreen-images', 'gameover.png'))
gameover_image = pygame.transform.scale(pygame.image.load(os.path.join(real_path, 'startscreen-images', 'gameover.png')), (600, 100))
playagain_image = pygame.image.load(os.path.join(real_path, 'startscreen-images', 'playagain.png'))
yesPlayAgain_image = pygame.image.load(os.path. join(real_path, 'startscreen-images', 'yesplayagain.png'))
noPlayAgain_image = pygame.image.load(os.path. join(real_path, 'startscreen-images', 'yesplayagain.png'))



def start_screen(window):
    multiplayer_button = Button(multiplayer_image, 640, 550, 400, 50)
    singleplayer_button = Button(singleplayer_image, 640, 400, 400, 50)

    run = True
    while run:

        window.blit(background_image, (0,0))
        window.blit(title_image, (340, 100))
        pos = pygame.mouse.get_pos()


        if singleplayer_button.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and singleplayer_button.clicked == False:
                singleplayer_button.clicked = True
                break
                print("CLICKED")
        if pygame.mouse.get_pressed()[0] == 0:
            singleplayer_button.clicked = False
        window.blit(singleplayer_button.image, singleplayer_button.rect.topleft)


        if multiplayer_button.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and multiplayer_button.clicked == False:
                multiplayer_button.clicked = True
                break
                print("CLICKED")
        if pygame.mouse.get_pressed()[0] == 0:
            multiplayer_button.clicked = False
        window.blit(multiplayer_button.image, multiplayer_button.rect.topleft)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()  #added this Wed Jan 4, 4:37 pushed it at the same time
        pygame.display.update()
    window.fill(YELLOW_GREEN)
    pygame.display.update()




def endscreen(window):
    yes_button = Button(460, 550, 440, 50)
    no_button = Button(460, 550, 440, 50)

    run = True
    while run:
        window.fill((0,0,0))
        window.blit(gameover_image, (350, 100))
        pos = pygame.mouse.get_pos()



        if yes_button.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and yes_button.clicked == False:
                yes_button.clicked = True
                break
        if pygame.mouse.get_pressed()[0] == 0:
            yes_button.clicked = False
        window.blit(yes_button.image, yes_button.rect.topleft)

        if no_button.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and no_button.clicked == False:
                no_button.clicked = True
                break
        if pygame.mouse.get_pressed()[0] == 0:
            no_button.clicked = False
        window.blit(no_button.image, no_button.rect.topleft)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()
