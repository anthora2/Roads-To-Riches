import os
import pygame

# Constants used across many files

#size of window
WIDTH = 1700
HEIGHT = 900

#Num rows and columns on grid
ROWS = 9
COLUMNS = 13

#Tile Size
SQUARE_SIZE = HEIGHT//ROWS

# Having global variables for the selected card and hand may work for now with single player
# but if we do implement multiplayer we will likely have to create a Player class that keeps track
# of that information separately
currentHand = []
currentCard = None
maxHandSize = 7

YELLOW_GREEN = (154, 205, 50)
DARKER_GREEN = (107, 142, 35)
RED = (255, 0, 0)
GREEN = (0,255,0)


