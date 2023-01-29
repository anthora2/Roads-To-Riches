import pygame
import random
from constants import *
from Tiles import Road, StraightRoad, BendedTurn, T_Intersection, FourWay, RoadBlock


def CheckGameWon(grid) -> tuple[bool, str]:
    """Returns True if the game has been won and the player who won"""
    # One way to make the search possibly faster is to first check if any of the adjacent tiles around
    # the airport or any of the casinos do not have a single road attached to them therefore meaning there
    # is definitely not a connection yet between the aiport and the road.
    # LOGIC: if there are no roads connected to either casino, then the game is definitely not won yet
    def SearchTree(grid, parent_row, parent_col):
        """Used to recursively search the branches of the roads"""
        pass
    


def CheckLegalMove(grid, selected_road, x:int, y:int) -> bool:
        """Takes in the selected road and the x and y coords of where the road is trying to be placed 
           and returns True if the placement is legal"""
        # Illegal moves can be made around the Casinos
        # #TODO: Make the logic not allow players to build roads off of their casino
        row, col = y//SQUARE_SIZE, x//SQUARE_SIZE
        adjacent_roads = GetAdjacentRoads(grid, row, col)
        connections_made = 0
        # Check Up
        if (adjacent_roads[0] != None):
            road = grid.road_grid[adjacent_roads[0][0]][adjacent_roads[0][1]]
            if (selected_road.up == road.down):
                connections_made += 1
            elif (repr(road) in ["Casino 1", "Casino 2"]):
                pass    
            else:
                return False

        # Check Down
        if (adjacent_roads[1] != None):
            road = grid.road_grid[adjacent_roads[1][0]][adjacent_roads[1][1]]
            if (selected_road.down == road.up):
                connections_made += 1
            elif (repr(road) in ["Casino 1", "Casino 2"]):
                pass    
            else:
                return False
        
        # Check Left
        if (adjacent_roads[2] != None):
            road = grid.road_grid[adjacent_roads[2][0]][adjacent_roads[2][1]]
            if (selected_road.left == road.right):
                connections_made += 1
            elif (repr(road) in ["Casino 1", "Casino 2"]):
                pass    
            else:
                return False

        # Check Right
        if (adjacent_roads[3] != None):
            road = grid.road_grid[adjacent_roads[3][0]][adjacent_roads[3][1]]
            if (selected_road.right == road.left):
                connections_made += 1
            elif (repr(road) in ["Casino 1", "Casino 2"]):
                pass    
            else:
                return False

        # If there was at least one connection and no illegal connections, return True
        return True if connections_made >= 1 else False


def CreateStartingHand():
    """Adds the max amount of cards to the players hand at the start"""
    global currentHand
    if currentHand:  # Clear the player's hand if there are already cards
        currentHand = []
    for _ in range(maxHandSize):
        currentHand.append( random.choices([StraightRoad.StraightRoad(0,0), BendedTurn.BendedTurn(0,0), 
                                            T_Intersection.T_Intersection(0,0), FourWay.FourWay(0,0), RoadBlock.RoadBlock(0,0)], 
                                           weights=[8, 10, 8, 7, 3], k=1)[0] )


def DrawCard():
    """Adds a single card to the player's hand"""
    global currentHand
    if len(currentHand) < maxHandSize:
        currentHand.append( random.choices([StraightRoad.StraightRoad(0,0), BendedTurn.BendedTurn(0,0), 
                                            T_Intersection.T_Intersection(0,0), FourWay.FourWay(0,0), RoadBlock.RoadBlock(0,0)], 
                                           weights=[8, 10, 8, 7, 3], k=1)[0] )
    else:
        print("ERROR: Hand already at max, could not draw another card")


def GetChildRoads(grid, row:int, col:int, parent_row:int, parent_col:int) -> list[tuple[int, int]]:
    """Returns a list with the indices of the child roads of the current road"""
    child_roads = []
    # Check Up
    if row-1 >= 0:  # index out of range if not true
        if (grid.road_grid[row-1][col] != None) and (row-1 != parent_row and col != parent_col):
            child_roads.append( (row-1, col) )

    # Check Down
    if row+1 <= ROWS:  # index out of range if not true
        if (grid.road_grid[row+1][col] != None) and (row+1 != parent_row and col != parent_col):
            child_roads.append( (row+1, col) )

    # Check Left
    if col-1 >= 0:  # index out of range if not true
        if (grid.road_grid[row][col-1] != None) and (row != parent_row and col-1 != parent_col):
            child_roads.append( (row, col-1) )

    # Check Right
    if col+1 <= COLUMNS:  # index out of range if not true
        if (grid.road_grid[row][col+1] != None) and (row != parent_row and col+1 != parent_col):
            child_roads.append( (row, col+1) )
    
    return child_roads


def GetAdjacentRoads(grid, row:int, col:int) -> list[tuple[int, int]]:
    """Returns a list with the indices of each adjacent tile to the provided road.
       If there is not a road at a position, the value will be None for that index.
       Index Values: 0 = up, 1 = down, 2 = left, 3 = right"""
    adjacent_roads = []
    # Check Up
    if row-1 >= 0:  # index out of range if not true
        if grid.road_grid[row-1][col] != None:
            adjacent_roads.append( (row-1, col) )
        else:
            adjacent_roads.append(None)

    # Check Down
    if row+1 <= ROWS:  # index out of range if not true
        if grid.road_grid[row+1][col] != None:
            adjacent_roads.append( (row+1, col) )
        else:
            adjacent_roads.append(None)

    # Check Left
    if col-1 >= 0:  # index out of range if not true
        if grid.road_grid[row][col-1] != None:
            adjacent_roads.append( (row, col-1) )
        else:
            adjacent_roads.append(None)

    # Check Right
    if col+1 <= COLUMNS:  # index out of range if not true
        if grid.road_grid[row][col+1] != None:
            adjacent_roads.append( (row, col+1) )
        else:
            adjacent_roads.append(None)
    
    return adjacent_roads