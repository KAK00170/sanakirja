import random

def sanakirja_luku(tiedosto_placeholder):
    sanakirja = {}
    with open("sanakirja.txt", "r", encoding="utf-8") as tiedosto:
        for rivi in tiedosto:
            if "," in rivi:
                englanti, suomi = rivi.strip().split(",")
                sanakirja[englanti] = suomi
    return sanakirja

def käännös(sanakirja, käännöskieli):   #Ohjelma
    toistomäärä = 0
    while True:
        if käännöskieli == "1":         #Englannista suomeksi
            sana = random.choice(list(sanakirja.keys()))
            oikea_vastaus = sanakirja[sana]
            vastaus = input(f"Mikä on sanan {sana} suomennos?")
            if vastaus == oikea_vastaus:
                print("Oikein")
            else:
                print(f"Väärin, oikea vastaus on: {oikea_vastaus}")
        elif käännöskieli == "2":       #Suomesta englanniksi
            sana = random.choice(list(sanakirja.values()))
            oikea_vastaus = [e for e, s in sanakirja.items() if s == sana][0]   #e = englanti arvo - s = suomi arvo
            vastaus = input(f"Mikä on sanan {sana} käännös englanniksi? ")
            if vastaus == oikea_vastaus:
                print("Oikein!")
            else:
                print(f"Väärin. Oikea vastaus on {oikea_vastaus}")
        else:
            print("Virheellinen valinta.")
            break
        toistomäärä += 1
        if toistomäärä % 5 == 0:        #Kysytään viiden kysymyksen jälkeen halutaanko jatkaa.
            while True:
                jatka = input("Haluatko jatkaa? kyllä/ei: ")
                if jatka == "kyllä":
                    break
                elif jatka == "ei":
                    print("Kiitos!")
                    return
                else:
                    print("Virheellinen valinta. Kirjoita 'kyllä' tai 'ei'")

def main():
    sanakirja = sanakirja_luku("sanakirja.txt")
    
    while True:
        print("Valitse käännöskieli:")
        print("1 = Englannista suomeksi")
        print("2 = Suomesta englanniksi")
        print("0 = Lopeta ohjelma")
        käännöskieli = input("Valitse 1, 2 tai 0: ")
        
        if käännöskieli == "0":
            print("Kiitos!")
            break
        elif käännöskieli == "1" or käännöskieli == "2":
            käännös(sanakirja, käännöskieli)
        else:
            print("Virheellinen valinta, yritä uudelleen.")

if __name__ == "__main__":
    main()