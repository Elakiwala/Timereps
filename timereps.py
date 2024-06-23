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
        t.sleep(2)
        if sec != 0:
            sec -= 1
            print(min,":",sec)
        elif sec == 0 and min != 0:
            if min == 1:
                min = 0
                sec = 58
                print(min,":",sec)
            elif min > 1:
                min -= 1
                sec -= 1
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
        timer(minBreak, secBreak, sonBreak) # break
        dureeSession = dureeSession - (minTimer * 60 + secTimer + minBreak * 60 + secBreak)
        nbSess += 1

def entrainement(sessions, timers, breaks):
    for i in range(len(sessions)):
        session(sessions[i], timers[i][0], timers[i][1], timers[i][2], breaks[0], breaks[1], breaks[2])
        

sessions = [2, 2, 3]

timers = [[0,20,0], [0,20,0], [0,30,0]] # (minute, secodes, num_son)

breaks = [0,10,1]


# entrainement(sessions, timers, breaks)

chrono(1)

