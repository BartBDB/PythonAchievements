print("Goedemorgen gebruiker!")
print("jouw telefoon gaat af, wil je opnemen?")
print("A - ja")
print("B - nee")
antwoord1 = input()
if antwoord1 == "A" or antwoord1 == "a":
    print("Je neemt de telefoon op.")
    print("Het is reclame, was dus redelijk onnodig om op te nemen")
elif antwoord1 == "B" or antwoord1 == "b":
    print("Je besluit om de telefoon niet op te nemen. Diegene die belt heeft maar pech gehad.")
else:
    print(antwoord1 + " was geen keuze die je kon maken")

print("Je loopt naar beneden, naar de keuken toe. Wat ga je drinken?")
print("A - Een glas water")
print("B - Koffie")
print("C - Thee")
antwoord2 = input()
if antwoord2 == "A" or antwoord2 == "a":
    print("Je besluit om een glas water te pakken.")
elif antwoord2 == "B" or antwoord2 == "b":
    print("Je besluit om een kop koffie te maken")
elif antwoord2 == "C" or antwoord2 == "c":
    print("Je besluit om een lop thee te maken")
else:
    print(antwoord2 + " was geen keuze die je kon maken")