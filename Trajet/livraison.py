from math import floor

# Dictionnaire
ville = {
    "Biarritz-Dax": 59,
    "Biarritz-Marmande": 231,
    "Biarritz-Pau": 119,
    "Biarritz-Poitiers": 442,
    "Biarritz-Tours": 540,
    
    "Dax-Marmande": 175,
    "Dax-Pau": 85,
    "Dax-Poitiers": 398,
    "Dax-Tours": 496,

    "Marmande-Pau": 193,
    "Marmande-Poitiers": 335,
    "Marmande-Tours": 335,

    "Pau-Poitiers": 462,
    "Pau-Tours": 559,

    "Poitiers-Tours": 105
}

print("\nListe des différentes villes:\nBiarritz\nDax\nMarmande\nPau\nPoitiers\nTours\n")

# Trou à Variable
start = input("De quelle ville partez-vous ?\n")
finished = input("Vers quelle destination ?\n")
# etapes = input("Si vous avez des livraisons sur le chemin, ecrivez les ici en les séparant par un tiret (-)\n").split('-')
asc = sorted([start.capitalize(), finished.capitalize()])
km = int(ville.get("{}-{}".format(asc[0], asc[1])))
timing = 0
pauses = 0
expo = 1
dist = 0

# Script
if km < 15:
    kmRest = km / 2
    while kmRest > 0:
        dist = dist + ((10/60) * expo)
        expo += 1
        kmRest = kmRest - (dist/2)
    timingM = expo

if 15 <= km <= 168:
    kmRest = km - 15
    timing = ((kmRest/1.5) + 18)
    timingH = floor(timing / 60)
    timingM = floor(timing % 60)
if km > 168:
    if (km % 168) > 15:
        pauses = floor(km / 168)
        kmRest = (km % 168) - 15
        timing = (kmRest/1.5) + 18
        timingH = floor(timing / 60) + (pauses*2)
        timingM = floor(timing % 60)
    else:
        pauses = floor(km / 168)
        kmRest = (km % 168) / 2
        while kmRest > 0:
            dist = dist + ((10/60) * expo)
            expo += 1
            kmRest = kmRest - (dist/2)
        timingH = pauses*2
        timingM = expo

if pauses != 0:
    newTime = (timingH * 60) + (pauses * 15) + timingM
    newTimeH = floor(newTime / 60)
    print(newTimeH)
    newTimeMin = newTime - (newTimeH*60)

print("\nVotre trajet de livraison : \n")
print("Depart : " + start.capitalize())
print("Arrivée : " + finished.capitalize())
print("Distance : {} Km".format(str(km)))
if timingH != 0:
  print("Temps de conduite : {}h {}min".format(str(timingH), str(timingM)))
  print("Temps total de votre Trajet : {}h {}min".format(str(newTimeH), str(newTimeMin)))
else:
  print("Temps total de votre Trajet: {}min".format(str(timingM)))
print("Pauses : " + str(pauses))
