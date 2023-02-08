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
    while jatek == 1:
        os.system('cls')
        print("\nA Roulette-t választotta!")
        while(True):
            os.system('cls')
            while(True):
                print("\nKérem válasszon számot!\n\nPiros: 2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36\nFekete: 1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35\nZöld: 0")
                szam = int(input())
                print("Zsetonok száma = ", zseton)
                tet = int(input("Kérem adja meg a tét mennyiségét!\n"))
                if tet > zseton:
                    os.system('cls')
                    print("Kérem adjon meg annyit amennyi zsetonja van!")
                    print("Zsetonok száma", zseton)
                    tet = int(input())
                zseton = zseton - tet
                randomszam = random.randint(1,37)
                if szam == randomszam:
                    zseton = zseton + (tet * 2)
                    print("Nyertél", tet * 2, "zsetont")
                    valasz = input("Szeretne tovább játszani? (I/N)")
                    if valasz == "I" or valasz == "i":
                        continue
                    elif valasz == "N" or valasz == "n":
                        break
                    break
                elif szam != randomszam:
                    print("Sajnos nem nyertél!")
                    valasz = input("Szeretne tovább játszani? (I/N)")
                    if valasz == "I" or valasz == "i":
                        continue
                    elif valasz == "N" or valasz == "n":
                        os.system('cls')
                        break
                    break
                break
            break
        break

    while jatek == 2:
        os.system('cls')
        print("\nA BlackJack-et választotta!")
        print("Mennyi téttel szeretne játszani?")
        tet = int(input())
        zseton = zseton - tet
        mehet = 1
        kartyak = ["A", "K", "J", "Q", 1,2,3,4,5,6,7,8,9,10]
        while(mehet == 1):
            jatekoskartyalist = []
            vezetokartyalist = []
            jatekososszeg = 0
            vezetosszeg = 0
            for i in range(1):
                randomvezetokartya = random.choice(kartyak)
                if randomvezetokartya == "A" or randomvezetokartya == "K" or randomvezetokartya == "J" or randomvezetokartya == "Q":
                    vezetosszeg = vezetosszeg + 10
                else:
                    vezetosszeg = vezetosszeg + randomvezetokartya
                vezetokartyalist.append(randomvezetokartya)
            for i in range(2):
                randomjatekoskartya = random.choice(kartyak)
                if randomjatekoskartya == "A" or randomjatekoskartya == "K" or randomjatekoskartya == "J" or randomjatekoskartya == "Q":
                    jatekososszeg = jatekososszeg + 10
                else:
                    jatekososszeg = jatekososszeg + randomjatekoskartya
                jatekoskartyalist.append(randomjatekoskartya)
                while len(jatekoskartyalist) >= 2:
                    print("Mit szeretne elvégezni?\n-(1) Stand (Kimarad a körből)\n-(2) Hit (Kér mégegy lapot)\n")
                    print("A te kártyáid: ",jatekoskartyalist)
                    print("Az osztó kártyái: ",vezetokartyalist)
                    valasz = int(input())
                    if valasz == 1:
                        for i in range(1):
                            randomvezetokartya = random.choice(kartyak)
                            if randomvezetokartya == "A" or randomvezetokartya == "K" or randomvezetokartya == "J" or randomvezetokartya == "Q":
                                vezetosszeg = vezetosszeg + 10
                            else:
                                vezetosszeg = vezetosszeg + randomvezetokartya
                            if vezetosszeg > 21:
                                print("Az osztó kártyáinak száma több mint 21 lett!")
                                zseton = zseton + 2*(tet)
                                mehet = 0
                                jatek = 0
                                jatekoskartyalist = []
                                break
                            vezetokartyalist.append(randomvezetokartya)
                    if valasz == 2:
                        for i in range(1):
                            randomjatekoskartya = random.choice(kartyak)
                            if randomjatekoskartya == "A" or randomjatekoskartya == "K" or randomjatekoskartya == "J" or randomjatekoskartya == "Q":
                                jatekososszeg = jatekososszeg + 10
                            else:
                                jatekososszeg = jatekososszeg + randomjatekoskartya
                            if jatekososszeg > 21:
                                print("Túl lépted a 21-et!")
                                mehet = 0
                                jatek = 0
                                break
                            jatekoskartyalist.append(randomjatekoskartya)




    while jatek == 3:
        os.system('cls')
        print("\nA Darts-ot válaszotta!")
        print("Mennyi tétet szeretne kockáztatni?\n")
        print("Zsetonok száma:", zseton)
        tet = int(input())
        zseton = zseton - tet
        dartkezdo = 510
        mehet = 1
        while(mehet == 1):
            haromszam = []
            dartszamok = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,   22,24,26,28,30,32,34,36,38,40,  33,36,39,42,45,48,51,54,57,60]
            for i in range(3):
                randomszam = random.choice(dartszamok)
                if randomszam > dartkezdo:
                    os.system('cls')
                    print("Túl lépted volna a pontszámot! Vesztettél")
                    mehet = 0
                    jatek = 0
                    time.sleep(2)
                    os.system('cls')
                    break
                elif randomszam <= dartkezdo:
                    haromszam.append(randomszam)
                    print(randomszam, "a dobott érték")
                    dartkezdo = dartkezdo - randomszam
                    print(dartkezdo)
                if randomszam - dartkezdo == 0:
                    print("Gratulálok nyertél!")
                    zseton = zseton + 2*(tet)
                if len(haromszam) == 3:
                    print("Szeretne mégegyet dobni? (I/N)")
                    valasz = input()
                    if valasz == "I" or valasz == "i":
                        continue
                    elif valasz == "N" or valasz == "n":
                        mehet = 0
                        jatek = 0
                        os.system('cls')
                        break
                    else:
                        break
                else:
                    continue
            

