import pygame
from pygame.locals import *
import random
import copy

#Load Images, updated path for functionality
icon = pygame.image.load('Blackjack-Python-master/resources/icon.png')
cBack = pygame.image.load('Blackjack-Python-master/resources/cards/cardback.png')
diamondA = pygame.image.load('Blackjack-Python-master/resources/cards/ad.png')
clubA = pygame.image.load('Blackjack-Python-master/resources/cards/ac.png')
heartA = pygame.image.load('Blackjack-Python-master/resources/cards/ah.png')
spadeA = pygame.image.load('Blackjack-Python-master/resources/cards/as.png')
diamond2 = pygame.image.load('Blackjack-Python-master/resources/cards/2d.png')
club2 = pygame.image.load('Blackjack-Python-master/resources/cards/2c.png')
heart2 = pygame.image.load('Blackjack-Python-master/resources/cards/2h.png')
spade2 = pygame.image.load('Blackjack-Python-master/resources/cards/2s.png')
diamond3 = pygame.image.load('Blackjack-Python-master/resources/cards/3d.png')
club3 = pygame.image.load('Blackjack-Python-master/resources/cards/3c.png')
heart3 = pygame.image.load('Blackjack-Python-master/resources/cards/3h.png')
spade3 = pygame.image.load('Blackjack-Python-master/resources/cards/3s.png')
diamond4 = pygame.image.load('Blackjack-Python-master/resources/cards/4d.png')
club4 = pygame.image.load('Blackjack-Python-master/resources/cards/4c.png')
heart4 = pygame.image.load('Blackjack-Python-master/resources/cards/4h.png')
spade4 = pygame.image.load('Blackjack-Python-master/resources/cards/4s.png')
diamond5 = pygame.image.load('Blackjack-Python-master/resources/cards/5d.png')
club5 = pygame.image.load('Blackjack-Python-master/resources/cards/5c.png')
heart5 = pygame.image.load('Blackjack-Python-master/resources/cards/5h.png')
spade5 = pygame.image.load('Blackjack-Python-master/resources/cards/5s.png')
diamond6 = pygame.image.load('Blackjack-Python-master/resources/cards/6d.png')
club6 = pygame.image.load('Blackjack-Python-master/resources/cards/6c.png')
heart6 = pygame.image.load('Blackjack-Python-master/resources/cards/6h.png')
spade6 = pygame.image.load('Blackjack-Python-master/resources/cards/6s.png')
diamond7 = pygame.image.load('Blackjack-Python-master/resources/cards/7d.png')
club7 = pygame.image.load('Blackjack-Python-master/resources/cards/7c.png')
heart7 = pygame.image.load('Blackjack-Python-master/resources/cards/7h.png')
spade7 = pygame.image.load('Blackjack-Python-master/resources/cards/7s.png')
diamond8 = pygame.image.load('Blackjack-Python-master/resources/cards/8d.png')
club8 = pygame.image.load('Blackjack-Python-master/resources/cards/8c.png')
heart8 = pygame.image.load('Blackjack-Python-master/resources/cards/8h.png')
spade8 = pygame.image.load('Blackjack-Python-master/resources/cards/8s.png')
diamond9 = pygame.image.load('Blackjack-Python-master/resources/cards/9d.png')
club9 = pygame.image.load('Blackjack-Python-master/resources/cards/9c.png')
heart9 = pygame.image.load('Blackjack-Python-master/resources/cards/9h.png')
spade9 = pygame.image.load('Blackjack-Python-master/resources/cards/9s.png')
diamond10 = pygame.image.load('Blackjack-Python-master/resources/cards/10d.png')
club10 = pygame.image.load('Blackjack-Python-master/resources/cards/10c.png')
heart10 = pygame.image.load('Blackjack-Python-master/resources/cards/10h.png')
spade10 = pygame.image.load('Blackjack-Python-master/resources/cards/10s.png')
diamondJ = pygame.image.load('Blackjack-Python-master/resources/cards/jd.png')
clubJ = pygame.image.load('Blackjack-Python-master/resources/cards/jc.png')
heartJ = pygame.image.load('Blackjack-Python-master/resources/cards/jh.png')
spadeJ = pygame.image.load('Blackjack-Python-master/resources/cards/js.png')
diamondQ = pygame.image.load('Blackjack-Python-master/resources/cards/qd.png')
clubQ = pygame.image.load('Blackjack-Python-master/resources/cards/qc.png')
heartQ = pygame.image.load('Blackjack-Python-master/resources/cards/qh.png')
spadeQ = pygame.image.load('Blackjack-Python-master/resources/cards/qs.png')
diamondK = pygame.image.load('Blackjack-Python-master/resources/cards/kd.png')
clubK = pygame.image.load('Blackjack-Python-master/resources/cards/kc.png')
heartK = pygame.image.load('Blackjack-Python-master/resources/cards/kh.png')
spadeK = pygame.image.load('Blackjack-Python-master/resources/cards/ks.png')
jokerR = pygame.image.load('Blackjack-Python-master/resources/cards/joker1.png')
jokerB = pygame.image.load('Blackjack-Python-master/resources/cards/joker2.png')

#Set Icon
pygame.display.set_icon(icon)

#Global Constants
black = (0,0,0)
white = (255,255,255)
gray = (192,192,192)

cards = [ diamondA, clubA, heartA, spadeA, \
          diamond2, club2, heart2, spade2, \
          diamond3, club3, heart3, spade3, \
          diamond4, club4, heart4, spade4, \
          diamond5, club5, heart5, spade5, \
          diamond6, club6, heart6, spade6, \
          diamond7, club7, heart7, spade7, \
          diamond8, club8, heart8, spade8, \
          diamond9, club9, heart9, spade9, \
          diamond10, club10, heart10, spade10, \
          diamondJ, clubJ, heartJ, spadeJ, \
          diamondQ, clubQ, heartQ, spadeQ, \
          diamondK, clubK, heartK, spadeK, \
          jokerR, jokerB ] #I messed this up lmao
cardA = [ diamondA, clubA, heartA, spadeA ]
card2 = [ diamond2, club2, heart2, spade2 ]
card3 = [ diamond3, club3, heart3, spade3 ]
card4 = [ diamond4, club4, heart4, spade4 ]
card5 = [ diamond5, club5, heart5, spade5 ]
card6 = [ diamond6, club6, heart6, spade6 ]
card7 = [ diamond7, club7, heart7, spade7 ]
card8 = [ diamond8, club8, heart8, spade8 ]
card9 = [ diamond9, club9, heart9, spade9 ]
card10 = [ diamond10, club10, heart10, spade10, \
            diamondJ, clubJ, heartJ, spadeJ, \
            diamondQ, clubQ, heartQ, spadeQ, \
            diamondK, clubK, heartK, spadeK ]
card21 = [ jokerR, jokerB ]

def getAmt(card):
    ''' Returns the amount the card is worth.
E.g. Ace is default 11. 10/Jack/Queen/King is 10.'''
    if card in cardA:
        return 11
    elif card in card2:
        return 2
    elif card in card3:
        return 3
    elif card in card4:
        return 4
    elif card in card5:
        return 5
    elif card in card6:
        return 6
    elif card in card7:
        return 7
    elif card in card8:
        return 8
    elif card in card9:
        return 9
    elif card in card10:
        return 10
    else:
        print('getAmt broke')
        exit()

def getAmtJ(card): #getAmt, but with the joker
    if card in cardA:
        return 11
    elif card in card2:
        return 2
    elif card in card3:
        return 3
    elif card in card4:
        return 4
    elif card in card5:
        return 5
    elif card in card6:
        return 6
    elif card in card7:
        return 7
    elif card in card8:
        return 8
    elif card in card9:
        return 9
    elif card in card10:
        return 10
    elif card in card21:
        return 21

def genCard(cList, xList):
    '''Generates an card from cList, removes it from cList, and appends it to xList.
Returns if card is Ace and the card itself.'''
    cA = 0
    card = random.choice(cList)
    cList.remove(card)
    xList.append(card)
    if card in cardA:
        cA = 1
    return card, cA

def initGame(cList, uList, dList):
    '''Generates two cards for dealer and user, one at a time for each.
Returns if card is Ace and the total amount of the cards per person.'''
    userA = 0
    dealA = 0
    card1, cA = genCard(cList, uList)
    userA += cA
    card2, cA = genCard(cList, dList)
    dealA += cA
    card3, cA = genCard(cList, uList)
    userA += cA
    card4, cA = genCard(cList, dList)
    dealA += cA
    return getAmt(card1) + getAmt(card3), userA, getAmt(card2) + getAmt(card4), dealA

def initGameJ(cList, uList, dList):
    #Generates two cards for dealer and user, one at a time for each.
    #Returns if card is Ace and the total amount of the cards per person.
    userA = 0
    dealA = 0

    card1, cA = genCard(cList, uList)
    userA += cA

    card2, cA = genCard(cList, dList)
    dealA += cA

    card3, cA = genCard(cList, uList)
    userA += cA

    card4, cA = genCard(cList, dList)
    dealA += cA

    return getAmtJ(card1) + getAmtJ(card3), userA, getAmtJ(card2) + getAmtJ(card4), dealA

def single_player(): #Changed name to indicate mode
    #Local Variable
    ccards = copy.copy(cards)
    stand = False
    userCard = []
    dealCard = []
    winNum = 0
    loseNum = 0
   
    #Initialize Game
    pygame.init()
    #Larger screen size
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('BlackjackGUI')
    font = pygame.font.SysFont('arial', 15)
    hitTxt = font.render('Hit', 1, black)
    standTxt = font.render('Stand', 1, black)
    restartTxt = font.render('Restart', 1, black)
    gameoverTxt = font.render('GAME OVER', 1, white)
    userSum, userA, dealSum, dealA = initGame(ccards, userCard, dealCard)

    #Fill Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background = pygame.image.load('Blackjack-Python-master/resources/table.png')

    #Change positions of buttons
    hitB = pygame.draw.rect(background, gray, (50, 525, 75, 25))
    standB = pygame.draw.rect(background, gray, (140, 525, 75, 25))
    ratioB = pygame.draw.rect(background, gray, (95, 575, 75, 50))

    #Event Loop
    while True:
        #checks if game is over
        gameover = True if (userSum >= 21 and userA == 0) or len(userCard) == 5 else False
        if len(userCard) == 2 and userSum == 21:
            gameover = True
        elif len(dealCard) == 2 and dealSum == 21:
            gameover = True

        #background needs to be redisplayed because it gets updated
        winTxt = font.render('Wins: %i' % winNum, 1, black)
        loseTxt = font.render('Losses: %i' % loseNum, 1, black)

        #checks for mouse clicks on buttons
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover or stand) and hitB.collidepoint(pygame.mouse.get_pos()):
                #gives player a card if they don't break blackjack rules
                card, cA = genCard(ccards, userCard)
                userA += cA
                userSum += getAmt(card)
                print('User: %i' % userSum) #corrected syntax error
                while userSum > 21 and userA > 0:
                    userA -= 1
                    userSum -= 10
            elif event.type == pygame.MOUSEBUTTONDOWN and not gameover and standB.collidepoint(pygame.mouse.get_pos()):
                #when player stands, the dealer plays
                stand = True
                while dealSum <= userSum and dealSum < 17:
                    card, cA = genCard(ccards, dealCard)
                    dealA += cA
                    dealSum += getAmt(card)
                    print('Dealer: %i' % dealSum) #corrected syntax error
                    while dealSum > 21 and dealA > 0:
                        dealA -= 1
                        dealSum -= 10
            elif event.type == pygame.MOUSEBUTTONDOWN and (gameover or stand) and restartB.collidepoint(pygame.mouse.get_pos()):
                #restarts the game, updating scores
                if userSum == dealSum:
                    pass
                elif userSum <= 21 and len(userCard) == 5:
                    winNum += 1
                elif userSum <= 21 and dealSum < userSum or dealSum > 21:
                    winNum += 1
                else:
                    loseNum += 1
                gameover = False
                stand = False
                userCard = []
                dealCard = []
                ccards = copy.copy(cards)
                userSum, userA, dealSum, dealA = initGame(ccards, userCard, dealCard)
                restartB = pygame.draw.rect(background, (80, 150, 15), (555, 300, 75, 25)) #Hide button during game

        #Change positioning of text w/ buttons
        screen.blit(background, (0, 0))
        screen.blit(hitTxt, (79, 525))
        screen.blit(standTxt, (156, 525))
        screen.blit(winTxt, (100, 580))
        screen.blit(loseTxt, (100, 600))

        #displays dealer's cards
        for card in dealCard:
            x = 50 + dealCard.index(card) * 110
            screen.blit(card, (x, 50))
        screen.blit(cBack, (160, 50))

        #displays player's cards
        for card in userCard:
            x = 225 + userCard.index(card) * 110
            screen.blit(card, (x, 500)) #Change position of user cards

        #when game is over, draws restart button and text, and shows the dealer's second card
        if gameover or stand:
            screen.blit(gameoverTxt, (555, 260))
            restartB = pygame.draw.rect(background, gray, (555, 300, 75, 25))
            screen.blit(restartTxt, (567, 302))
            screen.blit(dealCard[1], (160, 50))    
            
        pygame.display.update()

def single_playerJ(): #Changed name to indicate mode
    #Local Variable
    ccards = copy.copy(cards)
    stand = False
    userCard = []
    dealCard = []
    winNum = 0
    loseNum = 0
   
    #Initialize Game
    pygame.init()
    #Larger screen size
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('BlackjackGUI')
    font = pygame.font.SysFont('arial', 15)
    hitTxt = font.render('Hit', 1, black)
    standTxt = font.render('Stand', 1, black)
    restartTxt = font.render('Restart', 1, black)
    gameoverTxt = font.render('GAME OVER', 1, white)
    userSum, userA, dealSum, dealA = initGameJ(ccards, userCard, dealCard)

    #Fill Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background = pygame.image.load('Blackjack-Python-master/resources/table.png')

    #Change positions of buttons
    hitB = pygame.draw.rect(background, gray, (50, 525, 75, 25))
    standB = pygame.draw.rect(background, gray, (140, 525, 75, 25))
    ratioB = pygame.draw.rect(background, gray, (95, 575, 75, 50))

    #Event Loop
    while True:
        #checks if game is over
        gameover = True if (stand == True) or len(userCard) == 5 else False
        if len(userCard) == 2 and userSum == 21:
            gameover = True
        elif len(dealCard) == 2 and dealSum == 21:
            gameover = True
        elif userSum > 21:
            gameover = True
        elif dealSum > 21:
            gameover = True

        #background needs to be redisplayed because it gets updated
        winTxt = font.render('Wins: %i' % winNum, 1, black)
        loseTxt = font.render('Losses: %i' % loseNum, 1, black)

        #checks for mouse clicks on buttons
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover or stand) and hitB.collidepoint(pygame.mouse.get_pos()):
                #gives player a card if they don't break blackjack rules
                card, cA = genCard(ccards, userCard)
                userA += cA
                userSum += getAmtJ(card)
                print('User: %i' % userSum) #corrected syntax error
                while userSum > 21 and userA > 0:
                    userA -= 1
                    userSum -= 10
            elif event.type == pygame.MOUSEBUTTONDOWN and not gameover and standB.collidepoint(pygame.mouse.get_pos()):
                #when player stands, the dealer plays
                stand = True
                while dealSum <= userSum and dealSum < 17:
                    card, cA = genCard(ccards, dealCard)
                    dealA += cA
                    dealSum += getAmtJ(card)
                    print('Dealer: %i' % dealSum) #corrected syntax error
                    while dealSum > 21 and dealA > 0:
                        dealA -= 1
                        dealSum -= 10
            elif event.type == pygame.MOUSEBUTTONDOWN and (gameover or stand) and restartB.collidepoint(pygame.mouse.get_pos()):
                #restarts the game, updating scores
                if userSum == dealSum:
                    pass
                elif userSum <= 21 and len(userCard) == 5:
                    winNum += 1
                elif userSum <= 21 and dealSum < userSum or dealSum > 21:
                    winNum += 1
                else:
                    loseNum += 1
                gameover = False
                stand = False
                userCard = []
                dealCard = []
                ccards = copy.copy(cards)
                userSum, userA, dealSum, dealA = initGameJ(ccards, userCard, dealCard)
                restartB = pygame.draw.rect(background, (80, 150, 15), (555, 300, 75, 25)) #Hide button during game

        #Change positioning of text w/ buttons
        screen.blit(background, (0, 0))
        screen.blit(hitTxt, (79, 525))
        screen.blit(standTxt, (156, 525))
        screen.blit(winTxt, (100, 580))
        screen.blit(loseTxt, (100, 600))

        #displays dealer's cards
        for card in dealCard:
            x = 50 + dealCard.index(card) * 110
            screen.blit(card, (x, 50))
        screen.blit(cBack, (160, 50))

        #displays player's cards
        for card in userCard:
            x = 225 + userCard.index(card) * 110
            screen.blit(card, (x, 500)) #Change position of user cards

        #when game is over, draws restart button and text, and shows the dealer's second card
        if gameover or stand:
            screen.blit(gameoverTxt, (555, 260))
            restartB = pygame.draw.rect(background, gray, (555, 300, 75, 25))
            screen.blit(restartTxt, (567, 302))
            screen.blit(dealCard[1], (160, 50))
            
        pygame.display.update()

def rules_screen():
    
    pygame.init()

    pygame.display.set_caption('BlackjackGUI')
    
    screen = pygame.display.set_mode((1280, 720))

    #Establish background and match color of game
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((80, 150, 15))

    #Arrange Text
    font1 = pygame.font.SysFont('arialbold', 45)
    font2 = pygame.font.SysFont('arialbold', 25)
    font3 = pygame.font.SysFont('arial', 15)

    mode1 = font1.render('Normal Mode:', 1, white)
    mode2 = font1.render('Joker Mode:', 1, white)

    rules1 = font2.render('Normal Rules - Get as close to 21 without going over as you can. You start with 2 cards. Aces are 11 by default & can become 1. Face cards are 10.', 1, white)
    rules2 = font2.render('Normal Rules, but with a twist - The joker card sabotages your hand! The joker card is valued at 21 by itself.', 1, white)

    menuTxt = font3.render('Menu', 1, black)

    menuB = pygame.draw.rect(background, gray, (1100, 600, 75, 25))


    #Event loop for title screen
    while True:

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and menuB.collidepoint(pygame.mouse.get_pos()):
                title_screen() #Run main game if user clicks play button. 


        #Show text on background
        screen.blit(background, (0, 0))
        screen.blit(menuTxt, (1115, 600))
        screen.blit(mode1, (50, 100))
        screen.blit(rules1, (50, 175))
        screen.blit(mode2, (50, 300))
        screen.blit(rules2, (50, 375))
        
        pygame.display.update() #GET THIS DISPLAY TO SHOW WHAT I JUST CODED.

#Add a title screen; this also leads to the main game
def title_screen():

    pygame.init()

    pygame.display.set_caption('BlackjackGUI')
    
    screen = pygame.display.set_mode((1280, 720))

    #Establish background and match color of game
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((80, 150, 15))

    #Arrange Text
    font1 = pygame.font.SysFont('arialbold', 45)
    font2 = pygame.font.SysFont('arialbold', 15)
    font3 = pygame.font.SysFont('arial', 15)
    titleTxt = font1.render('BlackjackGUI', 1, white)
    subTxt = font2.render('Click on a mode to start', 1, white)
    playTxt = font3.render('Normal', 1, black)
    quitTxt = font3.render('Quit', 1, black)
    jokerTxt = font3.render('Joker', 1, black)
    rulesTxt = font3.render('Rules', 1, black)

    #Establish buttons
    playB = pygame.draw.rect(background, gray, (530, 400, 75, 25))
    playJB = pygame.draw.rect(background, gray, (640, 400, 75, 25))
    quitB = pygame.draw.rect(background, gray, (585, 480, 75, 25))
    rulesB = pygame.draw.rect(background, gray, (585, 440, 75, 25))

    #Event loop for title screen
    while True:

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and playB.collidepoint(pygame.mouse.get_pos()):
                single_player() #Run main game if user clicks play button. 
            elif event.type == pygame.MOUSEBUTTONDOWN and playJB.collidepoint(pygame.mouse.get_pos()):
                single_playerJ() #Run joker game if user clicks play button. 
            elif event.type == pygame.MOUSEBUTTONDOWN and rulesB.collidepoint(pygame.mouse.get_pos()):
                rules_screen() #Run rules screen when user clicks.
            elif event.type == pygame.MOUSEBUTTONDOWN and quitB.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()

        #Show text on background
        screen.blit(background, (0, 0))
        screen.blit(titleTxt, (530, 300))
        screen.blit(subTxt, (572, 350))
        screen.blit(playTxt, (540, 400)) 
        screen.blit(jokerTxt, (660, 400))
        screen.blit(quitTxt, (605, 480))
        screen.blit(rulesTxt, (605, 440))

        pygame.display.update() #GET THIS DISPLAY TO SHOW WHAT I JUST CODED.

title_screen() #Start program in the title screen


