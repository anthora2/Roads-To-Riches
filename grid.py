import pygame
from constants import *
from Tiles import Grass, Airport, Casino, \
                  StraightRoad, BendedTurn, T_Intersection, FourWay, RoadBlock

class Grid:
    """Grid class used for keeping track of the roads data and displays the board"""
    def __init__(self):
        """The grid is made using a list of lists to create a 2D matrix"""
        # Grass grid holds the Tiles for the background to be drawn before the roads
        self.grass_grid  = [[] for _ in range(ROWS)]
        alternator = False
        for row in range(ROWS):
            for col in range(COLUMNS):
                if alternator is False:
                    self.grass_grid[row].append(Grass.Grass(col*SQUARE_SIZE, row*SQUARE_SIZE, 1))
                else:
                    self.grass_grid[row].append(Grass.Grass(col*SQUARE_SIZE, row*SQUARE_SIZE, 2))
                alternator = not alternator
        
        # Road grid holds the structure/road Tiles at each coordinate pair. Value is None if there is no structure
        self.road_grid = [[None for _ in range(COLUMNS)] for _ in range(ROWS)]
        middle_col, middle_row = COLUMNS//2, ROWS//2
        first_col, last_col = 0, COLUMNS-1
        self.road_grid[middle_row][middle_col] = Airport.Airport(middle_col*SQUARE_SIZE, middle_row*SQUARE_SIZE)     # Airport
        self.road_grid[middle_row][first_col] = Casino.Casino(first_col*SQUARE_SIZE, middle_row*SQUARE_SIZE, 1, 1)   # Casino 1
        self.road_grid[middle_row][last_col] = Casino.Casino(last_col*SQUARE_SIZE, middle_row*SQUARE_SIZE, 2, 2)     # Casino 2
        
        # Devious nested list comprehension version of the code. Can be used to optimalize the speed of creating the grid but it's pretty overkill
        """
        self.grass_grid  = [ [Grass.Grass(row*SQUARE_SIZE, col*SQUARE_SIZE, 1) if (col % 2 == 0) else 
                              Grass.Grass(row*SQUARE_SIZE, col*SQUARE_SIZE, 2) for col in range(COLUMNS)] if (row % 2 == 0) else 
                             [Grass.Grass(row*SQUARE_SIZE, col*SQUARE_SIZE, 2) if (col % 2 == 0) else 
                              Grass.Grass(row*SQUARE_SIZE, col*SQUARE_SIZE, 1) for col in range(COLUMNS)] for row in range(ROWS) ]
        """


    def DisplayInternalGrid(self):
        """Prints a formatted grid with the Tile type at each index to the console for debugging"""
        # Get the longest text for spacing
        padding = 0
        for row in self.road_grid:
            for col in row:
                if len(repr(col)) > padding:
                    padding = len(repr(col))
        # Print the list with appropriate spacing
        for row in self.road_grid:
            print("[", end="")
            for col in range(len(row)):
                if col != len(row)-1:
                    print(repr(row[col]).ljust(padding)+" , ", end="")
                else:
                    print(repr(row[col]).ljust(padding), end="")
            print("]")
        # Print the dimensions of the grid as well
        print("Grid Dimensions: Width x Height = " + str(len(self.road_grid[0])) + " x " + str(len(self.road_grid)))
    

    def DisplayInternalCoords(self):
        """Prints a formatted grid with the coordinates at each index to the console for debugging"""
        # Get the longest text for spacing
        padding = 0
        for row in self.grass_grid:
            for col in row:
                if len(str(col.GetCoords())) > padding:
                    padding = len(str(col.GetCoords()))
        # Print the list with appropriate spacing
        for row in self.grass_grid:
            print("[", end="")
            for col in range(len(row)):
                if col != len(row)-1:
                    print(str(row[col].GetCoords()).ljust(padding)+" , ", end="")
                else:
                    print(str(row[col].GetCoords()).ljust(padding), end="")
            print("]")
        # Print the dimensions of the grid as well
        print("Grid Dimensions: Width x Height = " + str(len(self.grass_grid[0])) + " x " + str(len(self.grass_grid)))

 
    def DrawExternalGrid(self, window):
        """Draws all of the Tiles from the grid onto the window"""
        for row in range(ROWS):
            for col in range(COLUMNS):
                # Draw the background Tile first and then the Road on top of it, if there is one
                resizedIMG = pygame.transform.scale(self.grass_grid[row][col].image, (SQUARE_SIZE, SQUARE_SIZE))
                window.blit(resizedIMG, self.grass_grid[row][col].GetCoords())
                if self.road_grid[row][col] is not None:    # Draw Road
                    resizedIMG = pygame.transform.scale(self.road_grid[row][col].image, (SQUARE_SIZE, SQUARE_SIZE))
                    window.blit(resizedIMG, self.grass_grid[row][col].GetCoords())


    def PlaceRoad(self, x:int, y:int):
        """Takes in the mouse coordinates and finds what index of the grid that is to place the Road Tile"""
        try:
            row, col = y//SQUARE_SIZE, x//SQUARE_SIZE
            if self.road_grid[row][col] is not None:  # Do not place a road if the space is already taken 
                return
            self.road_grid[row][col] = StraightRoad.StraightRoad(col*SQUARE_SIZE, row*SQUARE_SIZE)
        except IndexError:
            print("ERROR: Cannot place a road outside of the board")
