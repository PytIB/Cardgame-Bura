#bura da maliutkaa gasasworebeli da plius 2 karts ro chadixar 
import pygame
import random







pygame.init()


# start of deck 


C10 = pygame.image.load('PNG\\10C.PNG')
C10 = pygame.transform.scale(C10,(150,150))

D10 = pygame.image.load('PNG\\10D.PNG')
D10 = pygame.transform.scale(D10,(150,150))

H10 = pygame.image.load('PNG\\10H.PNG')
H10 = pygame.transform.scale(H10,(150,150))

S10 = pygame.image.load('PNG\\10S.PNG')
S10 = pygame.transform.scale(S10,(150,150))

JC = pygame.image.load('PNG\\JC.PNG')
JC = pygame.transform.scale(JC,(150,150))

JD = pygame.image.load('PNG\\JD.PNG')
JD = pygame.transform.scale(JD,(150,150))

JH = pygame.image.load('PNG\\JH.PNG')
JH = pygame.transform.scale(JH,(150,150))

JS = pygame.image.load('PNG\\JS.PNG')
JS = pygame.transform.scale(JS,(150,150))

QC = pygame.image.load('PNG\\QC.PNG')
QC = pygame.transform.scale(QC,(150,150))

QD = pygame.image.load('PNG\\QD.PNG')
QD = pygame.transform.scale(QD,(150,150))

QH = pygame.image.load('PNG\\QH.PNG')
QH = pygame.transform.scale(QH,(150,150))

QS = pygame.image.load('PNG\\QS.PNG')
QS = pygame.transform.scale(QS,(150,150))

KC = pygame.image.load('PNG\\KC.PNG')
KC = pygame.transform.scale(KC,(150,150))

KD = pygame.image.load('PNG\\KD.PNG')
KD = pygame.transform.scale(KD,(150,150))

KH = pygame.image.load('PNG\\KH.PNG')
KH = pygame.transform.scale(KH,(150,150))

KS = pygame.image.load('PNG\\KS.PNG')
KS = pygame.transform.scale(KS,(150,150))

AC = pygame.image.load('PNG\\AC.PNG')
AC = pygame.transform.scale(AC,(150,150))

AD = pygame.image.load('PNG\\AD.PNG')
AD = pygame.transform.scale(AD,(150,150))

AH = pygame.image.load('PNG\\AH.PNG')
AH = pygame.transform.scale(AH,(150,150))

AS = pygame.image.load('PNG\\AS.PNG')
AS = pygame.transform.scale(AS,(150,150))

# END OF deCK

Screen = pygame.display.set_mode((1200,800))

fps = pygame.time.Clock()

Screen.fill((175,215,70))






class Card:
    def __init__(self) -> None:
        self.suits = ['Diamond','Heart','Spade','Club']
        self.rank = ['1','J','Q','K','A']
        self.cardDeck = []
    def get_deck(self):
        for i in self.suits:
            for j in self.rank:
                self.card = j + i
                self.cardDeck.append(self.card)
    
    def get_shuffle(self):
        for n in range(500):
            self.var1 = random.randint(0,19)
            self.var2 = random.randint(0,12)
            self.tmp = self.cardDeck[self.var1]
            self.cardDeck[self.var1] = self.cardDeck[self.var2]
            self.cardDeck[self.var2] = self.tmp



cards = Card()
cards.get_deck()
cards.get_shuffle()
Red_Back = pygame.image.load('red_back.png')
Red_Back = pygame.transform.scale(Red_Back,(150,150))
card_Deck = pygame.image.load('Deck.png')
card_Deck = pygame.transform.scale(card_Deck,(200,200))
button1 = pygame.image.load('PNG\\button1.PNG')
button1 = pygame.transform.scale(button1,(150,150))
button2 = pygame.image.load('PNG\\button2.PNG')
button2 = pygame.transform.scale(button2,(100,100))
button3 = pygame.image.load('PNG\\button3.PNG')
button3 = pygame.transform.scale(button3,(500,500))
spades = pygame.image.load('PNG\\spade1.png').convert_alpha()
spades = pygame.transform.scale(spades,(60,60))
diamond = pygame.image.load('PNG\\diamond1.png').convert_alpha()
diamond = pygame.transform.scale(diamond,(60,60))
clubs = pygame.image.load('PNG\\club1.png').convert_alpha()
clubs = pygame.transform.scale(clubs,(60,60))
heart = pygame.image.load('PNG\\heart1.png').convert_alpha()
heart = pygame.transform.scale(heart,(60,60))
font = pygame.font.Font('freesansbold.ttf', 32)
font1 = pygame.font.Font('freesansbold.ttf', 26)
font2 = pygame.font.Font('freesansbold.ttf', 18)
text = font.render('YOU LOST', True, ('black'))
text1 = font.render('BURA', True, ('black'))
text2 = font.render('YOU WON', True, ('black'))
text_move = font1.render('MOVE', True, ('black'))
text_var = font1.render('VAR', True, ('black'))
text_new_game = font2.render('New Game', True, ('orange'))

#variables
new_game_flag = False
Deck = cards.cardDeck
user_cards = []
comp_cards = []
Deck_is_empthy = False
total_score_user = 0
total_score_comp = 0
user_won = False
comp_won = False
move_made = False
koziri = ''
user_score_counter = 0
comp_score_counter = 0
computerTurn = False
game_over_flag = False
img_user = []
img_comp = []
img_taken_comp = []
user_suits = []
comp_suits = []
flags_user = [False,False,False]
flags_comp = [False,False,False]
cards_taken_user = []
cards_taken_comp = []
user_move_score = []
comp_move_score = []
comp_bura_flag = False
comp_maliutka_flag = False
user_bura_flag = False
user_maliutka_flag= False
Update = False
comps_miyvas = False

winner_comp = False
Surface = pygame.Surface((1200,800))
Surface.fill((175,215,70))

    #returns kozir
def kozir():

    var = random.randint(0,3)
    koziri =cards.suits[var]
    
    return koziri

    #renderds kozir
def kozir_render():
    if koziri == 'Diamond':
        Screen.blit(diamond,(72,320))
    elif koziri == 'Spade':
        Screen.blit(spades,(72,320))
    elif koziri == 'Heart':
        Screen.blit(heart,(72,320))

    else:
        Screen.blit(clubs,(72,320))
        
                
    #updates user_Cards and comp_cards updates Deck
def Update_cards(list,list2):
    if len(Deck) != 0:
        while(len(list) != 3 and len(list2) != 3 and len(Deck) != 0):
            var = random.randrange(0, len(Deck))
            list.insert(0,Deck[var])
            Deck.pop(var)    
            var2 = random.randrange(0, len(Deck))       
            list2.insert(0,Deck[var2])
            Deck.pop(var2)
  
    # puts suits in list2
def get_suits(list1,list2):
    str1 =''
    for i in range(len(list1)):
        str1 = list1[i]
        if str1[1] == 'D':
            list2.append('D')
        elif str1[1] == 'H':
            list2.append('H')
        elif str1[1] == 'C':
            list2.append('C')
        else:
            list2.append('S')           
        




    #checks if user move is possible 
def check_move():
    flag1 = flags_user[0]
    flag2 = flags_user[1]
    flag3 = flags_user[2]
    get_suits(user_cards,user_suits)
    if flag1 == True and flag2 == False and flag3 == False:
        user_suits.clear()
        return True
    if flag1 == False and flag2 == True and flag3 == False:
        user_suits.clear()
        return True
    if flag1 == False and flag2 == False and flag3 == True:
        user_suits.clear()
        return True
    if flag1 == True and flag2 == True and flag3 == False:
        if user_suits[0] == user_suits[1]:
            user_suits.clear()
            return True 
        else:
            user_suits.clear()
            return False
    if flag1 == True and flag2 == False and flag3 == True:
        if user_suits[0] == user_suits[2]:
            user_suits.clear()
            return True
        else:
            user_suits.clear()
            return False
    if  flag1 == False and flag2 == True and flag3 == True:
        if user_suits[1] == user_suits[2]:
            user_suits.clear()
            return True
        else:
            user_suits.clear()
            return False
    if flag1 == True and flag2 == True and flag3 == True:
        if user_suits[0] == user_suits[1] and user_suits[0] == user_suits[2]:
            user_suits.clear()
            return True
        else:
            user_suits.clear()
            return False
    
def check_move_after_comp_move():
    counter_comp = 0
    counter_user = 0
    get_suits(user_cards,user_suits)
    for i in range(len(flags_comp)):
        if flags_comp[i] == True:
            counter_comp += 1
        if flags_user[i] == True:
            counter_user += 1
    if counter_comp == 1 and counter_user == 1:
        user_suits.clear()
        return True
    if counter_comp == 1 and counter_user == 2:
        user_suits.clear()
        return False
    if counter_comp == 1 and counter_user == 3:
        if len(user_cards) == 3:
            if user_suits[0] == user_suits[1] and user_suits[0] == user_suits[2]:
                user_suits.clear()
                return True
            else:
                user_suits.clear()
                return False
    if counter_comp == 2 and counter_user == 1:
        user_suits.clear()
        return False
    if counter_comp == 2 and counter_user == 2:
        user_suits.clear()
        return True
    if counter_comp == 2 and counter_user == 3:
        if len(user_cards) == 3:
            if user_suits[0] == user_suits[1] and user_suits[0] == user_suits[2]:
                user_suits.clear()
                return True
            else:
                user_suits.clear()
                return False
    if counter_comp == 3 and counter_user != 3:
        user_suits.clear()
        return False
    else:
        user_suits.clear()
        return True

     # puts score at user_move_score
def user_score():
    if computerTurn == True:
        for i in range(len(user_cards)):
            str1 = user_cards[i]
            if str1[0] == 'J' and str1[1] == koziri[0]:
                user_move_score.append(50)
            if str1[0] == 'J' and str1[1] != koziri[0]:
                user_move_score.append(1)
            if str1[0] == 'Q' and str1[1] == koziri[0]:
                user_move_score.append(60)
            if str1[0] == 'Q' and str1[1] != koziri[0]:
                user_move_score.append(2)
            if str1[0] == 'K' and str1[1] == koziri[0]:
                user_move_score.append(70)
            if str1[0] == 'K' and str1[1] != koziri[0]:
                user_move_score.append(3)
            if str1[0] == '1' and str1[1] == koziri[0]:
                user_move_score.append(80)
            if str1[0] == '1' and str1[1] != koziri[0]:
                user_move_score.append(4)
            if str1[0] == 'A' and str1[1] == koziri[0]:
                user_move_score.append(100)
            if str1[0] == 'A' and str1[1] != koziri[0]:
                user_move_score.append(5)
    else:
        for i in range(len(user_cards)):
            str1 = user_cards[i]
            if str1[0] == 'J' and str1[1] == koziri[0]:
                user_move_score.append(50)
            if str1[0] == 'J' and str1[1] != koziri[0]:
                user_move_score.append(6)
            if str1[0] == 'Q' and str1[1] == koziri[0]:
                user_move_score.append(60)
            if str1[0] == 'Q' and str1[1] != koziri[0]:
                user_move_score.append(7)
            if str1[0] == 'K' and str1[1] == koziri[0]:
                user_move_score.append(70)
            if str1[0] == 'K' and str1[1] != koziri[0]:
                user_move_score.append(8)
            if str1[0] == '1' and str1[1] == koziri[0]:
                user_move_score.append(80)
            if str1[0] == '1' and str1[1] != koziri[0]:
                user_move_score.append(9)
            if str1[0] == 'A' and str1[1] == koziri[0]:
                user_move_score.append(100)
            if str1[0] == 'A' and str1[1] != koziri[0]:
                user_move_score.append(10)             
    # puts score at comp_move_score
def computer_score():
    if computerTurn == False:
        for i in range(len(comp_cards)):
            str1 = comp_cards[i]
            if str1[0] == 'J' and str1[1] == koziri[0]:
                comp_move_score.append(50)
            if str1[0] == 'J' and str1[1] != koziri[0]:
                comp_move_score.append(1)
            if str1[0] == 'Q' and str1[1] == koziri[0]:
                comp_move_score.append(60)
            if str1[0] == 'Q' and str1[1] != koziri[0]:
                comp_move_score.append(2)
            if str1[0] == 'K' and str1[1] == koziri[0]:
                comp_move_score.append(70)
            if str1[0] == 'K' and str1[1] != koziri[0]:
                comp_move_score.append(3)
            if str1[0] == '1' and str1[1] == koziri[0]:
                comp_move_score.append(80)
            if str1[0] == '1' and str1[1] != koziri[0]:
                comp_move_score.append(4)
            if str1[0] == 'A' and str1[1] == koziri[0]:
                comp_move_score.append(100)
            if str1[0] == 'A' and str1[1] != koziri[0]:
                comp_move_score.append(5)
    else:
        for i in range(len(comp_cards)):
            str1 = comp_cards[i]
            if str1[0] == 'J' and str1[1] == koziri[0]:
                comp_move_score.append(50)
            if str1[0] == 'J' and str1[1] != koziri[0]:
                comp_move_score.append(6)
            if str1[0] == 'Q' and str1[1] == koziri[0]:
                comp_move_score.append(60)
            if str1[0] == 'Q' and str1[1] != koziri[0]:
                comp_move_score.append(7)
            if str1[0] == 'K' and str1[1] == koziri[0]:
                comp_move_score.append(70)
            if str1[0] == 'K' and str1[1] != koziri[0]:
                comp_move_score.append(8)
            if str1[0] == '1' and str1[1] == koziri[0]:
                comp_move_score.append(80)
            if str1[0] == '1' and str1[1] != koziri[0]:
                comp_move_score.append(9)
            if str1[0] == 'A' and str1[1] == koziri[0]:
                comp_move_score.append(100)
            if str1[0] == 'A' and str1[1] != koziri[0]:
                comp_move_score.append(10)
              
    #appends list3 with card images based on list4 = user_cards or comp_cards
def get_images(list4,list3):
    
    for i in range(len(list4)):
        if list4[i] == '1Heart':
           list3.insert(i,H10)  
        if list4[i] == '1Spade':
           list3.insert(i,S10)
                
        if list4[i] == '1Diamond':
           list3.insert(i,D10)
                
        if list4[i] == '1Club':
                
           list3.insert(i,C10)
                
        if list4[i] == 'JHeart':
                
           list3.insert(i,JH)
                
        if list4[i] == 'JSpade':
                
           list3.insert(i,JS)
              
        if list4[i] == 'JDiamond':
                
           list3.insert(i,JD)
               
        if list4[i] == 'JClub':
                
           list3.insert(i,JC)
                
        if list4[i] == 'QHeart':
                
           list3.insert(i,QH)
                
        if list4[i] == 'QSpade':
                
           list3.insert(i,QS)
               
        if list4[i] == 'QDiamond':
                
           list3.insert(i,QD)
                
        if list4[i] == 'QClub':
                
           list3.insert(i,QC)
                
        if list4[i] == 'KHeart':
                
           list3.insert(i,KH)
                
        if list4[i] == 'KSpade':
                
           list3.insert(i,KS)
               
        if list4[i] == 'KDiamond':
                
           list3.insert(i,KD)
                
        if list4[i] == 'KClub':
                
            list3.insert(i,KC)
                
        if list4[i] == 'AHeart':
                
           list3.insert(i,AH)
              
        if list4[i] == 'ASpade':
                
           list3.insert(i,AS)
                
        if list4[i] == 'ADiamond':
                
           list3.insert(i,AD)
                
        if list4[i] == 'AClub':
                
           list3.insert(i,AC)
                
    return list3

    
def render_all():
    global Update,comps_miyvas
    get_images(user_cards,img_user)
    get_images(comp_cards,img_comp)
    x_comp = 300
    y_comp = 50
    y_change = 200
    start_x = 300
    start_y = 500
    move_y = 300
    for i in range(len(user_cards)):
        if move_made == False:
            if flags_user[i] == False:
                Screen.blit(img_user[i],(start_x,start_y))
                start_x += 100
            else:
                Screen.blit(img_user[i],(start_x,450))
                start_x += 100
        else:
            if flags_user[i] == False:
                Screen.blit(img_user[i],(start_x,start_y))
                start_x += 100
            else:
                Screen.blit(img_user[i],(start_x,move_y))
                start_x += 100
        if computerTurn == False:        
            if flags_comp[i] == False:
                Screen.blit(Red_Back,(x_comp,y_comp))
                #Screen.blit(img_comp[i],(x_comp,y_comp))
                x_comp += 100
            else:
                if comps_miyvas == True:
                   Screen.blit(img_comp[i],(x_comp,y_change))
                   x_comp += 100
                else:
                    Screen.blit(Red_Back,(x_comp,y_change))
                    x_comp += 100
                Update = True
        else:
            if flags_comp[i] == False:
                Screen.blit(Red_Back,(x_comp,y_comp))
                x_comp += 100
            else:
                
                fps.tick(20)
                Screen.blit(img_comp[i],(x_comp,y_change))
                x_comp += 100
                
                
    pygame.display.update()
    fps.tick(60)
         
            
def total_score():
    Score_ALL_User = font.render(('SCORE:'+ str(total_score_user)), True, ('black'))
    Score_ALL_Comp = font.render(('SCORE:'+ str(total_score_comp)), True, ('black'))
    Screen.blit(Score_ALL_User,(1000,60))
    Screen.blit(Score_ALL_Comp,(1000,700))
    
        
def user_moved():
    global computerTurn,Update,comps_miyvas,user_bura_flag,user_maliutka_flag,koziri,comp_bura_flag,comp_maliutka_flag,game_over_flag,comp_won
    num_of_cards_played = 0
    get_suits(comp_cards,comp_suits)
    get_suits(user_cards,user_suits)
    computer_score()
    user_score()
    
    if move_made == True and computerTurn == False:
        for i in reversed(range(len(user_cards))):
            if (min(comp_move_score) == comp_move_score[i]):
                min_value_index = i
            if comp_suits[i] == user_suits[i]:
                comp_move_score[i] = comp_move_score[i] + 5
            if flags_user[i] == False:
                user_move_score.pop(i)
                user_suits.pop(i)
            else:
                num_of_cards_played += 1
            
        if len(comp_cards) == 3:
                if comp_suits[0] == comp_suits[1] and comp_suits[0] == comp_suits[2]:
                    if comp_suits[0] == koziri[0]:
                        print("Comp yavs bura")
                        comp_bura_flag = True
                    else:
                        print("KOmps yavs maliutka")
                        comp_maliutka_flag = True
           # tu erti karti chamovida
        if num_of_cards_played == 1 and comp_bura_flag == False and comp_maliutka_flag == False:
           for i in range(len(comp_cards)):
               if comp_move_score[i] > user_move_score[0]:
                   flags_comp[i] = True
                   comps_miyvas = True
                   break
           if comps_miyvas == False:           
               flags_comp[min_value_index] = True
               
            # tu ori karti chamovida
        elif num_of_cards_played == 2 and comp_bura_flag == False and comp_maliutka_flag == False:
            if len(comp_cards) >= 2:
                print("Comp_move_score:",comp_move_score)
                print("User_move_score:",user_move_score)
                print(comp_move_score[0],user_move_score[0])
                if comp_move_score[0] > user_move_score[0] and comp_move_score[1] > user_move_score[1] or comp_move_score[0] > user_move_score[1] and comp_move_score[1] > user_move_score[0]:
                    flags_comp[0] = True
                    flags_comp[1] = True
                    comps_miyvas = True
                elif comp_move_score[0] > user_move_score[0] and comp_move_score[2] > user_move_score[1] or comp_move_score[0] > user_move_score[1] and comp_move_score[2] > user_move_score[0]:
                    flags_comp[0] = True
                    flags_comp[2] = True
                    comps_miyvas = True
                elif comp_move_score[1] > user_move_score[0] and comp_move_score[2] > user_move_score[1] or comp_move_score[1] > user_move_score[1] and comp_move_score[2] > user_move_score[0]:
                    flags_comp[1] = True
                    flags_comp[2] = True
                    comps_miyvas = True
                else:
                    for i in range(len(comp_cards)):
                        if comp_suits[i] == user_suits[0]:
                            comp_move_score[i] = comp_move_score[i] - 5
                    if max(comp_move_score) == comp_move_score[0]:
                       flags_comp[1] = True
                       flags_comp[2] = True
                       
                    elif max(comp_move_score) == comp_move_score[1]:
                        flags_comp[0] = True
                        flags_comp[2] = True
                        
                    else:
                        flags_comp[0] = True
                        flags_comp[1] = True
         #tu sami karti chamovida 
        elif(num_of_cards_played > 2):
            if comp_maliutka_flag == True:
                comp_maliutka_flag = False
            if comp_bura_flag == True:
                comp_bura_flag = False
            flags_comp[0] = True
            flags_comp[1] = True
            flags_comp[2] = True
            user_move_score.sort()
            comp_move_score.sort()
        
            # tu bura yavs players
            if user_suits[0] == koziri[0]:
                user_bura_flag = True
            #tu maliutka yavs players
            else:
                if comp_move_score[0] > user_move_score[0] and comp_move_score[1] > user_move_score[1] and comp_move_score[2] > user_move_score[2]:
                    comps_miyvas = True
        
        if comp_maliutka_flag == True or comp_bura_flag == True:
            comps_miyvas = True
            Update = True
                
    if move_made == True and computerTurn == True:
        #dasaweria
        if comp_bura_flag == True:
            game_over_flag = True
            comp_won = True
            for i in range(len(user_cards)):
                cards_taken_comp.append(user_cards[i])
                cards_taken_comp.append(comp_cards[i])
        elif comp_maliutka_flag == True:
            comp_move_score.clear()
            user_move_score.clear()
            user_score()
            computer_score()
            print("maliutka comp move_score:",comp_move_score)
            print("maliutka user move_score:",user_move_score)
            if comp_move_score[0] < user_move_score[0] and comp_move_score[1] < user_move_score[1] and comp_move_score[2] < user_move_score[2]:
                    comps_miyvas = False
                    Update = True
            else:
                comps_miyvas = True
                comp_maliutka_flag = False
                Update = True
        else:
            counter2 = 0
            #prosta Flagi gadaeci Render_ALL updateitdeba
            for i in reversed(range(len(user_cards))):
                if flags_user[i] == False:
                    user_move_score.pop(i)
                    user_suits.pop(i)
                if flags_comp[i] == False:
                    comp_move_score.pop(i)
                    comp_suits.pop(i)
            for i in reversed(range(len(user_move_score))):
                if user_suits[i] == comp_suits[i] and user_suits[i] != koziri[0]:
                    user_move_score[i] += 5
                counter2+= 1
                
            if counter2 == 1:
                if user_move_score[0] < comp_move_score[0]:
                    comps_miyvas = True
                    Update = True
                else:
                    Update = True
            elif counter2 == 2:
                user_move_score.sort()
                comp_move_score.sort()
                if user_move_score[0] > comp_move_score[0] and user_move_score[1] > comp_move_score[1]:
                    Update = True
                else:
                    comps_miyvas = True
                    Update = True
    
def cards_into_score(list4,counter):
    
    for i in range(len(list4)):
        if list4[i] == '1Heart' or list4[i] == '1Spade' or list4[i] == '1Diamond' or list4[i] == '1Club':
           counter += 10 
        if list4[i] == 'JHeart' or list4[i] == 'JSpade' or list4[i] == 'JDiamond' or list4[i] == 'JClub':
           counter += 2
                
        if list4[i] == 'QHeart' or list4[i] == 'QDiamond' or list4[i] == 'QClub' or list4[i] == 'QSpade':
           counter += 3
                
        if  list4[i] == 'KHeart' or list4[i] == 'KDiamond' or list4[i] == 'KClub' or list4[i] == 'KSpade':
                
           counter += 4
                
        if  list4[i] == 'AHeart' or list4[i] == 'ADiamond' or list4[i] == 'AClub' or list4[i] == 'ASpade':
                
           counter += 11
               
            
    return counter

def computer_turn():
    #dasaweriaaaaaaaaaaaaaa
    global flags_comp
    if comp_bura_flag == True or comp_maliutka_flag == True:
        flags_comp = [True,True,True]
    else:
        get_suits(comp_cards,comp_suits)
        if len(comp_suits) == 3:
            if comp_suits[0] == comp_suits[1]:
                flags_comp[0] = True
                flags_comp[1] = True
            elif comp_suits[0] == comp_suits[2]:
                flags_comp[0] = True
                flags_comp[2] = True
            elif comp_suits[1] == comp_suits[2]:
                flags_comp[1] = True
                flags_comp[2] = True
            else:
                flags_comp[1] = True
        else:
            flags_comp[0]
def win_render(list1,list2):
    global new_game_flag,total_score_comp,winner_user,winner_comp
    x = 200
    y = 300 
    text4 = font.render(('TOTAL SCORE:'+ str(comp_score_counter)), True, ('black'))
    text5 = font.render(('TOTAL SCORE:'+ str(user_score_counter)), True, ('black'))
    win_img = get_images(list1,list2)
   
    
    
    if comp_won == True:
        winner_comp = True
        for i in range(len(list1)):
            if comp_bura_flag == False:
                Screen.blit(win_img[i],(x,y))
                x += 100
                Screen.blit(text,(400,500))
                Screen.blit(text4,(400,200))
            else:
                Screen.blit(win_img[i],(x,y))
                x += 100
                Screen.blit(text,(400,500))
                Screen.blit(text1,(450,200))
            
    if user_won == True:
        if len(list1) != 0:
            for i in range(len(list1)):
                Screen.blit(win_img[i],(x,y))
                x += 100
                if user_score_counter > 30:
                    winner_comp = False
                    Screen.blit(text2,(450,500))
                    Screen.blit(text5,(400,200))
                else:
                    winner_comp = True
                    Screen.blit(text,(450,500))
                    Screen.blit(text5,(400,200))
        else:
            Screen.blit(text,(450,500))
            Screen.blit(text5,(400,200))
            winner_comp = True
    
    
def Update_Game():
    global move_made,computerTurn,flags_user,flags_comp,comps_miyvas,comp_score_counter,user_score_counter
    if comps_miyvas == True and comp_bura_flag == True or comps_miyvas == True and comp_maliutka_flag == True:
        computerTurn = True
        comps_miyvas = False
        return
    for i in reversed(range(len(user_cards))):
        if flags_comp[i] == True:
            if comps_miyvas == True:
                cards_taken_comp.append(comp_cards[i])
            else:
                cards_taken_user.append(comp_cards[i])
            comp_cards.pop(i)
        if flags_user[i] == True:
            if comps_miyvas == True:
                cards_taken_comp.append(user_cards[i])
            else:
                cards_taken_user.append(user_cards[i])
            user_cards.pop(i)
        
    Update_cards(user_cards,comp_cards)
    user_suits.clear()
    comp_suits.clear()
    comp_move_score.clear()
    user_move_score.clear()
    flags_comp = [False,False,False]
    flags_user = [False,False,False]
    move_made = False
    if comps_miyvas == True:
        computerTurn = True
        comps_miyvas = False
    else:
        computerTurn = False
    comp_score_counter = cards_into_score(cards_taken_comp,0)
    user_score_counter= cards_into_score(cards_taken_user,0)
    
def new_game():
    global koziri,Deck,game_over_flag,flags_comp,flags_user,user_score_counter,comp_score_counter,total_score_comp,total_score_user
    if winner_comp == True:
        total_score_comp += 1
    else:
        total_score_user += 1    
    
    user_cards.clear()
    comp_cards.clear()
    comp_move_score.clear()
    user_move_score.clear()
    img_comp.clear()
    img_user.clear()
    flags_user.clear()
    flags_comp.clear()
    Deck.clear()
    cards.get_deck()
    cards.get_shuffle()
    Deck = cards.cardDeck
    koziri = kozir()
    user_score_counter = 0
    comp_score_counter = 0
    Update_cards(user_cards,comp_cards)
    print("new game Deck",len(Deck))
    print("new game User_cards:",user_cards)
    print("new game Comp_cards:",comp_cards)
    print("Koziri:",koziri)
    print("flags_user:",flags_user)
    print("Comp_flags:",flags_comp)
    print("user_move_score:",user_move_score)
    print("comp_move_score:",comp_move_score)
    game_over_flag = False
    flags_user = [False,False,False]
    flags_comp = [False,False,False]
      



Update_cards(user_cards,comp_cards)
#koziri = kozir()
koziri = kozir()
#comp_cards = ['ASpade','ADiamond','KSpade']
#user_cards = ['KDiamond','JDiamond','QDiamond']
#for i in range(3):
#    Deck.remove(user_cards[i])
#    Deck.remove(comp_cards[i])



print("Initial_user:",user_cards)
print("Initial_comp:",comp_cards)
print("Koziri:",koziri)
print("Deck:",len(Deck))

python = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
           if event.button == 1:
               #var button
               print("Position",mouse)
               if 523 <= mouse[0] <= 615 and 677 <= mouse[1] <= 738:
                    user_won = True
                    game_over_flag = True
                      
                #move button      
               if 400 <= mouse[0] <= 492 and 678 <= mouse[1] <= 740:
                   if check_move() and computerTurn == False:
                        move_made = True
                        python = True
                   elif check_move_after_comp_move() and computerTurn == True:
                        move_made = True
                        python = True
                   else:
                        flags_user = [False,False,False]
                   
                    
               if 318 <= mouse[0] <= 395 and 510 <= mouse[1] <= 639:
                        if flags_user[0] == False:
                            flags_user[0] = True
                           
                        else:
                            flags_user[0] = False
                            
               if 410 <= mouse[0] <= 491 and 514 <= mouse[1] <= 638:
                        if flags_user[1] == False:
                            flags_user[1] = True
                            
                        else:
                            flags_user[1] = False
                            
               if 512 <= mouse[0] <= 639 and 510 <= mouse[1] <= 636:
                        if flags_user[2] == False:
                            flags_user[2] = True
                        else:
                            flags_user[2] = False           
               if 482 <= mouse[0] <= 571 and 575 <= mouse[1] <= 691:
                   if game_over_flag == True:
                       print("New_Game Button Pressed")
                       new_game()
    Screen.blit(Surface,(0,0))
    mouse = pygame.mouse.get_pos()
    Screen.blit(card_Deck,(0,250))      
    total_score()
    if game_over_flag == True:
        Screen.blit(button2,(480,550))
        Screen.blit(text_new_game,(480,590))
    if game_over_flag == False:
        Screen.blit(button2,(400,660))
        Screen.blit(button2,(520,660))
        Screen.blit(text_move,(409,695))
        Screen.blit(text_var,(540,695))
    kozir_render()
    if game_over_flag == False:
        render_all()
        if comp_score_counter > 30:
            comp_won = True
            game_over_flag = True
        
        
    if python == True:
        
        user_moved()
        
        python = False   

    

    if game_over_flag == True:
       if user_won == True:
           win_render(cards_taken_user,img_taken_comp)
           
       if comp_won == True:
           win_render(cards_taken_comp,img_taken_comp)     
    if Update == True and game_over_flag == False:
        pygame.time.delay(450)
        Update_Game()
        Update = False
    if computerTurn == True and game_over_flag == False:
        computer_turn()
    
    pygame.display.update()
    fps.tick(60)
   
        