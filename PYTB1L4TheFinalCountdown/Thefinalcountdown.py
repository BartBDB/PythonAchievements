isRunning = True
getal = input("Vanaf welk getal tellen wij af? ")
#Je kan natuurlijk ook een getal hier invoeren in plaats van input(), maar dit is leuker.

while (isRunning == True):
    getal = int(getal) - 1
    #Als wij input() niet gebruiken, moet int() weg hierboven.
    if getal == 0:
        print("Never gonna give you up. Never gonna let you down. Never gonna run around and desert you. Never gonna make you cry. Never gonna say goodbye. Never gonna tell a lie and hurt you")
        exit() #Dit zorgt ervoor dat het programma ook afsluit en je weer verder kan met je commandline.
