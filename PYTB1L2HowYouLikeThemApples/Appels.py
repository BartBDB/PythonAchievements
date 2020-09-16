ZonAppelbomen = 111
Schaduwappelbomen = 222

Zonappels = 146
Schaduwappels = 146/100
Schaduwappels *= 80
Schaduwappels //= 1
#Rond naar beneden af, dus er is 1 appel over.

AlleAppels = (ZonAppelbomen*Zonappels+Schaduwappelbomen*Schaduwappels)
print("Het totale aantal appels is " + str(AlleAppels))
Restwaarde = (AlleAppels % 4) + 1
AlleAppels //= 4
print("Het totale aantal appels dat ik mag verkopen is " + str(AlleAppels))
print("Het aantal appels wat overblijft is " + str(Restwaarde))