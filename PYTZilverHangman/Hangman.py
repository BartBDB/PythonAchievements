#oke dus, hangman spel
#Denk dat lists maken handig is. 1 lijst met meerdere woorden, 1 voor het complete woord, 1 voor de correcte letters en 1 voor de foute letters
#let erop dat je geen figuur moet tekenen (Godzijdank), je hebt alleen levens.

import os #Screen clearing, wel handing meestal
import time #Misschien wel handig
import random #Willekeurig woord kiezen

isRunning = True #Dit moet False worden aan het einde om het programma af te sluiten

woordenLijst = ["discord", "mediacollege", "koptelefoon", "python", "saturnus", "warframe"]
gekozenWoord = []
correcteLetters = []
fouteLetters = []

gameSetup = False

def displayStatus():
    print("Levens over: " + str(levens))
    print("Foute letters: " + str(fouteLetters))
    print("Goede letters: " + str(correcteLetters))

while isRunning == True: #Wanneer het script start, dit wordt dus de hoofdfunctie van het spel
    print("Welkom bij Hangman!")
    print("In dit spel moet je alle letters van een woord raden, voordat je levens opzijn.")
    print("Elke keer als je een letter fout hebt, gaat er een leven vanaf")
    print("De game start in 10 seconden, veel plezier!")
    time.sleep(10)
    if gameSetup == False:
        levens = 6
        gekozenWoord.append(woordenLijst[random.randrange(0, len(woordenLijst))])
        print(gekozenWoord[0])
        os.system("cls")
        gameSetup = True #Zorgt ervoor dat dit maar 1 keer gebeurt, aan het begin van het spel.
    displayStatus()
    exit()