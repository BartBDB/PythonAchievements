#oke dus, hangman spel
#Denk dat lists maken handig is. 1 lijst met meerdere woorden, 1 voor het complete woord, 1 voor de correcte letters en 1 voor de foute letters
#let erop dat je geen figuur moet tekenen (Godzijdank), je hebt alleen levens.
#Om letters te vergelijken is het *denk ik* het makkelijkste om INDEX te gebruiken. Ik moet dan wel het hele woord in elkaar hakken en in een lijst doen.

import os #Screen clearing, wel handing meestal
import time #Misschien wel handig
import random #Willekeurig woord kiezen

isRunning = True #Dit moet False worden aan het einde om het programma af te sluiten

woordenLijst = ["discord", "mediacollege", "koptelefoon", "python", "saturnus", "warframe"]

gameSetup = False

def gameReset():
    gekozenWoord = []
    gehakteWoord = []
    correcteLetters = []
    fouteLetters = []

def displayStatus():
    print("Levens over: " + str(levens))
    print("Foute letters: " + str(fouteLetters))
    print("Goede letters: " + str(correcteLetters))

while isRunning == True: #Wanneer het script start, dit wordt dus de hoofdfunctie van het spel
    print("Welkom bij Hangman!")
    print("In dit spel moet je alle letters van een woord raden, voordat je levens opzijn.")
    print("Elke keer als je een letter fout hebt, gaat er een leven vanaf")
    print("De game start in een paar seconden, veel plezier!")
    time.sleep(3)
    gekozenWoord = []
    gehakteWoord = []
    correcteLetters = []
    fouteLetters = []
    if gameSetup == False:
        gameReset()
        levens = 6
        gekozenWoord.append(woordenLijst[random.randrange(0, len(woordenLijst))])
        print(gekozenWoord[0])
        os.system("cls")
        gameSetup = True #Zorgt ervoor dat dit maar 1 keer gebeurt, aan het begin van het spel.
    displayStatus()
    letter = input("Type een letter in: ")
    if letter == correcteLetters.index(letter) or letter == fouteLetters.index(letter):
        print("Deze letter is al geraden, kies alsjeblieft een andere letter.")
    elif letter == gehakteWoord.index(letter): #Als het dus klopt
        correcteLetters.append(letter)
    else:
        levens = (levens - 1)
        fouteLetters.append(letter)
    if levens <= 0: #just to be sure
        print("Je hebt het woord niet kunnen raden, game over!")
        print("Het te raden woord was: " + gekozenWoord)
        opnieuw = input("Wil je het spel nog een keer spelen? (Ja of Nee)")
        if opnieuw == "Ja" or "ja":
            gameSetup = False
        elif opnieuw == "Nee" or "nee":
            exit()