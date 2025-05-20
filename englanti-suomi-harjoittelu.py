#
import random

def sanakirja_luku(tiedosto_placeholder):
    sanakirja = {}
    with open("sanakirja.txt", "r", encoding="utf-8") as tiedosto:
        for rivi in tiedosto:
            if "," in rivi:
                englanti, suomi = rivi.strip().split(",")
                sanakirja[englanti] = suomi
    return sanakirja

def käännös(sanakirja, käännöskieli):
    toistomäärä = 0
    while True:
        if käännöskieli == "1":
            sana = random.choice(list(sanakirja.keys()))  #random valinta
            oikea_vastaus = sanakirja[sana]
            vastaus = input(f"Mikä on sanan {sana} suomennos?")
            if vastaus == oikea_vastaus:
                print("Oikein")
            else:
                print(f"Väärin, oikea vastaus on: {oikea_vastaus}")
        elif käännöskieli == "2":
            sana = random.choice(list(sanakirja.values()))
            oikea_vastaus = [e for e, s in sanakirja.items() if s == sana][0] #e = englanti arvo - s = suomi arvo
            vastaus = input(f"Mikä on sanan {sana} käännös englanniksi? ")
            if vastaus == oikea_vastaus:
                print("Oikein!")
            else:
                print(f"Väärin. Oikea vastaus on {oikea_vastaus}")
        else:
            print("Virheellinen valinta.")
            break
        toistomäärä += 1
        if toistomäärä % 5 == 0: #Kysytään viiden kysymyksen jälkeen halutaanko jatkaa.
            jatka = input("Haluatko jatkaa? kyllä/ei: ")
            if jatka != "kyllä":
                print("Kiitos!")
                break

def main():
    sanakirja = sanakirja_luku("sanakirja.txt")
    
    print("Valitse käännöskieli:")
    print("1 = Englannista suomeksi")
    print("2 = Suomesta englanniksi")
    käännöskieli = input("Valitse 1 tai 2: ")
    käännös(sanakirja, käännöskieli)

if __name__ == "__main__":
    main()