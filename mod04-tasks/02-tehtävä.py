inpTuumia = 0
while inpTuumia >= 0:
    inpTuumia = input("Anna tuumamäärä:")
    while type(inpTuumia) != int:
        try:
            inpTuumia = int(inpTuumia)
        except:
            print("Virheellinen arvo. Syötä tuumamäärä oikeassa muodossa (kokonaisluku)!")
            inpTuumia = input("Anna tuumamäärä:")

    if inpTuumia >= 0:
        print (f"Se on {int(inpTuumia*2.54):.2f} senttimetriä")
    else:
        print ("Virhe. Tuumamäärä ei voi olla negatiivisena")
        print ("Ohjelma lopetettu")
