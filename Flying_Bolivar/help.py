def help(check_status):
    if check_status == "in_transportmenu":
        print("\nKulkuvälineiden ominaisuudet: ")
        print(f"\nLiitokone:, Nopeus: 60 km/h ja kulutus 50.")
        print(f"Lentokone: Nopeus 600 km/h ja kulutus 120.")
        print(f"Hävittäjä: Nopeus 1200 km/h ja kulutus 300.")
        print(f"Helikopteri: Nopeus 300 km/h ja kulutus 100.")
        print(f"Kuumailmapallo: Nopeus 50 km/h ja kulutus 10.")
    elif check_status == "in_continentmenu":
        print("\nTodennäköisimmät säätilat Euroopassa: 0-astetta ja pilvinen")
        print("Todennäköisimmät säätilat Aasiassa: Kuuma ja kirkas")
        print("Todennäköisimmät säätilat Pohjois-Amerikassa: 10-astetta ja tuulinen")
        print("Todennäköisimmät säätilat Afrikassa: Kuuma ja 20-astetta,")
        print("Todennäköisimmät säätilat Etelämantereella: Kylmä ja ehkä kirkas, tuulinen ja pilvinen.")
        print("Todennäköisimmät säätilat Etelä- Amerikassa: 20-astetta ja kuuma")
        print("Todennäköisimmät säätilat Oseaniassa: Kuuma, 20-astetta ja tuulinen")
    elif check_status == "in_airportmenu":
        print("\nKulkuvälineet ja lentokenttätyypit: ")
        print("\nHävittäjällä on mahdollista lentää: pienille, keskikokoisille, suurille ja suljetuille lentokentille sekä helikopteri-ja kuumailmapallokentille")
        print("Lentokoneella on mahdollista lentää: pienille, keskikokoisille,suurille ja suljetuille lentokentille")
        print("Liitokoneella on mahdollista lentää: pienille, keskikokoisille,suurille ja suljetuille lentokentille")
        print("Kuumailmapallolla on mahdollista laskeutua: Kuumailmapallokentille")
        print("Helikopterilla on mahdollista laskeutua helikopterikentille")
    elif check_status == "in_countrymenu":
        print(f"\nEt kait sinä nyt maiden valitsemiseen apua tarvitse. Ne on vain maita.")
    else:
        print(f"\nOlet nyt main menussa.")