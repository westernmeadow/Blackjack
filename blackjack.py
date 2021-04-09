# -*- coding: utf-8 -*-
"""
Created on Sat May  2 17:45:47 2020

@author: ecker
"""

import pygame, Card, Player, random

def main():
    pygame.init()
    
    black = (0,0,0)
    white = (255, 255, 255)
    green = (30, 160, 75)
    red = (255, 0, 0)
    size = (700, 500)
    
    screen = pygame.display.set_mode(size)
    
    
    cardY = 350
    pygame.display.set_caption('Blackjack')
    
    #hitButton = pygame.image.load('hit.png')
    #standButton = pygame.image.load('stand.png')
    hitButton = pygame.Rect(500, 250, 100, 50)
    standButton = pygame.Rect(500, 310, 100, 50)
    quitButton = pygame.Rect(680, 0, 20, 20)
    restartButton = pygame.Rect(500, 190, 100, 50)
    
    # Building the deck
    deck = []
    suits = ('d', 'c', 'h', 's')
    for suit in suits:
        for value in range(1, 14):
            image = suit + str(value) + ".png"
            if value > 10:
                newCard = Card.Card(10, image)
            else:
                newCard = Card.Card(value, image)
            deck.append(newCard)
    
    
    random.shuffle(deck)
    p1Hand = []
    houseHand = []
    p1 = Player.Player(p1Hand)
    house = Player.House(houseHand)
    
    p1.hit(deck).flip()
    p1.hit(deck).flip()
    house.hit(deck).flip()
    house.hit(deck)
    
    carryOn = True
    
    clock = pygame.time.Clock()
    
    while carryOn:
        cardX = 250
        hCardX = 250
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #user quits the game
                carryOn = False
                
            if event.type == pygame.MOUSEBUTTONDOWN: #user clicks mouse
                mouse_pos = event.pos #gets mouse position
                
                if hitButton.collidepoint(mouse_pos) and p1.getStatus(): #if user clicks Hit
                    p1.hit(deck).flip()
                    print('Hit') #call hit
                    if not p1.getStatus():
                        house.getHand()[1].flip()
                
                if standButton.collidepoint(mouse_pos) and p1.getStatus(): #if user clicks Stand
                    p1.stand()
                    print('Stand')
                    if not p1.getStatus():
                        house.getHand()[1].flip()
                
                if quitButton.collidepoint(mouse_pos): #quit game
                    pygame.quit()
                    
                if restartButton.collidepoint(mouse_pos) and not p1.getStatus(): #restart game
                    main()
            
            if not p1.getStatus() and house.getStatus():
                houseHandValue, hasEleven = house.getHandValue()
                if houseHandValue < 17:
                    house.hit(deck).flip()
                elif houseHandValue == 17 and hasEleven:
                    house.hit(deck).flip()
                else:
                    house.stand()
            
        
        #Player.getHand returns a list hand filled with cards
        screen.fill(green)
        for card in p1.getHand(): #draw the players hand
            screen.blit(pygame.image.load('cards\\' + card.getImage()), (cardX, cardY))
            cardX = cardX + 20 
    
       
        for cards in house.getHand(): #draw the houses hand
            screen.blit(pygame.image.load('cards\\' + cards.getImage()), (hCardX, 100))
            hCardX = hCardX + 20
        
        
        if not p1.getStatus() and not house.getStatus():
            pygame.draw.rect(screen, white, restartButton)
            screen.blit(pygame.font.SysFont('Arial', 25).render('Restart', True, black), (510, 200))
            playerHandValue = p1.getHandValue()
            houseHandValue = house.getHandValue()[0]
            if playerHandValue <= 21 and houseHandValue <= 21:
                if playerHandValue > houseHandValue:
                    screen.blit(pygame.font.SysFont('Arial', 25).render('You win!', True, black), (250, 250))
                elif houseHandValue > playerHandValue:
                    screen.blit(pygame.font.SysFont('Arial', 25).render('You lose!', True, black), (250, 250))     
                else:
                    screen.blit(pygame.font.SysFont('Arial', 25).render('Draw!', True, black), (250, 250))
            elif playerHandValue <= 21 and houseHandValue > 21:
          			screen.blit(pygame.font.SysFont('Arial', 25).render('You win!', True, black), (250, 250))
            elif playerHandValue > 21 and houseHandValue <= 21:
              	screen.blit(pygame.font.SysFont('Arial', 25).render('You lose!', True, black), (250, 250))
            else:
                screen.blit(pygame.font.SysFont('Arial', 25).render('Draw!', True, black), (250, 250))
            
    
        pygame.draw.rect(screen, red, quitButton)
        screen.blit(pygame.font.SysFont('Arial', 25).render('X', True, black), (682, -5))
        pygame.draw.rect(screen, white, hitButton)
        screen.blit(pygame.font.SysFont('Arial', 25).render('Hit', True, black), (530, 260))
        pygame.draw.rect(screen, white, standButton)
        screen.blit(pygame.font.SysFont('Arial', 25).render('Stand', True, black), (520, 320))

        pygame.display.flip() #update display
        clock.tick(60) #update rate
    pygame.quit()
    quit()
    
if __name__ == "__main__":
    main()
