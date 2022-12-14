#Megkérdezzük a felhasználótól milyen játékot szeretne játszani!

import os
os.system('cls')  #Töröl a Consolból mindent ami elötte van

while(True):
    print("- Roulett (1) \n- BlackJack (2) \n")
    jatek = int(input("Kérem adja meg annak a játéknak a számát amivel játszani szeretne: "))
    if jatek == 1:
        os.system('cls')
        print("\nA Roulette-t választotta!")
        valasz = input("\nSzeretné átnézni a szabályokat? (I/N)")
    if jatek == 2:
        os.system('cls')
        print("\nA BlackJack-et választotta!")
        valasz = input("\nSzeretné átnézni a szabályokat? (I/N)")