import time as t
import pygame   

pygame.mixer.init()

sounds = ['alarme.mp3', 'digicode.mp3', 'bip.mp3']

def load_sound(file):
    try:
        pygame.mixer.music.load(file)
        return True
    except pygame.error as e:
        print(f"Erreur lors du chargement du fichier {file} : {e}")
        return False

def play_sound(sound):
    try:
        pygame.mixer.music.play()
        t.sleep(1)
        pygame.mixer.music.stop()
    except pygame.error as e:
        print(f"Erreur lors de la lecture du fichier {sound} : {e}")

def timer(min, sec, son):
    if not load_sound(sounds[2]):
        return

    play_sound(sounds[2])
    duree = min * 60 + sec
    print("Départ du timer pour " , min , " minutes et " , sec , " secodes\n")
    print(min,":",sec)
    while duree != 0:
        t.sleep(1)
        if sec != 0:
            sec -= 1
            print(min,":",sec)
        elif sec == 0 and min != 0:
            if min == 1:
                min = 0
                sec = 59
                print(min,":",sec)
            elif min > 1:
                min -= 1
                sec = 59
                print(min,":",sec) 
        duree = min * 60 + sec
    print("Fin du timer\n")
    if not load_sound(sounds[son]):
        return

    play_sound(sounds[son])

def chrono(sonChrono):
    if not load_sound(sounds[2]):
        return

    play_sound(sounds[2])
    on = True
    print("Départ du Chrono\n")
    depart = t.time()
    while on :
        temps = t.time() - depart
        print(f"Temps écoulé : {temps:.2f} secondes", end="\r")
        t.sleep(0.01)

        if input() == '':
            on = False

    temps = t.time() - depart
    print(f"Chrono stoppé à {temps:.2f} secondes\n")
            
    if not load_sound(sounds[sonChrono]):
        return

    play_sound(sounds[sonChrono])

def session(minSession, minTimer, secTimer, sonTimer, minBreak, secBreak, sonBreak):
    dureeSession = minSession * 60
    if not load_sound(sounds[2]):
        return
    play_sound(sounds[2])

    nbSess = 1
    while dureeSession != 0:
        print("Depart session ", nbSess,"\n")
        timer(minTimer, secTimer, sonTimer) # timer
        temp1 = dureeSession - (minTimer *60)
        print("\nBREAK!\n")
        timer(minBreak, secBreak, sonBreak) # break
        minBreak *= 60
        dureeSession -= minBreak
        dureeSession -= secBreak
        nbSess += 1

def entrainement(sessions, timers, breaks):
    t.sleep(5)
    for i in range(len(sessions)):
        session(sessions[i], timers[i][0], timers[i][1], timers[i][2], breaks[i][0], breaks[i][1], breaks[i][2])
        
def setSession(sessions):
    print("\nCombien de session(s) souhaitez-vous faire? \n")
    nbSess= input()
    try:
        nbSess = int(nbSess)
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre.")
        return
    for i in range(nbSess):
        print("\nCombien de temps dure la session ", i+1, "?\n")
        nbTemps = input()
        try:
            nbSess = int(nbSess)
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")
            return
        sessions.append(nbTemps)
    """
    print("\nRécapitulatif de la session d'entrainement:\n")
    print("Vous allez faire ", nbSess, " session(s)\n")
    for i in range(nbSess):
        print("Session ", i+1, " va durée ", session[i], " minutes\n")
    """

def setTimer(nbSession, timers):
    print("\nVous devez faire ", nbSession, " sessions\n")
    for i in range(nbSession):
        interTimer = [0, 0, 0]
        print("\nVeuillez saisir le nombre de minutes à répéter pour la pratique de la session ", i+1,"\n")
        nbMin = input()
        try:
            nbMin = int(nbMin)
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")
            return
        interTimer[0] = nbMin
            
        print("\nVeuillez saisir le nombre de secondes à répéter pour la session", i+1,"\n")
        nbSec = input()
        try:
            nbSec = int(nbSec)
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")
            return
        interTimer[1] = nbSec
        timers.append(interTimer)

def setBreak(nbSession, breaks):
    print("\nVous devez faire ", nbSession, " sessions\n")
    for i in range(nbSession):
        interBreak = [0, 0, 1]
        print("\nVeuillez saisir le nombre de minutes à répéter pour le break ", i+1, "\n")
        nbMin = input()
        try:
            nbMin = int(nbMin)
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")
            return
        interBreak[0] = nbMin

        print("\nVeuillez saisir le nombre de secondes à répéter pour le break ", i+1, "\n")
        nbSec = input()
        try:
            nbSec = int(nbSec)
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")
            return
        interBreak[1] = nbSec
        breaks.append(interBreak)
    

def main():
    print("\n\nBienvenue pour votre session d'entrainement:\n")
    print("Que voulez vous faire? 1. Session - 2. Chronomètre - 5. Quitter\n")
    choix = input()

    try:
        choix = int(choix)
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre.")
        return
    
    if choix == 1:
        sessions = []
        timers = []
        breaks = []
        setSession(sessions)
        nbSession = len(sessions)
        setTimer(nbSession, timers)
        setBreak(nbSession, breaks)
        entrainement(sessions, timers, breaks)
        print("Votre Session est terminée! A demain!!\n")
        return
    elif choix == 2:
        chrono(1)
        print("\n\nLe chrono est terminé! A demain!!\n")
        return
    elif choix == 5:
        print("A demain!!!!\n")
        return
    else: 
        print("Option invalide. Veuillez choisir un chiffre entre 1, 2 et 5\n")
        return
"""
sessions = [2, 5, 5, 10]

timers = [[0,30,0], [0,20,0], [0,20,0], [0,30,0]] # (minute, secodes, num_son)

breaks = [[0,30,1], [0,10,1], [0,10,1], [0,10,1]]

main(sessions, timers, breaks)
"""
main()