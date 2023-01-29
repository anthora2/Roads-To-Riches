import pygame
from constants import * 
from grid import *
from GameHandler import *
from startscreen import *
from hotbar import *
from Tiles import StraightRoad, BendedTurn #this is just to test to see if draw card works


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ROADS TO RICHES")
FPS = 60

def main():
    run = True
    clock = pygame.time.Clock()
    start_screen(WINDOW)

    # Main Game Loop
    mainGrid = Grid()
    #mainGrid.DisplayInternalGrid()
    #mainGrid.DisplayInternalCoords()
    mainGrid.DrawExternalGrid(WINDOW)
    #drawCard(StraightRoad.StraightRoad(0, 0), WINDOW, 1)
    #drawCard(BendedTurn.BendedTurn(0, 0), WINDOW, 2)
    startingRoads = [BendedTurn.BendedTurn(0, 0), StraightRoad.StraightRoad(0, 0), BendedTurn.BendedTurn(0, 0), BendedTurn.BendedTurn(0, 0)]
    convertToCards(startingRoads)
    drawOrderedCards(WINDOW)
    #print(currentHand)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # MOUSEBUTTONDOWN = 1 = left click, 2 = middle click, 3 = right click
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()    #here we have to check if the position of the mouse was on grid or on card in hand
                    #function to check which one it pressed, function will also take in coordinates (x, y)
                    mainGrid.PlaceRoad(x, y)
                    mainGrid.DrawExternalGrid(WINDOW)
                elif event.button == 3:
                    # Right click should rotate the selected Toad Tile from the hotbar
                    pass
                
        
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()