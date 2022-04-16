
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
    def __init__(self,rank,suits,value,power,img,clicked,y_coordinate):
        self.card_rank = rank
        self.card_suit = suits
        self.card_value = value
        self.card_power = power
        self.card_image = img
        self.clicked = clicked
        self.card_y = y_coordinate
    
A_D = Card('A','D',11,5,AD,False,500)
K_D = Card('K','D',4,3,KD,False,500)
Q_D = Card('Q','D',3,2,QD,False,500)
J_D = Card('J','D',2,1,JD,False,500)
D_1 = Card('1','D',10,4,D10,False,500)

A_H = Card('A','H',11,5,AH,False,500)
K_H = Card('K','H',4,3,KH,False,500)
Q_H = Card('Q','H',3,2,QH,False,500)
J_H = Card('J','H',2,1,JH,False,500)
H_1 = Card('1','H',10,4,H10,False,500)

A_S = Card('A','S',11,5,AS,False,500)
K_S = Card('K','S',4,3,KS,False,500)
Q_S = Card('Q','S',3,2,QS,False,500)
J_S = Card('J','S',2,1,JS,False,500)
S_1 = Card('1','S',10,4,S10,False,500)

A_C = Card('A','C',11,5,AC,False,500)
K_C = Card('K','C',4,3,KC,False,500)
Q_C = Card('Q','C',3,2,QC,False,500)
J_C = Card('J','C',2,1,JC,False,500)
C_1 = Card('1','C',10,4,C10,False,500)    

Red_Back = pygame.image.load('red_back.png')
Red_Back = pygame.transform.scale(Red_Back,(150,150))
card_Deck1 = pygame.image.load('Deck.png')
card_Deck1 = pygame.transform.scale(card_Deck1,(200,200))
button1 = pygame.image.load('PNG\\button1.PNG')
button1 = pygame.transform.scale(button1,(100,100))
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
text = font.render('YOU LOST', True, ('black'))

user_cards = []
comp_cards = []
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
shuffle()
koziri = kozir()
Update_cards(user_cards,comp_cards)

def user_cards_render(list,x_coordinate):
    for i in range(len(list)):   
        Screen.blit(list[i].card_image,(x_coordinate,list[i].card_y))
        x_coordinate += 100


def comp_cards_render(list,x_coordinate):
    for i in range(len(list)):
        Screen.blit(Red_Back,(x_coordinate,50))
        x_coordinate += 100
Surface = pygame.Surface((1200,800))
Surface.fill((175,215,70))

   
                
                
                
            
                
                
            

                 









        



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
           if event.button == 1:
               if 523 <= mouse[0] <= 615 and 677 <= mouse[1] <= 738:
                   print("clicked at 523")
                      
                     
               if 400 <= mouse[0] <= 492 and 678 <= mouse[1] <= 740:  
                   print("Clicked at 400")
                  
               if 318 <= mouse[0] <= 395 and 510 <= mouse[1] <= 639:
                       if user_cards[0].card_y == 500:
                           user_cards[0].card_y = 450
                       else:
                           user_cards[0].card_y = 500
                            
               if 410 <= mouse[0] <= 491 and 514 <= mouse[1] <= 638:
                         if user_cards[1].card_y == 500:
                           user_cards[1].card_y = 450
                         else:
                           user_cards[1].card_y = 500
                            
               if 512 <= mouse[0] <= 639 and 510 <= mouse[1] <= 636:
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
    user_cards_render(user_cards,300)
    comp_cards_render(comp_cards,300)
   
    pygame.display.update()
    fps.tick(60)
