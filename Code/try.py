
import pygame
import random
import time

pygame.init()


# start of deck 
C10 = pygame.image.load('Cardgame-Bura\Code\PNG\\10C.PNG')
C10 = pygame.transform.scale(C10,(150,150))

D10 = pygame.image.load('Cardgame-Bura\Code\PNG\\10D.PNG')
D10 = pygame.transform.scale(D10,(150,150))

H10 = pygame.image.load('Cardgame-Bura\Code\PNG\\10H.PNG')
H10 = pygame.transform.scale(H10,(150,150))

S10 = pygame.image.load('Cardgame-Bura\Code\PNG\\10S.PNG')
S10 = pygame.transform.scale(S10,(150,150))

JC = pygame.image.load('Cardgame-Bura\Code\PNG\\JC.PNG')
JC = pygame.transform.scale(JC,(150,150))

JD = pygame.image.load('Cardgame-Bura\Code\PNG\\JD.PNG')
JD = pygame.transform.scale(JD,(150,150))

JH = pygame.image.load('Cardgame-Bura\Code\PNG\\JH.PNG')
JH = pygame.transform.scale(JH,(150,150))

JS = pygame.image.load('Cardgame-Bura\Code\PNG\\JS.PNG')
JS = pygame.transform.scale(JS,(150,150))

QC = pygame.image.load('Cardgame-Bura\Code\PNG\\QC.PNG')
QC = pygame.transform.scale(QC,(150,150))

QD = pygame.image.load('Cardgame-Bura\Code\PNG\\QD.PNG')
QD = pygame.transform.scale(QD,(150,150))

QH = pygame.image.load('Cardgame-Bura\Code\PNG\\QH.PNG')
QH = pygame.transform.scale(QH,(150,150))

QS = pygame.image.load('Cardgame-Bura\Code\PNG\\QS.PNG')
QS = pygame.transform.scale(QS,(150,150))

KC = pygame.image.load('Cardgame-Bura\Code\PNG\\KC.PNG')
KC = pygame.transform.scale(KC,(150,150))

KD = pygame.image.load('Cardgame-Bura\Code\PNG\\KD.PNG')
KD = pygame.transform.scale(KD,(150,150))

KH = pygame.image.load('Cardgame-Bura\Code\PNG\\KH.PNG')
KH = pygame.transform.scale(KH,(150,150))

KS = pygame.image.load('Cardgame-Bura\Code\PNG\\KS.PNG')
KS = pygame.transform.scale(KS,(150,150))

AC = pygame.image.load('Cardgame-Bura\Code\PNG\\AC.PNG')
AC = pygame.transform.scale(AC,(150,150))

AD = pygame.image.load('Cardgame-Bura\Code\PNG\\AD.PNG')
AD = pygame.transform.scale(AD,(150,150))

AH = pygame.image.load('Cardgame-Bura\Code\PNG\\AH.PNG')
AH = pygame.transform.scale(AH,(150,150))

AS = pygame.image.load('Cardgame-Bura\Code\PNG\\AS.PNG')
AS = pygame.transform.scale(AS,(150,150))

# END OF deCK
Screen = pygame.display.set_mode((1200,800))
Red_Back = pygame.image.load('Cardgame-Bura\Code\PNG\\red_back.png')
Red_Back = pygame.transform.scale(Red_Back,(150,150))
card_Deck1 = pygame.image.load('Cardgame-Bura\Code\PNG\\Deck.png')
card_Deck1 = pygame.transform.scale(card_Deck1,(200,200))
button1 = pygame.image.load('Cardgame-Bura\Code\PNG\\button1.PNG')
button1 = pygame.transform.scale(button1,(100,100))
button2 = pygame.image.load('Cardgame-Bura\Code\PNG\\button2.PNG')
button2 = pygame.transform.scale(button2,(100,100))
button3 = pygame.image.load('Cardgame-Bura\Code\PNG\\button3.PNG')
button3 = pygame.transform.scale(button3,(500,500))
spades = pygame.image.load('Cardgame-Bura\Code\PNG\\spade1.png').convert_alpha()
spades = pygame.transform.scale(spades,(60,60))
diamond = pygame.image.load('Cardgame-Bura\Code\PNG\\diamond1.png').convert_alpha()
diamond = pygame.transform.scale(diamond,(60,60))
clubs = pygame.image.load('Cardgame-Bura\Code\PNG\\club1.png').convert_alpha()
clubs = pygame.transform.scale(clubs,(60,60))
heart = pygame.image.load('Cardgame-Bura\Code\PNG\\heart1.png').convert_alpha()
heart = pygame.transform.scale(heart,(60,60))
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('YOU LOST', True, ('black'))


fps = pygame.time.Clock()

Screen.fill((175,215,70))


class Card:
    def __init__(self,rank,suits,value,power,img,img_back,clicked,y_coordinate,x_coordinate):
        self.card_rank = rank
        self.card_suit = suits
        self.card_value = value
        self.card_power = power
        self.card_image = img
        self.card_clicked = clicked
        self.card_y = y_coordinate
        self.card_image_back = img_back  
        self.card_x = x_coordinate 
A_D = Card('A','D',11,5,AD,Red_Back,False,500,300)
K_D = Card('K','D',4,3,KD,Red_Back,False,500,300)
Q_D = Card('Q','D',3,2,QD,Red_Back,False,500,300)
J_D = Card('J','D',2,1,JD,Red_Back,False,500,300)
D_1 = Card('1','D',10,4,D10,Red_Back,False,500,300)

A_H = Card('A','H',11,5,AH,Red_Back,False,500,300)
K_H = Card('K','H',4,3,KH,Red_Back,False,500,300)
Q_H = Card('Q','H',3,2,QH,Red_Back,False,500,300)
J_H = Card('J','H',2,1,JH,Red_Back,False,500,300)
H_1 = Card('1','H',10,4,H10,Red_Back,False,500,300)

A_S = Card('A','S',11,5,AS,Red_Back,False,500,300)
K_S = Card('K','S',4,3,KS,Red_Back,False,500,300)
Q_S = Card('Q','S',3,2,QS,Red_Back,False,500,300)
J_S = Card('J','S',2,1,JS,Red_Back,False,500,300)
S_1 = Card('1','S',10,4,S10,Red_Back,False,500,300)

A_C = Card('A','C',11,5,AC,Red_Back,False,500,300)
K_C = Card('K','C',4,3,KC,Red_Back,False,500,300)
Q_C = Card('Q','C',3,2,QC,Red_Back,False,500,300)
J_C = Card('J','C',2,1,JC,Red_Back,False,500,300)
C_1 = Card('1','C',10,4,C10,Red_Back,False,500,300)    



# stores turn  true -> user false -> comp 
turn = True
user_made_move = False
computer_made_move = False
user_cards_taken = []
comp_cards_taken = []
user_score = 0
comp_score = 0
user_cards = []
comp_cards = []
user_bura_flag = False
comp_bura_flag = False
card_Deck = [A_D,K_D,Q_D,J_D,D_1,A_H,K_H,Q_H,J_H,H_1,A_S,K_S,Q_S,J_S,S_1,A_C,K_C,Q_C,J_C,C_1]
def shuffle():
    for n in range(500):
        var1 = random.randint(0,19)
        var2 = random.randint(0,12)
        tmp = card_Deck[var1]
        card_Deck[var1] = card_Deck[var2]
        card_Deck[var2] = tmp   
def kozir():
    var = random.randint(0,3)
    if var == 0:
        kozir = 'H'
    elif var == 1:
        kozir = 'D'
    elif var == 2:
        kozir = 'C'
    else:
        kozir = 'S'
    return kozir
def kozir_render():
    if koziri == 'D':
        Screen.blit(diamond,(72,320))
    elif koziri == 'S':
        Screen.blit(spades,(72,320))
    elif koziri == 'H':
        Screen.blit(heart,(72,320))

    else:
        Screen.blit(clubs,(72,320))
def Update_cards(list,list2):
    if len(card_Deck) != 0:
        while(len(list) != 3 and len(list2) != 3 and len(card_Deck) != 0):
            var = random.randrange(0, len(card_Deck))
            list.insert(0,card_Deck[var])
            card_Deck.pop(var)    
            var2 = random.randrange(0, len(card_Deck))       
            list2.insert(0,card_Deck[var2])
            card_Deck.pop(var2)
        
def check_move():
    global user_bura_flag,comp_bura_flag
    if turn == True:
        if len(user_cards) == 1:
             suits1 = user_cards[0].card_suit
             card_y1 = user_cards[0].card_y
        elif len(user_cards) == 2:
            suits1 = user_cards[0].card_suit
            card_y1 = user_cards[0].card_y
            suits2 = user_cards[0].card_suit
            card_y2 = user_cards[0].card_y
        else:
            suits1 = user_cards[0].card_suit
            suits2 = user_cards[1].card_suit
            suits3 = user_cards[2].card_suit
            card_y1 = user_cards[0].card_y
            card_y2 = user_cards[1].card_y
            card_y3 = user_cards[2].card_y
        if len(user_cards) == 3:
            if comp_cards[0].card_clicked == True and comp_cards[1].card_clicked == True and comp_cards[2].card_clicked == True:
                if user_cards[0].card_y == 450 and user_cards[1].card_y == 450 and user_cards[2].card_y == 450:
                    return True
                else:
                    return False
            if card_y1 == 450 and card_y2 == 450 and card_y3 == 500:
                if suits1 == suits2:
                    return True
                else:
                    return False
            elif card_y1 == 450 and card_y2 == 500 and card_y3 == 450:
                if suits1 == suits3:
                    return True
                else:
                    return False
            elif card_y1 == 500 and card_y2 == 450 and card_y3 == 450:
                if suits2 == suits3:
                    return True
                else:
                    return False
            elif card_y1 == 450 and card_y2 == 450 and card_y3 == 450:
                if suits1 == suits2 and suits1 == suits3:
                    return True
                else:
                    return False
            elif card_y1 == 500 and card_y2 == 500 and card_y3 == 500:
                return False
            else:
                return True
        elif len(user_cards) == 2:
            if card_y1 == 450 and card_y2 == 450:
                if suits1 == suits2:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return True
    # if it is computers move       
    else:
        user_card_counter = 0
        comp_card_counter = 0
    
        if user_cards[0].card_y == 500 and user_cards[1].card_y == 500 and user_cards[2].card_y == 500:
            return False
        if user_cards[0].card_suit == user_cards[1].card_suit and user_cards[0].card_suit == user_cards[2].card_suit:
            #temporary solution
            user_bura_flag = True
            
        if comp_cards[0].card_suit == comp_cards[1].card_suit and comp_cards[0].card_suit == comp_cards[2].card_suit:
            comp_bura_flag = True
            
        for i in range(len(comp_cards)):
            if comp_cards[i].card_clicked == True:
                comp_card_counter += 1
            if user_cards[i].card_y == 450:
                user_card_counter += 1
        if user_card_counter != comp_card_counter and user_bura_flag == True:
            return True
        elif user_card_counter == comp_card_counter:
            return True
        else:
            return False  
        


shuffle()
koziri = 'H'
comp_cards = [K_D,A_H,D_1]
user_cards = [J_D,Q_C,A_D]
card_Deck.remove(A_D)
card_Deck.remove(J_D)
card_Deck.remove(A_H)
card_Deck.remove(D_1)
card_Deck.remove(Q_C)
card_Deck.remove(K_D)
#Update_cards(user_cards,comp_cards)



def card_print():
    
    print("User:"+"["+user_cards[0].card_rank + user_cards[0].card_suit + "," + user_cards[1].card_rank + user_cards[1].card_suit + "," + user_cards[2].card_rank + user_cards[2].card_suit+"]")
    print("Comp:"+"["+comp_cards[0].card_rank + comp_cards[0].card_suit + "," + comp_cards[1].card_rank + comp_cards[1].card_suit + "," +comp_cards[2].card_rank + comp_cards[2].card_suit+"]")

def who_takes_cards():
    user_card_values = []
    comp_card_values = []
    for i in range(len(user_cards)):
        if user_cards[i].card_y < 500:
            user_card_values.append(user_cards[i].card_power)
        if comp_cards[i].card_clicked == True:
            comp_card_values.append(comp_cards[i].card_power)
    print("User_card_values:",user_card_values)
    print("Comp_Card_values:",comp_card_values)
    if len(user_card_values) == 1:
        if user_card_values[0] > comp_card_values[0]:
            return True
        else:
            return False
    elif len(user_card_values) == 2:
       user_card_values.sort()
       comp_card_values.sort()
       if turn == False:
            if user_card_values[0] > comp_card_values[0] and user_card_values[1] > comp_card_values[1]:
                return True
            else:
                return False
       else:
            if comp_card_values[0] > user_card_values[0] and comp_card_values[1] > user_card_values[1]:
                return False
            else:
                return True
    elif len(user_card_values) == 3:
        user_card_values.sort()
        comp_card_values.sort()
        if turn == False and user_bura_flag == False:
            if user_card_values[0] > comp_card_values[0] and user_card_values[1] > comp_card_values[1] and user_card_values[2] > comp_card_values[2]:
                return True
            else:
                return False
        else:
            if comp_bura_flag == True:
                if user_card_values[0] > comp_card_values[0] and user_card_values[1] > comp_card_values[1] and user_card_values[2] > comp_card_values[2]:
                    return True
                else:
                    return False
            else:
                if comp_card_values[0] > user_card_values[0] and comp_card_values[1] > user_card_values[1] and comp_card_values[2] > user_card_values[2]:
                    return False
                else:
                    return True

def update_card_power():
    suit = ""
    if turn == True:
        if user_bura_flag == True:
            for i in range(len(comp_cards)):
                if comp_cards[i].card_suit != user_cards[0].card_suit and comp_cards[i].card_suit != koziri:
                    comp_cards[i].card_power = 0
        if comp_bura_flag == True:
             for i in range(len(user_cards)):
                if user_cards[i].card_suit != comp_cards[0].card_suit and user_cards[i].card_suit != koziri:
                    user_cards[i].card_power = 0
        else:
            for i in range(len(user_cards)):
                if user_cards[i].card_suit == koziri:
                    if user_cards[i].card_power < 20:
                        user_cards[i].card_power = user_cards[i].card_power * 20
                if comp_cards[i].card_suit == koziri:
                    if comp_cards[i].card_power < 20:
                        comp_cards[i].card_power = comp_cards[i].card_power * 20
                if user_cards[i].card_y == 450 and user_cards[i].card_suit != koziri:
                    suit = user_cards[i].card_suit
                    if user_cards[i].card_power < 6:
                        user_cards[i].card_power = user_cards[i].card_power + 5
            for i in range(len(user_cards)):
                if comp_cards[i].card_suit == suit:
                    if comp_cards[i].card_power < 6:
                        comp_cards[i].card_power = comp_cards[i].card_power + 5
    else:
        if comp_bura_flag == True:
            for i in range(len(user_cards)):
                if user_cards[i].card_suit != comp_cards[0].card_suit and user_cards[i].card_suit != koziri:
                    user_cards[i].card_power = 0
        if user_bura_flag == True:
            for i in range(len(comp_cards)):
                if comp_cards[i].card_suit != user_cards[0].card_suit and comp_cards[i].card_suit != koziri:
                    comp_cards[i].card_power = 0
        else:
            for i in range(len(comp_cards)):
                if user_cards[i].card_suit == koziri:
                    if user_cards[i].card_power < 20:
                        user_cards[i].card_power = user_cards[i].card_power * 20
                if comp_cards[i].card_suit == koziri:
                    if comp_cards[i].card_power < 20:
                        comp_cards[i].card_power = comp_cards[i].card_power * 20
                if comp_cards[i].card_clicked == True and comp_cards[i].card_suit != koziri:
                    suit = comp_cards[i].card_suit 
                    if comp_cards[i].card_power < 6:
                        comp_cards[i].card_power = comp_cards[i].card_power + 5
            for i in range(len(comp_cards)):
                if user_cards[i].card_suit == suit:
                    if user_cards[i].card_power < 6:
                        user_cards[i].card_power = user_cards[i].card_power + 5 

def computer_move_on_user_turn():
    global user_made_move,comp_bura_flag
    
    update_card_power()
    user_card_score = []
    comp_card_score = []
    card_counter = 0
    
    for i in range(len(user_cards)):
        if user_cards[i].card_y == 450:
            card_counter += 1
            user_card_score.append(user_cards[i])
        comp_card_score.append(comp_cards[i].card_power)
    #one card was played
    if len(comp_cards) == 3:
        if card_counter == 1:
            if user_card_score[0].card_value > 9 and user_card_score[0].card_suit != koziri:
                if comp_cards[0].card_suit == comp_cards[1].card_suit and comp_cards[0].card_suit == comp_cards[2].card_suit:
                    comp_cards[0].card_clicked = True
                    comp_cards[1].card_clicked = True
                    comp_cards[2].card_clicked = True
                    user_made_move = False
                    comp_bura_flag = True
                    update_card_power()
                    
                elif comp_cards[0].card_suit == comp_cards[1].card_suit and comp_cards[2].card_power > user_card_score[0].card_power :
                    comp_cards[2].card_clicked = True
                elif  comp_cards[0].card_suit == comp_cards[2].card_suit and comp_cards[1].card_power > user_card_score[0].card_power:
                    comp_cards[1].card_clicked = True
                elif comp_cards[1].card_suit == comp_cards[2].card_suit and comp_cards[0].card_power > user_card_score[0].card_power:
                    comp_cards[0].card_clicked = True
                elif comp_cards[0].card_power > user_card_score[0].card_power and comp_cards[1].card_power > user_card_score[0].card_power:
                    if comp_cards[0].card_power > comp_cards[1].card_power:
                         comp_cards[0].card_clicked = True
                    else:
                         comp_cards[1].card_clicked = True
                elif comp_cards[0].card_power > user_card_score[0].card_power and comp_cards[2].card_power > user_card_score[0].card_power:
                    if comp_cards[0].card_power > comp_cards[2].card_power:
                         comp_cards[0].card_clicked = True
                    else:
                         comp_cards[2].card_clicked = True
                elif comp_cards[1].card_power > user_card_score[0].card_power and comp_cards[2].card_power > user_card_score[0].card_power:
                    if comp_cards[1].card_power > comp_cards[2].card_power:
                         comp_cards[1].card_clicked = True
                    else:
                         comp_cards[2].card_clicked = True
                elif comp_cards[0].card_power > user_card_score[0].card_power or comp_cards[1].card_power > user_card_score[0].card_power or comp_cards[2].card_power > user_card_score[0].card_power:
                    if comp_cards[0].card_power > user_card_score[0].card_power:
                        comp_cards[0].card_clicked = True
                    elif comp_cards[1].card_power > user_card_score[0].card_power:
                        comp_cards[0].card_clicked = True
                    else:
                        comp_cards[2].card_clicked = True
                elif comp_cards[0].card_suit == comp_cards[1].card_suit and comp_cards[2].card_value < 10:
                    comp_cards[2].card_clicked = True
                elif  comp_cards[0].card_suit == comp_cards[2].card_suit and comp_cards[1].card_value < 10:
                    comp_cards[1].card_clicked = True
                elif comp_cards[1].card_suit == comp_cards[2].card_suit and comp_cards[0].card_value < 10:
                    comp_cards[0].card_clicked = True
                else:
                    min = 0
                    if comp_cards[0].card_value > comp_cards[1].card_value and comp_cards[1].card_value < comp_cards[2].card_value:
                        min = 1
                    if comp_cards[0].card_value > comp_cards[2].card_value and comp_cards[2].card_value < comp_cards[1].card_value:
                        min = 2
                    comp_cards[min].card_clicked = True
            elif user_card_score[0].card_value > 9 and user_card_score[0].card_suit == koziri:
                if comp_cards[0].card_suit == comp_cards[1].card_suit and comp_cards[0].card_suit == comp_cards[2].card_suit:
                    comp_cards[0].card_clicked = True
                    comp_cards[1].card_clicked = True
                    comp_cards[2].card_clicked = True
                    user_made_move = False
                    comp_bura_flag = True
                elif comp_cards[0].card_power > user_card_score[0].card_power or comp_cards[1].card_power > user_card_score[0].card_power or comp_cards[2].card_power > user_card_score[0].card_power:
                    if comp_cards[0].card_power > user_card_score[0].card_power:
                        comp_cards[0].card_clicked = True
                    elif comp_cards[1].card_power > user_card_score[0].card_power:
                        comp_cards[0].card_clicked = True
                    else:
                        comp_cards[2].card_clicked = True
                else:
                    min = 0
                    if comp_cards[0].card_value > comp_cards[1].card_value and comp_cards[1].card_value < comp_cards[2].card_value:
                        min = 1
                    if comp_cards[0].card_value > comp_cards[2].card_value and comp_cards[2].card_value < comp_cards[1].card_value:
                        min = 2
                    comp_cards[min].card_clicked = True
            elif user_card_score[0].card_value < 9 and user_card_score[0].card_suit != koziri:
                if comp_cards[0].card_suit == comp_cards[1].card_suit and comp_cards[0].card_suit == comp_cards[2].card_suit:
                    comp_cards[0].card_clicked = True
                    comp_cards[1].card_clicked = True
                    comp_cards[2].card_clicked = True
                    user_made_move = False
                    comp_bura_flag = True
                    update_card_power()
                elif comp_cards[0].card_suit == user_card_score[0].card_suit and comp_cards[0].card_value > 9:
                     comp_cards[0].card_clicked = True
                elif comp_cards[1].card_suit == user_card_score[0].card_suit and comp_cards[1].card_value > 9:
                     comp_cards[1].card_clicked = True
                elif comp_cards[2].card_suit == user_card_score[0].card_suit and comp_cards[2].card_value > 9:
                     comp_cards[2].card_clicked = True
                elif comp_cards[0].card_suit == comp_cards[1].card_suit and comp_cards[2].card_power > user_card_score[0].card_power :
                    comp_cards[2].card_clicked = True
                elif  comp_cards[0].card_suit == comp_cards[2].card_suit and comp_cards[1].card_power > user_card_score[0].card_power:
                    comp_cards[1].card_clicked = True
                elif comp_cards[1].card_suit == comp_cards[2].card_suit and comp_cards[0].card_power > user_card_score[0].card_power:
                    comp_cards[0].card_clicked = True
                elif comp_cards[0].card_suit == comp_cards[1].card_suit and comp_cards[2].card_value < 10:
                    comp_cards[2].card_clicked = True
                elif  comp_cards[0].card_suit == comp_cards[2].card_suit and comp_cards[1].card_value < 10:
                    comp_cards[1].card_clicked = True
                elif comp_cards[1].card_suit == comp_cards[2].card_suit and comp_cards[0].card_value < 10:
                    comp_cards[0].card_clicked = True
                else:
                    min = 0
                    if comp_cards[0].card_value > comp_cards[1].card_value and comp_cards[1].card_value < comp_cards[2].card_value:
                        min = 1
                    if comp_cards[0].card_value > comp_cards[2].card_value and comp_cards[2].card_value < comp_cards[1].card_value:
                        min = 2
                    comp_cards[min].card_clicked = True
            else:
                if comp_cards[0].card_suit == comp_cards[1].card_suit and comp_cards[0].card_suit == comp_cards[2].card_suit:
                    comp_cards[0].card_clicked = True
                    comp_cards[1].card_clicked = True
                    comp_cards[2].card_clicked = True
                    user_made_move = False
                    comp_bura_flag = True
                    update_card_power()
                    
                elif comp_cards[0].card_suit == comp_cards[1].card_suit and comp_cards[2].card_power > user_card_score[0].card_power :
                    comp_cards[2].card_clicked = True
                elif  comp_cards[0].card_suit == comp_cards[2].card_suit and comp_cards[1].card_power > user_card_score[0].card_power:
                    comp_cards[1].card_clicked = True
                elif comp_cards[1].card_suit == comp_cards[2].card_suit and comp_cards[0].card_power > user_card_score[0].card_power:
                    comp_cards[0].card_clicked = True
                elif comp_cards[0].card_suit == comp_cards[1].card_suit and comp_cards[2].card_value < 10:
                    comp_cards[2].card_clicked = True
                elif  comp_cards[0].card_suit == comp_cards[2].card_suit and comp_cards[1].card_value < 10:
                    comp_cards[1].card_clicked = True
                elif comp_cards[1].card_suit == comp_cards[2].card_suit and comp_cards[0].card_value < 10:
                    comp_cards[0].card_clicked = True
                else:
                    min = 0
                    if comp_cards[0].card_value > comp_cards[1].card_value and comp_cards[1].card_value < comp_cards[2].card_value:
                        min = 1
                    if comp_cards[0].card_value > comp_cards[2].card_value and comp_cards[2].card_value < comp_cards[1].card_value:
                        min = 2
                    comp_cards[min].card_clicked = True
        elif card_counter == 3:
            comp_cards[0].card_clicked = True
            comp_cards[1].card_clicked = True
            comp_cards[2].card_clicked = True
            
        else:
            if comp_cards[0].card_suit == comp_cards[1].card_suit and comp_cards[0].card_suit == comp_cards[2].card_suit:
                    comp_cards[0].card_clicked = True
                    comp_cards[1].card_clicked = True
                    comp_cards[2].card_clicked = True
                    user_made_move = False
                    comp_bura_flag = True
                    update_card_power()
            else:
                #comp_cards[0].card_clicked = True
                #comp_cards[1].card_clicked = True

                # sort user card by power
                sum_of_user_score = user_card_score[0].card_power + user_card_score[1].card_power             
                if user_card_score[0].card_power > user_card_score[1].card_power:
                    tmp = user_card_score[0].card_power
                    user_card_score[0].card_power = user_card_score[1].card_power
                    user_card_score[1].card_power = tmp
                for i in range(len(comp_card_score)):
                    if comp_card_score[i] > user_card_score[1].card_power and comp_card_score[i] > 19:
                        comp_card_score[i] = user_card_score[1].card_power + 1
                sum_of_user_score = user_card_score[0].card_power + user_card_score[1].card_power
                comp_card_score.sort()
                
                comp_sum_min = comp_card_score[0] + comp_card_score[1]
                comp_sum_mid = comp_card_score[0] + comp_card_score[2]
                comp_sum_max = comp_card_score[1] + comp_card_score[2]
                print("SUM_USER:",sum_of_user_score)
                print("SUM_MIN:",comp_sum_min)
                print("SUM_MID:",comp_sum_mid)
                print("SUM_MAX:",comp_sum_max)
                # if comp_card len == 3 
                if comp_sum_min > sum_of_user_score:
                    print("YVELANAIRAD MIMAQ")
                    click_counter = 0 
                    for i in range(len(comp_cards)):
                        if click_counter == 2:
                            break
                        if comp_cards[i].card_value > 9 and comp_cards[i].card_suit != koziri:
                            comp_cards[i].card_clicked = True
                            click_counter += 1
                        elif comp_cards[i].card_value < 9 and comp_cards[i].card_suit != koziri:
                            comp_cards[i].card_clicked = True
                            click_counter += 1 
                        else:
                            if comp_cards[i].card_suit == koziri and i == 1 or comp_cards[i].card_suit == koziri and i == 0:
                                if comp_cards[i+1].card_suit != koziri:
                                    i = i+1
                                else:
                                    comp_cards[i].card_clicked = True
                                    click_counter += 1 

                        
                    
                elif comp_sum_mid > sum_of_user_score:
                    print("ORNAIRAD MIMAQ")
                    click_counter2 = 0 
                    for i in range(len(user_cards)):
                        if click_counter2 == 2:
                            break
                        if comp_cards[i].comp_suit != koziri and comp_cards[i].card_power > user_card_score[0].card_power or comp_cards[i].comp_suit != koziri and comp_cards[i].card_power > user_card_score[1].card_power:
                            comp_cards[i].card_clicked = True
                            click_counter2 += 1
                        elif comp_cards[i].comp_suit == koziri and comp_cards[i].card_power > user_card_score[0].card_power or comp_cards[i].comp_suit == koziri and comp_cards[i].card_power > user_card_score[1].card_power:
                            comp_cards[i].card_clicked = True
                            click_counter2 += 1
                elif comp_sum_max > sum_of_user_score:
                    print("MXOLOD ERTI GZIT MIMAQ")
                    if comp_cards[0].card_power > user_card_score[0].card_power or   comp_cards[0].card_power > user_card_score[1].card_power:
                        comp_cards[0].card_clicked = True
                    if comp_cards[1].card_power > user_card_score[0].card_power or   comp_cards[1].card_power > user_card_score[1].card_power:
                        comp_cards[1].card_clicked = True
                    if comp_cards[2].card_power > user_card_score[0].card_power or   comp_cards[2].card_power > user_card_score[1].card_power:
                        comp_cards[2].card_clicked = True
                else:
                    print("AR SHEMIDZLIA WAVIGO")
                    comp_cards[0].card_clicked = True
                    comp_cards[1].card_clicked = True

                
                    
                

def computer_move_on_comp_turn():
    global computer_made_move,user_bura_flag,comp_bura_flag
    if turn == False:
        if user_bura_flag == True:
             comp_cards[0].card_clicked = True
             comp_cards[1].card_clicked = True
             comp_cards[2].card_clicked = True
             update_card_power()
             coordinate_update(comp_cards,False)
             computer_made_move = True
             
        else:
           # if len(comp_cards) == 3:
            if comp_cards[0].card_suit == comp_cards[1].card_suit and comp_cards[0].card_suit == comp_cards[2].card_suit:
                        comp_cards[0].card_clicked = True
                        comp_cards[1].card_clicked = True
                        comp_cards[2].card_clicked = True
                        comp_bura_flag = True
                        update_card_power()
                        coordinate_update(comp_cards,False)
                        computer_made_move = True

            else:        
                comp_cards[0].card_clicked = True
                update_card_power()
                coordinate_update(comp_cards,False)
                computer_made_move = True

def coordinate_update(list,bool1):
    if bool1 == True:
        for i in range(len(list)):
            if list[i].card_y == 450:
                list[i].card_y = 300
    else:
        for i in range(len(list)):
            if list[i].card_clicked == True:
                list[i].card_y = 650

def process():
    global turn,comp_score,user_score,user_bura_flag,comp_bura_flag
    print("WHO TAKES CARDS:",who_takes_cards())
    if who_takes_cards() == True:
        turn = True
        for i in range(len(user_cards)):
            if user_cards[i].card_y == 300:
                user_cards_taken.append(user_cards[i])
                user_score += user_cards[i].card_value
            if comp_cards[i].card_clicked == True:
                user_cards_taken.append(comp_cards[i])
                user_score += comp_cards[i].card_value
    else:
        turn = False
        for i in range(len(user_cards)):
            if user_cards[i].card_y == 300:
                comp_cards_taken.append(user_cards[i])
                comp_score += user_cards[i].card_value
            if comp_cards[i].card_clicked == True:
                comp_cards_taken.append(comp_cards[i])
                comp_score += comp_cards[i].card_value
   

    for i in reversed(range(len(user_cards))):
        if user_cards[i].card_y == 300:
            user_cards.pop(i)
        if comp_cards[i].card_clicked == True:
            comp_cards.pop(i)
    if user_bura_flag == True or comp_bura_flag == True:
        user_bura_flag = False
        comp_bura_flag = False
    if len(card_Deck) != 0:
        Update_cards(user_cards,comp_cards)

def user_cards_render(list):
    x_coordinate = 300
    for i in range(len(list)):
        Screen.blit(list[i].card_image,(x_coordinate,list[i].card_y))        
        x_coordinate += 100
    
def comp_cards_render(list):
    x_coordinate = 300
    for i in range(len(list)): 
        #if turn == True:          
            #if comp_cards[i].card_y == 650 and who_takes_cards() == False:
                #comp_cards[i].card_image_back = comp_cards[i].card_image
        #else:
            #if comp_cards[i].card_y == 650:
                #comp_cards[i].card_image_back = comp_cards[i].card_image
        #Screen.blit(comp_cards[i].card_image_back,(x_coordinate,comp_cards[i].card_y-450))
        Screen.blit(comp_cards[i].card_image,(x_coordinate,comp_cards[i].card_y-450))
        x_coordinate += 100
  
    


Surface = pygame.Surface((1200,800))
Surface.fill((175,215,70))



   
                
                
                
            
                
                
            

                 









        



while True:
    if user_made_move == True and computer_made_move == True:
        pygame.time.wait(750)
        process()
        user_made_move = False
        computer_made_move = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
           if event.button == 1:
               if 523 <= mouse[0] <= 615 and 677 <= mouse[1] <= 738:
                   print("clicked at 523-----")
                   print("USER SCORE:",user_score)
                   print("COMP SCORE:",comp_score)
                   card_print()
                   print("TURN:",turn)
               if 400 <= mouse[0] <= 492 and 678 <= mouse[1] <= 740:  
                   print(check_move())
                   if check_move() == True:
                      user_made_move = True
                      if turn == True and comp_bura_flag == False:
                        computer_move_on_user_turn()
                        coordinate_update(comp_cards,False)
                        computer_made_move = True
                      if comp_bura_flag == True:
                          coordinate_update(comp_cards,False)
                          computer_made_move = True   
                      coordinate_update(user_cards,True) 
                   else:
                       user_cards[0].card_y = 500
                       user_cards[1].card_y = 500
                       user_cards[2].card_y = 500
               if 318 <= mouse[0] <= 395 and 510 <= mouse[1] <= 639:
                       if user_made_move == False:
                            if user_cards[0].card_y == 500:
                                user_cards[0].card_y = 450
                            else:
                                user_cards[0].card_y = 500
                            
               if 410 <= mouse[0] <= 491 and 514 <= mouse[1] <= 638:
                         if user_made_move == False:
                            if user_cards[1].card_y == 500:
                                user_cards[1].card_y = 450
                            else:
                                user_cards[1].card_y = 500
                            
               if 512 <= mouse[0] <= 639 and 510 <= mouse[1] <= 636:
                        if user_made_move == False:
                            if user_cards[2].card_y == 500:
                                user_cards[2].card_y = 450
                            else:
                                user_cards[2].card_y = 500
    Screen.blit(Surface,(0,0))
    mouse = pygame.mouse.get_pos()
    Screen.blit(card_Deck1,(0,250))      
    kozir_render()
    Screen.blit(button2,(400,660))
    Screen.blit(button2,(520,660))
    computer_move_on_comp_turn()
    user_cards_render(user_cards)
    comp_cards_render(comp_cards)
        
    pygame.display.update()
    fps.tick(60)
