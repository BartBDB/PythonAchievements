# Verander in False als je geen schooldag hebt
schooldag = True
weekdag = input("Welke dag is het vandaag? ")

if schooldag == True and weekdag == "Maandag" or weekdag == "Dinsdag" or weekdag == "Woensdag" or weekdag == "Donderdag" or weekdag == "Vrijdag":
  print("Pak je spullen en ga er heen!")
else:
  print("Lekker uitslapen!")