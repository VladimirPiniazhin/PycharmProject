# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä,
# haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa.
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta kertaa
# tahansa aina siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

n = ""
dictionary = {"LLIB":"Ben Ya'akov Airport","LLMZ":"Bar Yehuda Airfield","LLNV":"Nevatim Air Base","LLSR":"Soroka Medical Center","LLHA":"Haifa International Airport"}
while n != 3:
    print("Jos haluat syöttää uuden lentoaseman syötä - 1")
    print("Jos haluat hakea jo syötetyn lentoaseman tiedot syötä - 2")
    print("Jos haluat lopettaa ohjelman - 3")
    n = int(input("Syötä numero: "))
    if n == 1:
        a = input("Syötä uuden lentoaseman ICAO-koodi: ")
        b = input("Syötä uuden lentoaseman nimi: ")
        dictionary[a] = b
    elif n == 2:
        c = input("Syötä haun lentoaseman ICAO-koodi: ")
        print(f"Lentoaseman nimi on {dictionary.get(c)}")

    elif n != 3 and n != 2 and n != 1:
        print("Numero syötetty väärin")

print("Ohjelma lopetettu")