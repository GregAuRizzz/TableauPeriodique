#Importation des bibliothèques :
import pygame
from pygame.locals import *
from data import *

#Initialisation de pygame :
pygame.init()
pygame.display.set_caption("Grégory Projet Tableau Périodique")
surface = pygame.display.set_mode((1050,625))
horloge = pygame.time.Clock()

#Définition de la Police d'écriture pour plusieurs éléments:
font_element = pygame.font.SysFont('Arial', 20)
font_titre = pygame.font.SysFont('"Volter.ttf"', 40)
font_config = pygame.font.SysFont('Arial', 20)
font_legende = pygame.font.SysFont('Arial', 10)
font_masse = pygame.font.SysFont('Arial', 10)
font_nomcomplet = pygame.font.SysFont('Volter.ttf', 14)

#Chargement de la musique de fond :
pygame.mixer.init()
pygame.mixer.music.load("Musique_De_Fond.mp3")
pygame.mixer.music.play(loops=-1)

#Couleur de fond :
surface.fill((185,248,248))

# Création des légendes des groupes chimiques :
liste_couleur = [(176,224,230),(187,210,225),(176,196,222),(173,216,230),(135,206,250),(135,206,235),(128,208,208),(95,158,160),(0,191,255),(119,181,254),(100,149,237)]
liste_legende = [[10,570,80,20],[10,540,80,20],[10,510,80,20],[10,480,80,20],[10,450,80,20],[100,570,80,20],[100,540,80,20],[100,510,80,20],[100,480,80,20],[100,450,80,20],[190,440,80,20]]
liste_groupe = ["Diatomic nonmetal","Noble gas","Alkaline earth metal","Polyatomic nonmetal","Metalloid","Alkali metal","Transition metal","Poor metal","Transition metal","Lanthanide","Actinide"]
for i in range(len(liste_couleur)):
    leg = pygame.draw.rect(surface,liste_couleur[i],liste_legende[i])
    texte = font_legende.render(liste_groupe[i],1,(255,0,0))
    surface.blit(texte,leg)

#Ecriture du titre de mon tableau périodique
titre = 0
titre = font_titre.render("Tableau périodique TP Chimie Grégory",1,(0,0,0))
surface.blit(titre, (300, 25))

# Variable utile
data = 0
w =1272
c = 53

#Les différents groupes de métaux :
def Groupes(x):
    for i in range(len(liste_groupe)):
        if data1[x][5] == liste_groupe[i]:
            return liste_couleur[i]
    return (230,230,250)

# écriture des éléments chimiques :
def texte(x,rect):
    if data1[x][0] == "La-Lu" or data1[x][0] == "Ac-Lr":
        texte = font_element.render(" "+str(data1[x][0]),1,(255,0,0))
        surface.blit(texte,rect)
    else:
        texte = font_element.render("   "+str(data1[x][0]),1,(255,0,0))
        surface.blit(texte,rect)
#écriture 
def masse_atomique(x,y,i):
    titre = font_masse.render(data1[i][2],1,(0,0,0))
    surface.blit(titre,(x, y))
#Nom Complet Cliquer
def nom_element(i):
    titre = font_nomcomplet.render(data1[i][1],1,(0,0,0))
    surface.blit(titre, (370, 85))

#Ecriture config
def config(i):
    pygame.draw.rect(surface,(185,248,248),[353,70,200,90])
    config = font_config.render(str(data1[i][6]),1,(0,0,0))
    surface.blit(config,(370,100))
    config = font_masse.render(str(data1[i][2]),1,(0,0,0))
    surface.blit(config,(370,140))

#Boucle savoir un élément chimique
def savoir_element(i):    
    config(i)
    rectangle = pygame.draw.rect(surface,Groupes(i),[300,100,53,53],border_radius =3)
    texte(i,rectangle)
    nom_element(i)

def Savoir_Quelle_Element(rectangle1,mouse):
    if rectangle1 == True:
        if mouse[1] < 106 and mouse[0] < 83:
            i = 0
            savoir_element(i)
        elif mouse[1] < 106 and mouse[0] > 931:
            i = 1
            savoir_element(i)
        elif mouse[1] < 159 and mouse[0] < 136:
            i = ((mouse[0]-30)//53) + 2
            i+= 2
            savoir_element(i)
        elif mouse[1] < 159 and mouse[0] > 666:
            i = ((mouse[0]-30)//53 - 10)
            i += 2
            savoir_element(i)
        elif mouse[1] < 212 and mouse[0] < 136:
            i = ((mouse[0]-30)//53) + 10
            i += 10
            savoir_element(i)
        elif mouse[1] < 212 and mouse[0] > 666:
            i = ((mouse[0]-30)//53)
            savoir_element(i)
        elif mouse[1] > 212 and mouse[1] < 265:
            i = (mouse[0]-30)//53 + 18
            savoir_element(i)
        elif mouse[1] > 265 and mouse[1] < 318:
            i = ((mouse[0]-30)//53) + 36
            savoir_element(i)
        elif mouse[1] > 318 and mouse[1] < 371:
            i = ((mouse[0]-30)//53) + 54
            savoir_element(i)
        elif mouse[1] > 371 and mouse[1] < 424 and mouse[0] < 666:
            i = ((mouse[0]-30)//53) + 72
            savoir_element(i)
    else:
        if mouse[1] > 477 and mouse[1] < 530 and mouse[0] > 189:
            i = ((mouse[0]-30)//53 - 3) + 84
            savoir_element(i)
        if mouse[1] > 530 and mouse[1] < 583 and mouse[0] > 189:
            i = ((mouse[0]-30)//53 - 3) + 99
            savoir_element(i)

#Création des cases :
def aide_creation_case(i,j):
    global data,a
    rectangle = pygame.draw.rect(surface,Groupes(data),[(i*c)+30,j*c, c, c],0,border_radius =3)
    x = i*c + 30
    y = j*c + 40
    masse_atomique(x,y,a)
    texte(data,rectangle)
    a += 1
    data += 1
a = 0
for j in range (0,13):
    for i in range(0,18):
            if data > 113:
                break
            if j == 1 and (i <1 or i >16 ) :
                aide_creation_case(i,j)
            elif j == 2 and (i<2 or i >11):
                aide_creation_case(i,j)
            elif j == 3 and (i<2 or i >11):
                aide_creation_case(i,j)
            elif (j>3 and j<7):
                aide_creation_case(i,j)
            elif j == 7 and i < 12:
                aide_creation_case(i,j)
            elif j == 9 and (i>2):
                aide_creation_case(i,j)
            elif j == 10 and (i>2):
                aide_creation_case(i,j)

# Cliquer et afficher les infos en continue
run = True
while run:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif pygame.mouse.get_pressed()[0]:
            detection = pygame.draw.rect(surface,(185,248,248),[30,53,954,371],1)
            if pygame.Rect.collidepoint(detection,mouse):
                rectangle1 = True
                Savoir_Quelle_Element(rectangle1,mouse)
                
            #Si le Deuxième bloc d'éléments est cliqué:
            detection = pygame.draw.rect(surface,(185,248,248),[189,477,795,106],1)
            if pygame.Rect.collidepoint(detection,mouse):
                rectangle1 = False
                Savoir_Quelle_Element(rectangle1,mouse)
        pygame.display.update()

pygame.quit()