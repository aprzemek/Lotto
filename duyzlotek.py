import random
import time

while True:
    print("Podaj swoje imie: ")
    imie=input()
    def przywitanie():
        print("WITAJ "+ imie+" W DUŻYM LOTKU! PODAJ 6 LICZB OD 1 DO 50")

    przywitanie()

    ileliczb= 6
    maksliczba = 50
    liczby = []
    i = 0

    while i < ileliczb:
        liczba = random.randint(1, 50)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            i = i + 1

    for i in range(1):
        typy = set()
        i = 0
        while i < ileliczb:
            typ = int(input("Podaj liczbę %s: " % (i + 1)))
            if typ not in typy and typ <= 50 and typ !=0:
                typy.add(typ)
                i = i + 1

        time.sleep(1)
        print("Twoje liczby to:", sorted(typy))
        print("\n" + "x" * 40 +" LOSOWANIE " + "x" * 40+"\n")
        time.sleep(3)
        print("Wylosowane liczby to :", sorted(liczby))
        time.sleep(1)
        trafione = set(liczby) & typy

        time.sleep(2)
        if trafione:
            print("\nIlość trafień: %s" % len(trafione))
            time.sleep(2)
            print("\nTrafione liczby: ", trafione)
        else:
            print("\nBrak trafień. Spróbuj jeszcze raz!")

        time.sleep(2)
        if len(trafione) == 3:
                print("\nGRATULACJĘ " +imie+ ", WYGRAŁEŚ: 10 ZŁ!")
        elif len(trafione) == 4:
                print("\nGRATULACJĘ " +imie+ ", WYGRAŁEŚ: 100 ZŁ!")
        elif len(trafione) == 5:
                print("\nGRATULACJĘ " +imie+ ", WYGRAŁEŚ: 3500 ZŁ!")
        elif len(trafione) == 6:
                print("\nGRATULACJĘ " +imie+ ", WYGRAŁEŚ: 1 000 000 ZŁ!")
        elif len(trafione) == 0 or len(trafione) == 1 or len(trafione) == 2:
                print("\nNIESTETY " +imie+ ", NIC NIE WYGRAŁEŚ")

        localtime = time.localtime(time.time())
        timestring = time.strftime('%Y/%m/%d - %H:%M:%S')
        zapisanewyniki = open("wynikilosowan.txt", "a")
        zapisanewyniki.write("\nWylosowane liczby dnia: %s"% timestring + " to: "+str(sorted(liczby)))
        kupony = open("kupony.txt", "a")
        kupony.write("\nKupon dnia: %s" % timestring + " to: " +str(sorted(typy)))

        while True:
            answer = str(input("\nCzy chcesz zagrać jeszcze raz? (tak/nie): "))
            if answer in ('tak', 'nie'):
                break
            print("\nNieprawidłowa wartość!")
        if answer == 'tak':
            continue
        if answer == 'nie':
            print("\nKONIEC GRY!\n")
            quit()





