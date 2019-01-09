#git is working, for real now!!. 
import random

player_names = {1: 'player ONE', 2: 'player TWO', 3: 'player THREE', 4: 'player FOUR'}
bank = {'player ONE': 0, 'player TWO': 0, 'player THREE': 0, 'player FOUR': 0}
turnOfPlayer = 0

dice1 = 1
dice2 = 1

page='attack_cards'

Player_one_movement_card = []
Player_one_attack_card = []
Player_two_movement_card = []
Player_two_attack_card = []
Player_three_movement_card = []
Player_three_attack_card = []
Player_four_movement_card = []
Player_four_attack_card = []
neutral_movement_cards = ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l',
                          'l', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', ]
attackCards_stack = ['mk.I', 'mk.I', 'mk.I', 'mk.I', 'mk.I', 'mk.I', 'mk.II', 'mk.II', 'mk.II', 'mk.II', 'mk.II',
                         'shield', 'shield', 'shield', 'shield', 'shield', 'shield', 'nuke', 'blockade', 'blockade',
                         'blockade', 'blockade', 'blockade', 'blockade']
attackCards_price = {'mk.I': 10, 'mk.II': 15, 'shield': 15, 'blockade': 7, 'nuke': 35, 'used': 0}


# adds money(blobs) to the bank account of the player
def add_money(x, y, w, h, r, t, f):
    if f == 'display':
        if (mouseX > (width*x) and mouseY > (height*y) and (mouseX < ((width*x) + (width * w)) and mouseY < ((height*y) + (height*h)))):
            fill(100, 100, 100, 100)
            rect((width* x), (height* y), (width* w), (height* h), r)
        else:
            rect((width* x), (height* y), (width* w), (height* h), r)
    elif f == 'play':
        if mouseButton == LEFT:
            if (mouseX > (width*x) and mouseY > (height*y) and (mouseX < ((width*x) + (width * w)) and mouseY < ((height*y) + (height*h)))):
                global turnOfPlayer
                global dice1, dice2
                if turnOfPlayer == 0:
                    pass
                else:
                    player = player_names[t]
                    dice1 = random.randint(1, 6)
                    dice2 = random.randint(1, 6)
                    bank[player] = bank[player] + dice1 + dice2
                    turnOfPlayer = 0


# shuffles the cards stack and deals 5 movement card per player
def shuffle():
    if len(neutral_movement_cards) == 30:
        random.shuffle(neutral_movement_cards)
        for a in range(5):
            Player_one_movement_card.append(neutral_movement_cards[a])
            del neutral_movement_cards[a]
            Player_two_movement_card.append(neutral_movement_cards[a])
            del neutral_movement_cards[a]
            Player_three_movement_card.append(neutral_movement_cards[a])
            del neutral_movement_cards[a]
            Player_four_movement_card.append(neutral_movement_cards[a])
            del neutral_movement_cards[a]


# moves the chosen card to the neutral movement cardstack and the first movement card of the neutral stack is added to the player movement cardstack.
# movement_cards(card number,player movement card stack)
def movement_cards(k, p):
    neutral_movement_cards.append(p[k])
    del p[k]


def hand_out_movement_card(x, y, w, h, r, t, f):
    if f == 'display':
        if (mouseX > (width*x) and mouseY > (height*y) and (mouseX < ((width*x) + (width * w)) and mouseY < ((height*y) + (height*h)))):
            fill(100, 100, 100, 100)
            rect((width* x), (height* y), (width* w), (height* h), r)
            
        else:
            rect((width* x), (height* y), (width* w), (height* h), r)
    elif f == 'play':
        if mouseButton == LEFT:
            if (mouseX > (width*x) and mouseY > (height*y) and (mouseX < ((width*x) + (width * w)) and mouseY < ((height*y) + (height*h)))):
                global turnOfPlayer
                if turnOfPlayer == 0:
                    pass
                if turnOfPlayer == 1:
                    if len(Player_one_movement_card)==5:
                        pass
                    else:
                        Player_one_movement_card.append(neutral_movement_cards[0])
                        del neutral_movement_cards[0]
                        turnOfPlayer = 0
                        
                if turnOfPlayer == 2:
                    if len(Player_two_movement_card)==5:
                        pass
                    else:
                        Player_two_movement_card.append(neutral_movement_cards[0])
                        del neutral_movement_cards[0]    
                        turnOfPlayer = 0        
                if turnOfPlayer == 3:
                    if len(Player_three_movement_card)==5:
                        pass
                    else:
                        Player_three_movement_card.append(neutral_movement_cards[0])
                        del neutral_movement_cards[0]   
                        turnOfPlayer = 0               
                if turnOfPlayer == 4:
                    if len(Player_four_movement_card)==5:
                        pass
                    else:
                        Player_four_movement_card.append(neutral_movement_cards[0])
                        del neutral_movement_cards[0]
                        turnOfPlayer = 0


# rectangle with (x, y, width, height, radius) in percentages
def rect_h(x, y, w, h, r):
    rect((width / 100) * x, (height / 100) * y, (width / 100) * w, (height / 100) * h, r)

    
# button to change player turn value
# turn_button(x,y,width,height,radius,turn number, if elif):
def turn_button(x, y, w, h, r, t, f):
    global turnOfPlayer
    if f == 'display':
        if (mouseX > (width*x) and mouseY > (height*y) and (mouseX < ((width*x) + (width * w)) and mouseY < ((height*y) + (height*h)))):
            fill(100, 100, 100, 150)
            rect((width*x), (height*y), (width * w), (height*h), r)
            if turnOfPlayer == t:
                strokeWeight(width*0.005)
                stroke(204, 102, 0)
                rect((width*x), (height*y), (width * w), (height*h), r)
                stroke(0, 0, 0)
                strokeWeight(0)
        else:
            rect((width*x), (height*y), (width * w), (height*h), r)
            if turnOfPlayer == t:
                strokeWeight(width*0.005)
                stroke(204, 102, 0)
                rect((width*x), (height*y), (width * w), (height*h), r)
                stroke(0, 0, 0)
                strokeWeight(0)
    elif f == 'play':
        if mouseButton == LEFT:
            if (mouseX > (width*x) and mouseY > (height*y) and (mouseX < ((width*x) + (width * w)) and mouseY < ((height*y) + (height*h)))):
                turnOfPlayer = t


def page_button(x, y, w, h, r, p, f):
    global page
    if f == 'display':
        if (mouseX > (width*x) and mouseY > (height*y) and (mouseX < ((width*x) + (width * w)) and mouseY < ((height*y) + (height*h)))):
            fill(100, 100, 100, 150)
            rect((width*x), (height*y), (width * w), (height*h), r)
            fill(250, 250, 250, 100)
            if page == p:
                strokeWeight(width*0.002)
                stroke(204, 102, 0)
                rect((width*x), (height*y), (width * w), (height*h), r)
                stroke(0, 0, 0)
                strokeWeight(0)
        else:
            rect((width*x), (height*y), (width * w), (height*h), r)
            if page == p:
                strokeWeight(width*0.002)
                stroke(204, 102, 0)
                rect((width*x), (height*y), (width * w), (height*h), r)
                stroke(0, 0, 0)
                strokeWeight(0)
    elif f == 'play':
        if mouseButton == LEFT:
            if (mouseX > (width*x) and mouseY > (height*y) and (mouseX < ((width*x) + (width * w)) and mouseY < ((height*y) + (height*h)))):
                page = p



# display test on the screen
def text_display():
    fill(0, 0, 0)
    p1 = str(bank['player ONE']) + ' blobs'
    p2 = str(bank['player TWO']) + ' blobs'
    p3 = str(bank['player THREE']) + ' blobs'
    p4 = str(bank['player FOUR']) + ' blobs'
    
    turn_wheel_page='Turn \nwheel'
    attack_card_page='Attack \ncards'
    dice = 'Dice'
    cards = 'Cards'
    
    textSize(width * 0.01)
    text(p1, width * 0.035, height* 0.22)
    text(p2, width * 0.925, height * 0.22)
    text(p3, width  * 0.035, height* 0.98)
    text(p4, width * 0.925, height * 0.98)
    
    textSize(width  * 0.02)
    text(dice, width * 0.48, height * 0.125)
    text(cards, width  * 0.474, height * 0.18)
    text(attack_card_page, width  * 0.4, height * 0.13)
    text(turn_wheel_page, width  * 0.548, height * 0.13)
    
    textSize(width * 0.01)
    if turnOfPlayer == 0:
        turn = 'Please choose the player turn by clicking \n on the player spaceship'
        text(turn, width * 0.402, height  * 0.047)
    else:
        turn = 'Player ' + str(turnOfPlayer) + ' turn'
        text(turn, width * 0.47, height * 0.06)
    if page=='attack_cards':
        # attack cards prise text
        attack_cards_price = ' CARDS PRICE \n Mk.I:       10 Blobs \n Mk.II:      15 Blobs \n Shield:    15 Blobs \n Nuke:      35 Blobs \n Blockade: 7 blobs '
        fill(250, 250,250)
        textSize(width * 0.01)
        text(attack_cards_price, width  * 0.89, height * 0.46)


# displays movement cards on the screen by checking the player stack list
# movement_card_play(x,y,player stack list name,list item number)
def movement_card(x, y, p, k, f):
    if f == 'play':
        if mousePressed:
            if (mouseX > (width*x) and mouseY > (height*y) and (mouseX < ((width*x) + (width * 0.05)) and mouseY < ((height*y) + (height* 0.13)))):
                    movement_cards(k, p)
    elif 'display':
        if (mouseX > (width*x) and mouseY > (height*y) and (mouseX < ((width*x) + (width * 0.05)) and mouseY < ((height*y) + height* 0.13))):
            if p == Player_three_movement_card or p == Player_four_movement_card:
                if p[k] == 'f':
                    image(move_forward, (width*x), (height* (y-0.02)), (width *0.05), (height* 0.13))
    
                elif p[k] == 'r':
                    image(move_right, (width*x), (height* (y-0.02)), (width *0.05), (height* 0.13))
        
                elif p[k] == 'l':
                    image(move_left, (width*x), (height* (y-0.02)), (width *0.05), (height* 0.13))
            else:
                
                if p[k] == 'f':
                    image(move_forward, (width*x), (height* (y+0.02)), (width *0.05), (height* 0.13))
        
                elif p[k] == 'r':
                    image(move_right, (width*x), (height* (y+0.02)), (width *0.05), (height* 0.13))
        
                elif p[k] == 'l':
                    image(move_left, (width*x), (height* (y+0.02)), (width *0.05), (height* 0.13))
        else:
            if p[k] == 'f':
                image(move_forward, (width*x), (height*y), (width *0.05), (height* 0.13))
    
            elif p[k] == 'r':
                image(move_right, (width*x), (height*y), (width *0.05), (height* 0.13))
    
            elif p[k] == 'l':
                image(move_left, (width*x), (height*y), (width *0.05), (height* 0.13))


# checks the bank account and if there is enough money then then the player can buy the attack and defence cards that are still available
# displays the attack and defence cards that are still available on the screen
# attack_card(x,y,card name, if and elif ):
def attack_card(x, y, k, f):
    if page=='attack_cards':
        global turnOfPlayer
        p = attackCards_stack[k]
        if f == 'buy':
            if mousePressed:
                if (mouseX > (width*x) and mouseY > (height*y) and (mouseX < ((width*x) + (width * 0.05)) and mouseY < ((height*y) + height* 0.13))):
                    if turnOfPlayer == 0:
                        pass
                    else:
                        player = player_names[turnOfPlayer]
                        price = -attackCards_price[p]
                        if bank[player] + price < 0:
                            turnOfPlayer = 0
                        else:
                            if attackCards_stack[k]=='used':
                                turnOfPlayer = 0
                            else:
                                bank[player] = bank[player] + price
                                if turnOfPlayer == 1:
                                    Player_one_attack_card.append(attackCards_stack[k])
                                    turnOfPlayer = 0
                                    attackCards_stack[k] = 'used'
                                elif turnOfPlayer == 2:
                                    Player_two_attack_card.append(attackCards_stack[k])
                                    turnOfPlayer = 0
                                    attackCards_stack[k] = 'used'
                                elif turnOfPlayer == 3:
                                    Player_three_attack_card.append(attackCards_stack[k])
                                    turnOfPlayer = 0
                                    attackCards_stack[k] = 'used'
                                elif turnOfPlayer == 4:
                                    Player_four_attack_card.append(attackCards_stack[k])
                                    turnOfPlayer = 0
                                    attackCards_stack[k] = 'used'
        elif f == 'display':            
            if attackCards_stack[k] == 'mk.I':
                image(mk_I_laser, (width* x), (height* y), (width* 0.07), (height* 0.17))
        
            elif attackCards_stack[k] == 'mk.II':
                image(mk_II_laser, (width* x), (height* y), (width* 0.07), (height* 0.17))
        
            elif attackCards_stack[k] == 'shield':
                image(shield, (width* x), (height* y), (width* 0.07), (height* 0.17))
        
            elif attackCards_stack[k] == 'blockade':
                image(blockade, (width* x), (height* y), (width* 0.07), (height* 0.17))
        
            elif attackCards_stack[k] == 'nuke':
                image(nuke, (width* x), (height* y), (width* 0.07), (height* 0.17))
        
            elif attackCards_stack[k] == 'used':
                image(sold, (width* x), (height* y), (width* 0.07), (height* 0.17))
            
            
            if (mouseX > (width*x) and mouseY > (height*y) and (mouseX < ((width*x) + (width * 0.05)) and mouseY < ((height*y) + height* 0.13))):
            
                if attackCards_stack[k] == 'mk.I':
                    image(mk_I_laser, width* (x-0.0025), height* (y-0.0025), width*(0.07+0.005), height* (0.17+0.005))
            
                elif attackCards_stack[k] == 'mk.II':
                    image(mk_II_laser,  width* (x-0.0025), height* (y-0.0025), width*(0.07+0.005), height* (0.17+0.005))
            
                elif attackCards_stack[k] == 'shield':
                    image(shield,  width* (x -0.0025), height* (y -0.0025), width*(0.07+0.005), height* (0.17+0.005))
            
                elif attackCards_stack[k] == 'blockade':
                    image(blockade,  width* (x-0.0025), height* (y-0.0025), width*(0.07+0.005), height* (0.17+0.005))
            
                elif attackCards_stack[k] == 'nuke':
                    image(nuke,  width* (x-0.0025), height* (y-0.0025), width*(0.07+0.005), height* (0.17+0.005))
            
                elif attackCards_stack[k] == 'used':
                    image(sold,  width* (x-0.0025), height* (y-0.0025), width*(0.07+0.005), height* (0.17+0.005))    


# displays the attack and defence cards owned by the player on the screen next to the player spaceship
# removes attack and defence cards that player want to use by clicking on it
#   player_card(x,y,card number,if and elif,player power card stack)
def player_attack_card(x, y, k, f, p):
    if f == 'use':
        if mousePressed:
            if (mouseX > (width*x) and mouseY > (height*y) and (mouseX <  ((width*x) + width*0.035) and mouseY < ((height*y) + height*0.08))):
                del p[k - 1]

    elif f == 'display':
        if len(p) == 0: pass
        else:
            if p[k - 1] == 'mk.I':image(mk_I_laser, (width*x),  (height*y), width*0.035,height*0.08)
            elif p[k - 1] == 'mk.II':image(mk_II_laser,  (width*x),  (height*y), width*0.035, height*0.08)
            elif p[k - 1] == 'shield':image(shield, (width*x),  (height*y), width*0.035, height*0.08)
            elif p[k - 1] == 'blockade':image(blockade, (width*x), (height*y),width*0.035, height*0.08)
            elif p[k - 1] == 'nuke':image(nuke,  (width*x), (height*y),width* 0.035, height*0.08)
            elif p[k - 1] == 'used':image(sold, (width*x), (height*y), width*0.035, height*0.08)


def player_name(x, y, w, h, r, playerName,f):
    if f == 'display':
        if (mouseX > (width*x) and mouseY > (height*y) and (mouseX < ((width*x) + (width * w)) and mouseY < ((height*y) + (height*h)))):
            fill(10, 10, 10, 150)
            rect((width*x), (height*y), (width * w), (height*h), r)
        else:
            fill(50, 50, 50, 150)
            rect((width*x), (height*y), (width * w), (height*h), r)
        # player names 
        fill(255)
        textFont(createFont("Arial", width*0.01, True))
        text(playerName,width*(x+0.01), height*(y+0.02)) # text(name, x, y)


def setup():
    frameRate(60)
    size(1500,900)
    #fullScreen()
    shuffle()
    
    global move_left, move_right, move_forward, Background, mk_I_laser, mk_II_laser, shield, blockade, nuke, sold, Text1, Text2, Text3, Text4, d1, d2, d3, d4, d5, d6, Ship1, Ship2, Ship3, Ship4
    
    Text1, Text2, Text3, Text4 = "| ", "| ", "| ", "| " # Text input for each textbox
    
    move_left= loadImage("move_left.PNG")
    move_right= loadImage("move_right.PNG")
    move_forward= loadImage("move_forward.PNG")
    
    Background = loadImage("Background-1.jpg")
    
    mk_I_laser = loadImage("mk_I_laser.png")
    mk_II_laser = loadImage("mk_II_laser.png")
    shield = loadImage("shield.png")
    blockade = loadImage("blockade.png")
    nuke = loadImage("nuke.png")
    sold = loadImage("sold.png")
    
    d1 = loadImage("1.png")
    d2 = loadImage("2.png")
    d3 = loadImage("3.png")
    d4 = loadImage("4.png")
    d5 = loadImage("5.png")
    d6 = loadImage("6.png")
    
    Ship1 = loadImage("BlueShip.png")
    Ship2 = loadImage("GreenShip.png")
    Ship3 = loadImage("GreyShip.png")
    Ship4 = loadImage("RedShip.png")
    
def draw():
    global Text1, Text2, Text3, Text4, dice1, dice2, d1, d2, d3, d4, d5, d6, Ship1, Ship2, Ship3, Ship4
    
    # Background
    image(Background, 0, 0, width, height)
    
    # display page buttons
    fill(250, 250, 250, 100)
    page_button(0.39, 0.094, 0.07, 0.1, 20, 'attack_cards', 'display')
    page_button(0.54, 0.094, 0.07, 0.1, 20, 'turn_wheel', 'display')
    
    
    # Display image with corresponding dice number
    if dice1 == 1: image(d1, width* 0.5, height* 0.86, width*0.07, height* 0.11)
    if dice1 == 2: image(d2, width* 0.5, height* 0.86, width*0.07, height* 0.11)
    if dice1 == 3: image(d3, width* 0.5, height* 0.86, width*0.07, height* 0.11)
    if dice1 == 4: image(d4, width* 0.5, height* 0.86, width*0.07, height* 0.11)
    if dice1 == 5: image(d5, width* 0.5, height* 0.86, width*0.07, height* 0.11)
    if dice1 == 6: image(d6, width* 0.5, height* 0.86, width*0.07, height* 0.11)
    
    if dice2 == 1: image(d1, width* 0.42, height* 0.86, width*0.07, height* 0.11)
    if dice2 == 2: image(d2, width* 0.42, height* 0.86, width*0.07, height* 0.11)
    if dice2 == 3: image(d3, width* 0.42, height* 0.86, width*0.07, height* 0.11)
    if dice2 == 4: image(d4, width* 0.42, height* 0.86, width*0.07, height* 0.11)
    if dice2 == 5: image(d5, width* 0.42, height* 0.86, width*0.07, height* 0.11)
    if dice2 == 6: image(d6, width* 0.42, height* 0.86, width*0.07, height* 0.11)

    # player one background rectangle
    # rect(x, y, width, height, round)
    fill(0, 100, 200, 150) # Blue Ship
    turn_button(0.005, 0.005, 0.10, 0.23, 20, 1, 'display')
    # player two background rectangle
    fill(0, 120, 50, 150) # Green Ship
    turn_button(0.895, 0.005, 0.10, 0.23, 20, 2, 'display')
    # player three background rectangle
    fill(200, 200, 0, 100) # Yellow Ship
    turn_button(0.005, 0.765, 0.10, 0.23, 20, 3, 'display')
    # player four background rectangle
    fill(120, 20, 0, 150) # Red Ship
    turn_button(0.895, 0.765, 0.10, 0.23, 20, 4, 'display')
    
    
    # displays player name on the screen 
    player_name(0.015, 0.17, 0.08, 0.03, 10, Text1,'display')
    player_name(0.015, 0.93, 0.08, 0.03, 10, Text2,'display')
    player_name(0.905, 0.93, 0.08, 0.03, 10, Text3,'display')
    player_name(0.905, 0.17, 0.08, 0.03, 10, Text4,'display')
    
    # player turn display background rectangle
    # rect(x, y, width, height, round)
    if turnOfPlayer == 0:
        fill(250, 250, 250, 100)
        rect(width*0.39, height*0.025, width*0.22,height*0.06, 20)
    else:
        fill(250, 250, 250, 100)
        rect(width*0.45, height*0.03, width*0.10,height*0.05, 20)


    # dice background rectangle
    # rect(x, y, width, height, round)
    fill(250, 250, 250, 100)
    add_money(0.465, 0.09, 0.07, 0.05, 20, turnOfPlayer, 'display')
    
    # display button to hand out movement card 
    fill(250, 250, 250, 100)
    hand_out_movement_card(0.465, 0.145,0.07, 0.05, 20, turnOfPlayer, 'display')
    
    # display player (blobs) amount and turn/dice test on the screen
    text_display()

    # display ships on the screen
    image(Ship1, (width * 0.0155), (height* 0.015), (width * 0.075), (height * 0.15))
    image(Ship2, (width * 0.907), (height* 0.015), (width * 0.075), (height * 0.15))
    image(Ship3, (width * 0.0155), (height* 0.78), (width * 0.075), (height  * 0.14))
    image(Ship4, (width * 0.882), (height* 0.78), (width * 0.13), (height  * 0.14))

    # displays movement cards on the screen by checking the player stack list
    # movement_card_play(x,y,player stack list name,list item number,fuctionName)
    # player one
    # movement_card_play(x,y,player stack list name,list item number,if and elif)
    if len(Player_one_movement_card) >= 1:movement_card(0.12, 0.015, Player_one_movement_card, 0, 'display')
    if len(Player_one_movement_card) >= 2:movement_card(0.17, 0.015, Player_one_movement_card, 1, 'display')
    if len(Player_one_movement_card) >= 3:movement_card(0.22, 0.015, Player_one_movement_card, 2, 'display')
    if len(Player_one_movement_card) >= 4:movement_card(0.27, 0.015, Player_one_movement_card, 3, 'display')
    if len(Player_one_movement_card) >= 5:movement_card(0.32, 0.015, Player_one_movement_card, 4, 'display')
    # player two
    if len(Player_two_movement_card) >= 1:movement_card(0.83, 0.015, Player_two_movement_card, 0, 'display')
    if len(Player_two_movement_card) >= 2:movement_card(0.78, 0.015, Player_two_movement_card, 1, 'display')
    if len(Player_two_movement_card) >= 3:movement_card(0.73, 0.015, Player_two_movement_card, 2, 'display')
    if len(Player_two_movement_card) >= 4:movement_card(0.68, 0.015, Player_two_movement_card, 3, 'display')
    if len(Player_two_movement_card) >= 5:movement_card(0.63, 0.015, Player_two_movement_card, 4, 'display')
    # player three
    if len(Player_three_movement_card) >= 1:movement_card(0.12, 0.85, Player_three_movement_card, 0, 'display')
    if len(Player_three_movement_card) >= 2:movement_card(0.17, 0.85, Player_three_movement_card, 1, 'display')
    if len(Player_three_movement_card) >= 3:movement_card(0.22, 0.85, Player_three_movement_card, 2, 'display')
    if len(Player_three_movement_card) >= 4:movement_card(0.27, 0.85, Player_three_movement_card, 3, 'display')
    if len(Player_three_movement_card) >= 5:movement_card(0.32, 0.85, Player_three_movement_card, 4, 'display')
    # player four
    if len(Player_four_movement_card) >= 1:movement_card(0.83, 0.85, Player_four_movement_card, 0, 'display')
    if len(Player_four_movement_card) >= 2:movement_card(0.78, 0.85, Player_four_movement_card, 1, 'display')
    if len(Player_four_movement_card) >= 3:movement_card(0.73, 0.85, Player_four_movement_card, 2, 'display')
    if len(Player_four_movement_card) >= 4:movement_card(0.68, 0.85, Player_four_movement_card, 3, 'display')
    if len(Player_four_movement_card) >= 5:movement_card(0.63, 0.85, Player_four_movement_card, 4, 'display')

    # displays the attack and defence cards that are still available on the screen
    # attack_card(x,y,card name, if and elif ):
    attack_card(0.203, 0.631, 20, 'display')
    attack_card(0.278, 0.631, 23, 'display')
    attack_card(0.353, 0.631, 0, 'display')
    attack_card(0.428, 0.631, 1, 'display')
    attack_card(0.503, 0.631, 2, 'display')
    attack_card(0.578, 0.631, 3, 'display')
    attack_card(0.653, 0.631, 4, 'display')
    attack_card(0.728, 0.631, 5, 'display')
    
    attack_card(0.203, 0.279, 18, 'display')
    attack_card(0.278, 0.279, 21, 'display')
    attack_card(0.353, 0.279, 6, 'display')
    attack_card(0.428, 0.279, 7, 'display')
    attack_card(0.503, 0.279, 8, 'display')
    attack_card(0.578, 0.279, 9, 'display')
    attack_card(0.653, 0.279, 10, 'display')
    attack_card(0.728, 0.279, 11, 'display')
    
    attack_card(0.203, 0.455, 19, 'display')
    attack_card(0.278, 0.455, 22, 'display')
    attack_card(0.353, 0.455, 12, 'display')
    attack_card(0.428, 0.455, 13, 'display')
    attack_card(0.503, 0.455, 14, 'display')
    attack_card(0.578, 0.455, 15, 'display')
    attack_card(0.653, 0.455, 16, 'display')
    attack_card(0.728, 0.455, 17, 'display')


    
    
    

    # displays the attack and defence cards owned by the player on the screen next to the player spaceship
    #   player_attack_card(x,y,card number,if and elif,player power card stack)
    if len(Player_one_attack_card) >= 1: player_attack_card(0.12, 0.15, 1, 'display', Player_one_attack_card)
    if len(Player_one_attack_card) >= 2: player_attack_card(0.156, 0.15, 2, 'display', Player_one_attack_card)
    if len(Player_one_attack_card) >= 3: player_attack_card(0.192, 0.15, 3, 'display', Player_one_attack_card)
    if len(Player_one_attack_card) >= 4: player_attack_card(0.228, 0.15, 4, 'display', Player_one_attack_card)
    if len(Player_one_attack_card) >= 5: player_attack_card(0.264, 0.15, 5, 'display', Player_one_attack_card)
    if len(Player_one_attack_card) >= 6: player_attack_card(0.3, 0.15, 6, 'display', Player_one_attack_card)
    if len(Player_one_attack_card) >= 7: player_attack_card(0.336, 0.15, 7, 'display', Player_one_attack_card)

    if len(Player_two_attack_card) >= 1: player_attack_card(0.845, 0.15, 1, 'display', Player_two_attack_card)
    if len(Player_two_attack_card) >= 2: player_attack_card(0.809, 0.15, 2, 'display', Player_two_attack_card)
    if len(Player_two_attack_card) >= 3: player_attack_card(0.773, 0.15, 3, 'display', Player_two_attack_card)
    if len(Player_two_attack_card) >= 4: player_attack_card(0.737, 0.15, 4, 'display', Player_two_attack_card)
    if len(Player_two_attack_card) >= 5: player_attack_card(0.701, 0.15, 5, 'display', Player_two_attack_card)
    if len(Player_two_attack_card) >= 6: player_attack_card(0.669, 0.15, 6, 'display', Player_two_attack_card)
    if len(Player_two_attack_card) >= 7: player_attack_card(0.629, 0.15, 7, 'display', Player_two_attack_card)

    if len(Player_three_attack_card) >= 1: player_attack_card(0.12, 0.765, 1, 'display', Player_three_attack_card)
    if len(Player_three_attack_card) >= 2: player_attack_card(0.156, 0.765, 2, 'display', Player_three_attack_card)
    if len(Player_three_attack_card) >= 3: player_attack_card(0.192, 0.765, 3, 'display', Player_three_attack_card)
    if len(Player_three_attack_card) >= 4: player_attack_card(0.228, 0.765, 4, 'display', Player_three_attack_card)
    if len(Player_three_attack_card) >= 5: player_attack_card(0.264, 0.765, 5, 'display', Player_three_attack_card)
    if len(Player_three_attack_card) >= 6: player_attack_card(0.30, 0.765, 6, 'display', Player_three_attack_card)
    if len(Player_three_attack_card) >= 7: player_attack_card(0.336, 0.765, 7, 'display', Player_three_attack_card)

    if len(Player_four_attack_card) >= 1: player_attack_card(0.845, 0.765, 1, 'display', Player_four_attack_card)
    if len(Player_four_attack_card) >= 2: player_attack_card(0.809, 0.765, 2, 'display', Player_four_attack_card)
    if len(Player_four_attack_card) >= 3: player_attack_card(0.773, 0.765, 3, 'display', Player_four_attack_card)
    if len(Player_four_attack_card) >= 4: player_attack_card(0.737, 0.765, 4, 'display', Player_four_attack_card)
    if len(Player_four_attack_card) >= 5: player_attack_card(0.701, 0.765, 5, 'display', Player_four_attack_card)
    if len(Player_four_attack_card) >= 6: player_attack_card(0.665, 0.765, 6, 'display', Player_four_attack_card)
    if len(Player_four_attack_card) >= 7: player_attack_card(0.629, 0.765, 7, 'display', Player_four_attack_card)
    
def keyPressed():
    global Text1, Text2, Text3, Text4
    
   # allow you to input player name on the screen by typing the name while you hover the mouse over one particular name box
    if (mouseX > (width*0.015) and mouseY > (height*0.17) and (mouseX < ((width*0.015) + (width * 0.08)) and mouseY < ((height*0.17) + (height*0.03)))):
            if len(Text1) < 12 and key!= ENTER and keyCode != SHIFT and key != 65535 and key != BACKSPACE:
                Text1 += str(key)
            elif len(Text1)>0:
                if key == BACKSPACE:
                    Text1=Text1[:-1]
                
    elif (mouseX > (width*0.015) and mouseY > (height*0.93) and (mouseX < ((width*0.015) + (width * 0.08)) and mouseY < ((height*0.93) + (height*0.03)))):
        if len(Text2) < 12 and key!= ENTER and keyCode != SHIFT and key != 65535 and key != BACKSPACE:
                Text2 += str(key)
        elif len(Text2)>0:
                if key == BACKSPACE:
                    Text2=Text2[:-1]

    elif (mouseX > (width*0.905) and mouseY > (height*0.93) and (mouseX < ((width*0.905) + (width * 0.08)) and mouseY < ((height*0.93) + (height*0.03)))):
        if len(Text3) < 12 and key!= ENTER and keyCode != SHIFT and key != 65535 and key != BACKSPACE:
                Text3 += str(key)
        elif len(Text3)>0:
                if key == BACKSPACE:
                    Text3=Text3[:-1]

    elif (mouseX > (width*0.905) and mouseY > (height*0.17) and (mouseX < ((width*0.905) + (width * 0.08)) and mouseY < ((height*0.17) + (height*0.03)))):
        if len(Text4) < 12 and key!= ENTER and keyCode != SHIFT and key != 65535 and key != BACKSPACE:
                Text4 += str(key)
        elif len(Text4)>0:
                if key == BACKSPACE:
                    Text4=Text4[:-1]
    
def mousePressed():
    fill(250, 250, 250, 0)

    # dice background rectangle button
    # rect(x, y, width, height, round,functionName)
    add_money(0.45, 0.09, 0.10, 0.05, 20, turnOfPlayer, 'play')
    
    # button to hand out movement card 
    hand_out_movement_card(0.45, 0.145,0.10, 0.05, 20, turnOfPlayer, 'play')

    fill(250, 250, 250, 0)
    # makes the player background rectangle into a button
    # rect(x, y, width, height, round)
    turn_button(0.005, 0.005, 0.10, 0.23, 20, 1, 'play') # player one
    turn_button(0.895, 0.005, 0.10, 0.23, 20, 2, 'play')  # player two
    turn_button(0.895, 0.765, 0.10, 0.23, 20, 4, 'play') # player four
    turn_button(0.005, 0.765, 0.10, 0.23, 20, 3, 'play') # player three
    
    # changes the page with mouse click
    page_button(0.39, 0.094, 0.07, 0.1, 20, 'attack_cards', 'play')
    page_button(0.54, 0.094, 0.07, 0.1, 20, 'turn_wheel', 'play')


    # movement card will be removed by clicking on it and one new movement card from the neutral stack will be added to player stack
    # player one
    # movement_card_play(x,y,player stack list name,list item number,if and elif)
    if len(Player_one_movement_card) >= 1:movement_card(0.12, 0.015, Player_one_movement_card, 0, 'play')
    if len(Player_one_movement_card) >= 2:movement_card(0.17, 0.015, Player_one_movement_card, 1, 'play')
    if len(Player_one_movement_card) >= 3:movement_card(0.22, 0.015, Player_one_movement_card, 2, 'play')
    if len(Player_one_movement_card) >= 4:movement_card(0.27, 0.015, Player_one_movement_card, 3, 'play')
    if len(Player_one_movement_card) >= 5:movement_card(0.32, 0.015, Player_one_movement_card, 4, 'play')
    # player two
    if len(Player_two_movement_card) >= 1:movement_card(0.83, 0.015, Player_two_movement_card, 0, 'play')
    if len(Player_two_movement_card) >= 2:movement_card(0.78, 0.015, Player_two_movement_card, 1, 'play')
    if len(Player_two_movement_card) >= 3:movement_card(0.73, 0.015, Player_two_movement_card, 2, 'play')
    if len(Player_two_movement_card) >= 4:movement_card(0.68, 0.015, Player_two_movement_card, 3, 'play')
    if len(Player_two_movement_card) >= 5:movement_card(0.63, 0.015, Player_two_movement_card, 4, 'play')
    # player three
    if len(Player_three_movement_card) >= 1:movement_card(0.12, 0.85, Player_three_movement_card, 0, 'play')
    if len(Player_three_movement_card) >= 2:movement_card(0.17, 0.85, Player_three_movement_card, 1, 'play')
    if len(Player_three_movement_card) >= 3:movement_card(0.22, 0.85, Player_three_movement_card, 2, 'play')
    if len(Player_three_movement_card) >= 4:movement_card(0.27, 0.85, Player_three_movement_card, 3, 'play')
    if len(Player_three_movement_card) >= 5:movement_card(0.32, 0.85, Player_three_movement_card, 4, 'play')
    # player four
    if len(Player_four_movement_card) >= 1:movement_card(0.83, 0.85, Player_four_movement_card, 0, 'play')
    if len(Player_four_movement_card) >= 2:movement_card(0.78, 0.85, Player_four_movement_card, 1, 'play')
    if len(Player_four_movement_card) >= 3:movement_card(0.73, 0.85, Player_four_movement_card, 2, 'play')
    if len(Player_four_movement_card) >= 4:movement_card(0.68, 0.85, Player_four_movement_card, 3, 'play')
    if len(Player_four_movement_card) >= 5:movement_card(0.63, 0.85, Player_four_movement_card, 4, 'play')

    # checks the bank account and if there is enough money then then player buy the attack and defence cards that are still available
    # attack_card(x,y,card name, if and elif ):
    attack_card(0.203, 0.631, 20, 'buy')
    attack_card(0.278, 0.631, 23, 'buy')
    attack_card(0.353, 0.631, 0, 'buy')
    attack_card(0.428, 0.631, 1, 'buy')
    attack_card(0.503, 0.631, 2, 'buy')
    attack_card(0.578, 0.631, 3, 'buy')
    attack_card(0.653, 0.631, 4, 'buy')
    attack_card(0.728, 0.631, 5, 'buy')
    
    attack_card(0.203, 0.279, 18, 'buy')
    attack_card(0.278, 0.279, 21, 'buy')
    attack_card(0.353, 0.279, 6, 'buy')
    attack_card(0.428, 0.279, 7, 'buy')
    attack_card(0.503, 0.279, 8, 'buy')
    attack_card(0.578, 0.279, 9, 'buy')
    attack_card(0.653, 0.279, 10, 'buy')
    attack_card(0.728, 0.279, 11, 'buy')
    
    attack_card(0.203, 0.455, 19, 'buy')
    attack_card(0.278, 0.455, 22, 'buy')
    attack_card(0.353, 0.455, 12, 'buy')
    attack_card(0.428, 0.455, 13, 'buy')
    attack_card(0.503, 0.455, 14, 'buy')
    attack_card(0.578, 0.455, 15, 'buy')
    attack_card(0.653, 0.455, 16, 'buy')
    attack_card(0.728, 0.455, 17, 'buy')

    # removes attack and defence cards that player want to use by clicking on it
    #   power_card(x,y,card number,if and elif,player power card stack)
    if len(Player_one_attack_card) >= 1: player_attack_card(0.12, 0.15, 1, 'use', Player_one_attack_card)
    if len(Player_one_attack_card) >= 2: player_attack_card(0.156, 0.15, 2, 'use', Player_one_attack_card)
    if len(Player_one_attack_card) >= 3: player_attack_card(0.192, 0.15, 3, 'use', Player_one_attack_card)
    if len(Player_one_attack_card) >= 4: player_attack_card(0.228, 0.15, 4, 'use', Player_one_attack_card)
    if len(Player_one_attack_card) >= 5: player_attack_card(0.264, 0.15, 5, 'use', Player_one_attack_card)
    if len(Player_one_attack_card) >= 6: player_attack_card(0.3, 0.15, 6, 'use', Player_one_attack_card)
    if len(Player_one_attack_card) >= 7: player_attack_card(0.336, 0.15, 7, 'use', Player_one_attack_card)

    if len(Player_two_attack_card) >= 1: player_attack_card(0.845, 0.15, 1, 'use', Player_two_attack_card)
    if len(Player_two_attack_card) >= 2: player_attack_card(0.809, 0.15, 2, 'use', Player_two_attack_card)
    if len(Player_two_attack_card) >= 3: player_attack_card(0.773, 0.15, 3, 'use', Player_two_attack_card)
    if len(Player_two_attack_card) >= 4: player_attack_card(0.737, 0.15, 4, 'use', Player_two_attack_card)
    if len(Player_two_attack_card) >= 5: player_attack_card(0.701, 0.15, 5, 'use', Player_two_attack_card)
    if len(Player_two_attack_card) >= 6: player_attack_card(0.669, 0.15, 6, 'use', Player_two_attack_card)
    if len(Player_two_attack_card) >= 7: player_attack_card(0.629, 0.15, 7, 'use', Player_two_attack_card)

    if len(Player_three_attack_card) >= 1: player_attack_card(0.12, 0.765, 1, 'use', Player_three_attack_card)
    if len(Player_three_attack_card) >= 2: player_attack_card(0.156, 0.765, 2, 'use', Player_three_attack_card)
    if len(Player_three_attack_card) >= 3: player_attack_card(0.192, 0.765, 3, 'use', Player_three_attack_card)
    if len(Player_three_attack_card) >= 4: player_attack_card(0.228, 0.765, 4, 'use', Player_three_attack_card)
    if len(Player_three_attack_card) >= 5: player_attack_card(0.264, 0.765, 5, 'use', Player_three_attack_card)
    if len(Player_three_attack_card) >= 6: player_attack_card(0.30, 0.765, 6, 'use', Player_three_attack_card)
    if len(Player_three_attack_card) >= 7: player_attack_card(0.336, 0.765, 7, 'use', Player_three_attack_card)

    if len(Player_four_attack_card) >= 1: player_attack_card(0.845, 0.765, 1, 'use', Player_four_attack_card)
    if len(Player_four_attack_card) >= 2: player_attack_card(0.809, 0.765, 2, 'use', Player_four_attack_card)
    if len(Player_four_attack_card) >= 3: player_attack_card(0.773, 0.765, 3, 'use', Player_four_attack_card)
    if len(Player_four_attack_card) >= 4: player_attack_card(0.737, 0.765, 4, 'use', Player_four_attack_card)
    if len(Player_four_attack_card) >= 5: player_attack_card(0.701, 0.765, 5, 'use', Player_four_attack_card)
    if len(Player_four_attack_card) >= 6: player_attack_card(0.665, 0.765, 6, 'use', Player_four_attack_card)
    if len(Player_four_attack_card) >= 7: player_attack_card(0.629, 0.765, 7, 'use', Player_four_attack_card)
    
