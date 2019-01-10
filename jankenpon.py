from random import randrange
import serial
import time
import tkinter as tk

feuille = 0
cailloux = 0
ciseau = 0

feuilleb =0
caillouxb = 0
ciseaub = 0
BOT = 0

pointJ = 0
pointB = 0

def choix(count) :
    global pointJ,pointB

    cpt = 0
    down1 = 3
    down2 = 3
    down3 = 3
    down4 = 3
    down5 = 3
    doigt1 = 0
    doigt2 = 0
    doigt3 = 0
    doigt4 = 0
    doigt5 = 0
    while cpt < 30:
        cpt+=1
        res = str(arduino.readline())
        print(res)
        if ("1" in res):
            down1+=1
        if ("11" in res):
            down1 = 0
        if ("2" in res):
            down2+=1
        if ("12" in res):
            down2 = 0
        if ("3" in res):
            down3+=1
        if ("13" in res):
            down3 = 0
        if ("4" in res):
            down4+=1
        if ("14" in res):
            down4 = 0
        if ("5" in res):
            down5+=1
        if ("15" in res):
            down5 = 0
        if (down1 < 3 and doigt1 == 0):
            doigt1 = 1
        elif (down1 >= 3 and doigt1 == 1):
            doigt1 = 0
        if (down2 < 3 and doigt2 == 0):
            doigt2 = 1
        elif (down2 >= 3 and doigt2 == 1):
            doigt2 = 0
        if (down3 < 3 and doigt3 == 0):
            doigt3 = 1
        elif (down3 >= 3 and doigt3 == 1):
            doigt3 = 0
        if (down4 < 3 and doigt4 == 0):
            doigt4 = 1
        elif (down4 >= 3 and doigt4 == 1):
            doigt4 = 0
        if (down5 < 3 and doigt5 == 0):
            doigt5 = 1
        elif (down5 >= 3 and doigt5 == 1):
            doigt5 = 0
        time.sleep(0.02)

    count.after(1000, lambda: count.config(text='3'))
    count.pack()
    count.after(2000, lambda: count.config(text='2'))
    count.pack()
    count.after(3000, lambda: count.config(text='1'))
    count.pack()
    print(doigt1, doigt2, doigt3, doigt4, doigt5)
    count.after(4000, lambda: count.config(text=''))
    count.pack()
    BOT = randrange(1,4)
    if BOT == 1 :
        feuilleb = 1
    elif BOT == 2 :
        caillouxb = 1
    else:
        ciseaub = 1

    if doigt2 == 0 and doigt4 == 0 or doigt2 == 1 and doigt4 == 0 :
         print("dedans")
         if BOT == 1 :
            chaine.after(4000, lambda: chaine.config(text='Vous avez choisi: Feuille.\nLe BOT a choisi: Feuille.\nEgalité.\n'))
         elif BOT == 2 :
            chaine.after(4000, lambda: chaine.config(text='Vous avez choisi: Feuille.\nLe BOT a choisi: Pierre.\nVous gagnez.\n'))
            pointJ += 1
         else:
            chaine.after(4000, lambda: chaine.config(text='Vous avez choisi: Feuille.\nLe BOT a choisi: Ciseau.\nVous perdez.\n'))
            pointB += 1

    elif doigt2 == 1 and doigt4 == 1 :
        if BOT == 2 :
            chaine.after(4000, lambda: chaine.config(text='Vous avez choisi: Pierre.\nLe BOT a choisi: Pierre.\nEgalité.\n'))
        elif BOT ==1 :
            chaine.after(4000, lambda: chaine.config(text='Vous avez choisi: Pierre.\nLe BOT a choisi: Feuille.\nVous perdez.\n'))
            pointB += 1
        else:
            chaine.after(4000, lambda: chaine.config(text='Vous avez choisi: Pierre.\nLe BOT a choisi: Ciseau.\nVous gagnez.\n'))
            pointJ += 1

    elif doigt2 == 0 and doigt4 == 1 :
        if BOT == 3 :
            chaine.after(4000, lambda: chaine.config(text='Vous avez choisi: Ciseau.\nLe BOT a choisi: Ciseau.\nEgalité.\n'))
        elif BOT == 2 :
            chaine.after(4000, lambda: chaine.config(text='Vous avez choisi: Ciseau.\nLe BOT a choisi: Pierre.\nVous gagnez.\n'))
            pointJ += 1
        else:
            chaine.after(4000, lambda: chaine.config(text='Vous avez choisi: Ciseau.\nLe BOT a choisi: Feuille.\nVous perdez.\n'))
            pointB += 1
    score.after(4000, lambda: score.config(text='Votre score : {0}.\nScore du BOT : {1}.\n'.format(pointJ,pointB)))


    
try:
    arduino = serial.Serial("COM3", timeout=1)
except:
    print("Please check the port")
pointJ,pointB=0,0
fenetre = tk.Tk()
texte1 = tk.Label(fenetre, text='Bienvenue au Jankenpon SHAND !\n\n\nPour jouer:\n\n1) Sélectionner le bouton GO pour lancer la partie.\n2) Réaliser pierre/feuille/ciseau avec votre gant avant le compte à rebours.\n')
texte1.pack()
count = tk.Label(fenetre)
count.pack()
bouton1 = tk.Button(fenetre, text="GO", command = (lambda: choix(count)))
bouton1.pack()
chaine = tk.Label(fenetre)
chaine.pack()
score = tk.Label(fenetre,text='Votre score : {0}.\nScore du BOT : {1}.\n'.format(pointJ,pointB))
score.pack()
fenetre.mainloop()