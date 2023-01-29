import pygame, os
from constants import *




#Function loads card images, made to clean up code
def loadImage(imageString):
    real_path = os.path.dirname(os.path.realpath(__file__))
    image = pygame.image.load(os.path.join(real_path, 'card-images', imageString))
    return pygame.transform.scale(image, (150, 150))

#CardImages in lists so we can use random select to choose one of indices 
bendedImages = [loadImage("BendTurnCard1.png"), loadImage("BendTurnCard2.png")]
FourWayImages = [loadImage("FourWayCard1.png"), loadImage("FourWayCard2.png")]
RoadBlockImages = [loadImage("RoadBlockCard1.png"), loadImage("RoadBlockCard2.png")]
StrRoadImages = [loadImage("StrRoadCard1.png"), loadImage("StrRoadCard2.png")]
tInterImages = [loadImage("T-InterCard1.png"), loadImage("T-InterCard2.png")]




class Card():

    def __init__(self, road, roadImage):
        #self.roadImage = road.image 
        self.roadImage = pygame.transform.scale(roadImage, (92.5, 92.5))
        #self.roadImage = pygame.transform.scale(road.image, (92.5, 92.5))
        self.road = road
        self.rect = roadImage.get_rect()
        #self.rect = self.roadImage.get_rect()
        self.clicked = False
        self.handPosition = None
        self.coordinates = None
        self.cardImages = None
        self.cardType = None
        if repr(road) == "Four-Way":
            self.cardType = "King"
            self.cardImages = FourWayImages
        elif repr(road) == "Road Block":
            self.cardType = "Ace"
            self.cardImages = RoadBlockImages
        elif repr(road) == "T-Intersection":
            self.cardType = "Queen"
            self.cardImages = tInterImages
        elif repr(road) == "Straight Road":
            self.cardType = "10"
            self.cardImages = StrRoadImages
        else:
            self.cardType = "Jack"
            self.cardImages = bendedImages


    def __repr__(self):
        return repr(self.road) + " Card"















"""
class Card():

    #takes in the roadType, checks it's repr and based on repr string will set cardType to proper card suit
    def __init__(self, road):
        self.road = road
       #self.handPosition = handPosition
        self.roadImage = pygame.transform.scale(road.image, (92.5, 92.5))
        self.cardImages = None
        self.cardType = None
        if repr(road) == "Four-Way":
            self.cardType = "King"
            self.cardImages = FourWayImages
        elif repr(road) == "Road Block":
            self.cardType = "Ace"
            self.cardImages = RoadBlockImages
        elif repr(road) == "T-Intersection":
            self.cardType = "Queen"
            self.cardImages = tInterImages
        elif repr(road) == "Straight Road":
            self.cardType = "10"
            self.cardImages = StrRoadImages
        else:
            self.cardType = "Jack"
            self.cardImages = bendedImages


    def __repr__(self):
        return repr(self.road) + " Card"

"""
