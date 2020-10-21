import time

isRunning = True
getal = input("Vanaf welk getal tellen wij af? ")
#Je kan natuurlijk ook een getal hier invoeren in plaats van input(), maar dit is leuker.

while (isRunning == True):
    getal = int(getal) - 1
    time.sleep(0.01)
    #Als wij input() niet gebruiken, moet int() weg hierboven.
    print(getal)
    if getal == 0:
        print("En nu zitten wij op 0.")
        exit() #Dit zorgt ervoor dat het programma ook afsluit en je weer verder kan met je commandline.
