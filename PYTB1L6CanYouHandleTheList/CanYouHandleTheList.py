opdrachtLijst = [2267.2, "Team Fortress 2", 20, "Metal Gear Rising REVENGEANCE", 250, "Sonic Robo Blast 2 Kart"]

extraLijst = [300, "Phantasy Star Online 2"]

print(opdrachtLijst)

opdrachtLijst.extend(extraLijst)

print("\nVoeg Phantasy Star Online 2 toe bij de lijst")
print(opdrachtLijst)

opdrachtLijst.pop(2)
opdrachtLijst.pop(2)

print("\nVerwijder Metal Gear Rising REVENGEANCE uit de lijst")
print(opdrachtLijst)

opdrachtLijst.reverse()

print("\nDraai de lijst om")
print(opdrachtLijst)