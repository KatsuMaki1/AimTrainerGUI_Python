#Katsu, le 21/11/2024 en Python 3.7
from tkinter import *
from tkinter import ttk
import webbrowser #permet d'ouvrir une url ou un fichier dans l'ordinateur
import os #permet de trouver des fichiers dans l'ordinateur
import pygame #permet de demarrer du son
##------------VOLUME SLIDER------------##
def set_volume(value):
    """Set the volume based on slider value (range from 0 to 1)."""
    volume = float(value) / 100  # Scale slider (0-100) to pygame's (0.0-1.0) range
    pygame.mixer.music.set_volume(volume)

##----------Fenetre Info--------##
def create():
    global info
    global Bouton_Maison
    global Bouton_Yuxe
    global Bouton_Katsu
    info = Label(gui, text='Développeurs:', font='Impact 40')
    info.place(x=460,y=120)
    Bouton_Katsu = Button(gui,text="Evan", command=kat, font='Impact 40')
    Bouton_Katsu.place(x=470,y=200)
    Bouton_Yuxe = Button(gui,text="Youri",command=yuxe, font='Impact 40')
    Bouton_Yuxe.place(x=620,y=200)
    Bouton_Jouer.place_forget()
    Bouton_Setting.place_forget()
    Bouton_Database.place_forget()
    Bouton_Info.place_forget()
    Bouton_Close.place_forget()
    titre.place_forget()
    Bouton_Maison = Button(gui,text="Retourner au menu principal", command=back, font='Impact 40')
    Bouton_Maison.place(x=300,y=360)
    pygame.mixer.init()
    pygame.mixer.music.load("info.mp3") #Loading File Into Mixer
    pygame.mixer.music.play()

def kat():
    webbrowser.open_new(r"https://github.com/KatsuMaki1")

def yuxe():
    webbrowser.open_new(r"https://www.youtube.com/@YUXE_")
#FONCTION CREATE: fonction qui va cacher temporairement les boutons du menu principal et affiche le nom des dévéloppeurs ainsi qu'un bouton permettant de revenir au menu principal
##-------------RETOUR ARRIERE--------##

def back():
    pygame.mixer.music.stop()
    Bouton_Maison.place_forget()
    info.place_forget()
    Bouton_Katsu.place_forget()
    Bouton_Yuxe.place_forget()
    Bouton_Jouer.place(x=50,y=120)
    Bouton_Setting.place(x=50,y=462)
    Bouton_Database.place(x=50,y=234)
    Bouton_Info.place(x=50,y=348)
    Bouton_Close.place(x=50,y=576)
    titre.place(x=15,y=12)
    pygame.mixer.init()
    pygame.mixer.music.load("menu.mp3") #Loading File Into Mixer
    pygame.mixer.music.play()

#FONCTION BACK: fonction qui va cacher le menu avec les info developpeurs pour reafficher le menu principal

##--------------------RETOUR------------------##
def bye():
    pygame.mixer.music.stop()
    Bouton_Retour.place_forget()
    score.place_forget()
    Bouton_Jouer.place(x=50,y=120)
    Bouton_Setting.place(x=50,y=462)
    Bouton_Database.place(x=50,y=234)
    Bouton_Info.place(x=50,y=348)
    Bouton_Close.place(x=50,y=576)
    titre.place(x=15,y=12)
    pygame.mixer.init()
    pygame.mixer.music.load("menu.mp3") #Loading File Into Mixer
    pygame.mixer.music.play()
##----------Fenetre Parametres---------##
def set():
    global Bouton_Appliquer
    global Bouton_Blanc
    global Bouton_Gris
    global texte_fond
    global texte_vol
    global slider
    global Bouton_Cheat
    Bouton_Jouer.place_forget()
    Bouton_Setting.place_forget()
    Bouton_Database.place_forget()
    Bouton_Info.place_forget()
    Bouton_Close.place_forget()
    titre.place_forget()
    Bouton_Appliquer = Button(gui, text="Appliquer", command=show, font='Impact 40', width=12, height=1)
    Bouton_Appliquer.place(x=460, y=600)

    ##----- Creation d'une saisie avec Entry -----##
    pygame.mixer.init()
    pygame.mixer.music.load("option.mp3") #Loading File Into Mixer
    pygame.mixer.music.play()
    texte_fond = Label(gui, text="Choisissez la couleur du fond:",  font='Impact 40')
    texte_fond.place(x=300,y=380)
    Bouton_Blanc = Button(gui, text="Fond Blanc", command=white,  font='Impact 40', width=12, height=1)
    Bouton_Blanc.place(x=230,y=460)
    Bouton_Gris = Button(gui, text="Fond Gris", command=grey,  font='Impact 40', width=12, height=1)
    Bouton_Gris.place(x=698,y=460)
    Bouton_Cheat = Button(gui,text="Secret", command=troll, font='Impact 9')
    Bouton_Cheat.place(x=0,y=0)
    texte_vol = Label(gui, text="Baissez ou Montez le son" , font='Impact 40')
    slider = Scale(gui,from_=0,to=100,orient='horizontal',command=set_volume,font='Impact 40')
    texte_vol.place(x=41,y=100)
    slider.place(x=592,y=100)

def white():
    gui.config(bg="white")
    Bouton_Blanc.config(bg="black", fg="white")

def grey():
    gui.config(bg="grey")
    Bouton_Gris.config(bg="white", fg="black")

def troll():
     webbrowser.open_new(r"https://youtu.be/FtutLA63Cp8?si=YE5HyyEnrz5ZsLYV")
##---------------def retour des boutons----------##
def show():
    pygame.mixer.music.stop()
    Bouton_Appliquer.place_forget()
    Bouton_Gris.place_forget()
    Bouton_Blanc.place_forget()
    texte_fond.place_forget()
    slider.place_forget()
    Bouton_Cheat.place_forget()
    texte_vol.place_forget()
    Bouton_Jouer.place(x=50,y=120)
    Bouton_Setting.place(x=50,y=462)
    Bouton_Database.place(x=50,y=234)
    Bouton_Info.place(x=50,y=348)
    Bouton_Close.place(x=50,y=576)
    titre.place(x=15,y=12)
    pygame.mixer.init()
    pygame.mixer.music.load("menu.mp3") #Loading File Into Mixer
    pygame.mixer.music.play()

##--------------Musique Menu---------------##
def leave():
    pygame.mixer.music.stop()
    gui.destroy()


##----------------LEADERBOARD------------##
def lead():
    global score
    global Bouton_Retour
    score = Label(gui, text='Voici la liste des scores:', font='Impact 40')
    score.place(x=360,y=10)
    Bouton_Jouer.place_forget()
    Bouton_Setting.place_forget()
    Bouton_Database.place_forget()
    Bouton_Info.place_forget()
    Bouton_Close.place_forget()
    titre.place_forget()
    Bouton_Retour = Button(gui,text="Retourner au menu principal", command=bye, font='Impact 40')
    Bouton_Retour.place(x=300,y=600)
    pygame.mixer.init()
    pygame.mixer.music.load("info.mp3") #Loading File Into Mixer
    pygame.mixer.music.play()
##----------------------GUI TKINTER--------------##
gui = Tk()
gui.title("AimTrainer")
gui.geometry('1280x720')
gui.configure(bg='#808080')
pygame.mixer.init()
pygame.mixer.music.load("menu.mp3") #Loading File Into Mixer
pygame.mixer.music.play()
titre = Label(gui, text="Merci d'avoir téléchargé notre jeu", font='Impact 40')
titre.place(x=15,y=12)

##------------BOUTON PLAY---------##
Label(gui, text='Play')

Bouton_Jouer = Button(gui,text="Jouer",command=gui.destroy, font='Impact 40', width=12, height=1)

##------------BOUTON LEADERBOARD-------------##
Label(gui, text='Leaderboard')

Bouton_Database = Button(gui,text="Scores", command=lead, font='Impact 40', width=12, height=1)


##----------BOUTON INFO--------#
Label(gui, text='Info')

Bouton_Info = Button(gui,text="Crédits", command =create, font='Impact 40', width=12, height=1)


##-------------BOUTON PARAMETRE------------##
Label(gui, text='Parametre')

Bouton_Setting = Button(gui,text="Paramètres", command=set, font='Impact 40', width=12, height=1)

##-----------BOUTON QUITTER---------------##
Label(gui, text='Close')

Bouton_Close = Button(gui,text="Quitter le jeu", command=leave, font='Impact 40', width=12, height=1)


##
##----------- GRILLE --------##
Bouton_Jouer.place(x=50,y=120)
Bouton_Database.place(x=50,y=234)
Bouton_Info.place(x=50,y=348)
Bouton_Setting.place(x=50,y=462)
Bouton_Close.place(x=50,y=576)


gui.mainloop()
