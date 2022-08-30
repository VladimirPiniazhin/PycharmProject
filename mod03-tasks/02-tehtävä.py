luokka = input ("Mikä sun hyttiluokka on? (LUX, A, B, C):")
if luokka.lower() == "lux":
        print("LUX on parvekkeellinen hytti yläkannella")
elif luokka.lower() == "a":
        print("A on ikkunallinen hytti autokannen yläpuolella.")
elif luokka.lower() == "b":
        print("B on ikkunaton hytti autokannen yläpuolella")
elif luokka.lower() == "c":
        print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.Syötä hyttiluokka oikenmuodossa (A, B, C, LUX)")