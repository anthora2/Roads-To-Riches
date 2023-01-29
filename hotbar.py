import pygame
from constants import *
import os, sys
import random
from Card import *

# 7 @ 110 ?
# 6 @ 130 ?
# 5 @ 150 ?
# 4 @ 170 ?
# 3 @ 190 ?
# 2 @ 210 ?
# 1 @ 230


#How spaced out the drawing of each card should be for the y coordinate
def chooseCardGap(maxCardNumber):
    base = 230
    baseCardGap = 230 - ((maxCardNumber -1) * 20)
    return baseCardGap



"""
setCards both takes in new cards to re-order them and is also used to re-order cards to move
to the front after they are pressed --> reason for two different for loops, first checks if we are adding 
new cards, second reorders all cards that are in currentHand
"""
def setCards(cardsShuffled):
    if len(currentHand) < maxHandSize:
        for card in cardsShuffled:
            currentHand.append(card)
    counter = 0
    for card in currentHand:
        card.handPosition = counter
        card.clicked = False
        counter += 1



"""
The idea is that if the code updates fast enough, we can run this function for each of the cards that are in the current hand
sum like checkPressed(currentHand[0])
         checkPressed(currentHand[1])
         checkPressed(currentHand[2])
and it will continue to check all of them and it should run so fast that they check almost instantaneously

and we want to use this function like 

if checkPressed(currentHand[0]):       so if its true (meaning it WAS pressed) it will redraw the hand
    drawOrderedCards(currentHand[0])

"""
def checkPressed(card):
    pos = pygame.mouse.get_pos()
    
    if card.rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1 and card.clicked == False:
            card.clicked = True
            return True
    if pygame.mouse.get_pressed()[0] == 0:
        card.clicked = False




"""
Function should be ran after "checkPressed". If checkPressed(card1) == True, then that same card1 should be passed into swapCards so that we 
can swap the card (to the front of hand) that was pressed. 
"""
def swapCards(pressedCard):
    position = pressedCard.handPosition
    if position == 0:
        return 
    else:
        currentHand.insert(0, currentHand.pop(currentHand[position]))
        setCards()



"""
THIS SEEMS TO BE ERRORING THE MOST

We want to draw currentHand from last to first and from top to bottom. Last card will be drawn first near the top, rest will overlap 
this card and be drawn a little lower, will be using the cards "handPosition" as a scaler to how much space should be between cards.
"""
def drawOrderedCards(window):
    xcoordinate = 1350
    index = len(currentHand) - 1
    if index <= 0:
        print("This shit dont work")
        return
    while index >= 0: # this is backwards, its printing the position first and then its sending it all the way to the back, think about how its actually 
        #reacting with hand.position
        random_suit = random.choice([0,1])
        currentCard = currentHand[index] 
        suitCard = currentCard.cardImages[random_suit]
        window.blit(suitCard, (xcoordinate, currentCard.handPosition * 170 + 50)) #0
        window.blit(currentCard.roadImage, (xcoordinate + 30, currentCard.handPosition * 170 + 80)) #30
        index -= 1

# this is change later, might not work righ tnow its just idae 
    for card in currentHand:
        randomSuit = random.choice([0, 1])
        suitCard = card.cardImages[randomSuit]
        window.blit(suitCard, (xcoordinate, currentCard.handPosition * 170 + 50))
        window.blit(card.roadImage, (xcoordinate + 30, card.handPosition * 170 + 80))





"""
My bad this is kind of redundant I forgot that they were roads and not cards so this is like a temporary stupid solution
Ill come back to it and make a better one. 
This is what takes in the roads from the logic section of the code; should be ran first before any of the above
"""
def convertToCards(roads):
    shuffledCards = []
    for road in roads:
        #newCardImage = newRoad.image
        #newCardRectangle = newRoad.image.get_rect()
        newCard = Card(road, road.image)
        shuffledCards.append(newCard)
    setCards(shuffledCards)


"""
def drawCard(road, window, position):
    #roadCard = Card(road) #card is already passed in, in makeHotBar
    #rectangle = pygame.Rect(1350, 50, 200, 200) # this leaves about 50 on each side, think about formula to always get that
    #pygame.draw.rect(window, (0,0,0), rectangle)
    scale = 100
    cardPadding = position * scale
    roadCard = Card(road)
    randomSuit = random.choice([0, 1])
    suitCard = roadCard.cardImages[randomSuit]
    #window.blit(suitCard, 1350, position * 10)
    window.blit(suitCard, (1350, 100 * position + cardPadding)) # want to change, just to show it changes by position 
    window.blit(roadCard.roadImage, (1350, 100 * position + 57 + cardPadding))
                                    #1410, 110
    

def makeHotBar(*roads, window):
    suitColor = random.choice([1,2])
    for road in roads:
        currentHand.append(Card(road))

"""

