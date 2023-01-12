#Megkérdezzük a felhasználótól milyen játékot szeretne játszani!

import os #Os modult beimportáljuk
os.system('cls')  #Töröl a Consolból mindent ami elötte van
import random #Random modult beimportáljuk
import time #Time modult beimportáljuk

zseton = 500 #Kezdő zsteon szám


while(True):
    print("- Roulett (1) \n- BlackJack (2) \n- Darts (3)\n")
    print("\nZsetonok száma:", zseton)
    jatek = int(input("Kérem adja meg annak a játéknak a számát amivel játszani szeretne: "))
    if zseton == 0:
        os.system('cls')
        print("Nincs több zsetonja. Szeretne még 500-at? (I/N)\n")
        valasz = input()
        if valasz == "I" or valasz == "i":
            zseton = zseton + 500
        elif valasz == "N" or valasz == "n":
            break
    if jatek == 1:
        os.system('cls')
        print("\nA Roulette-t választotta!")
        while(True):
            os.system('cls')
            while(True):
                print("\nKérem válasszon számot!\n\nPiros: 2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36\nFekete: 1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35\nZöld: 0")
                szam = int(input())
                print("Zsetonok száma = ", zseton)
                tet = int(input("Kérem adja meg a tét mennyiségét!\n"))
                zseton = zseton - tet
                randomszam = random.randint(1,37)
                if szam == randomszam:
                    zseton = zseton + (tet * 2)
                    print("Nyertél", tet * 2, "zsetont")
                    valasz = input("Szeretne tovább játszani? (I/N)")
                    if valasz == "I" or valasz == "i":
                        break
                    elif valasz == "N" or valasz == "n":
                        break
                    break
                elif szam != randomszam:
                    print("Sajnos nem nyertél!")
                    valasz = input("Szeretne tovább játszani? (I/N)")
                    if valasz == "I" or valasz == "i":
                        break
                    elif valasz == "N" or valasz == "n":
                        os.system('cls')
                        break
                    break
                break
            break

    if jatek == 2:
        os.system('cls')
        print("\nA BlackJack-et választotta!")


    if jatek == 3:
        os.system('cls')
        print("\nA Darts-ot válaszotta!")