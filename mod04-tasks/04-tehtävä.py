import random
rundomNum = random.randint(0,10)

inpNum = ""
while rundomNum != inpNum:
    inpNum = input("Arvaa numero?:")
    while not inpNum.isnumeric():
        print("Virheellinen arvo. Syötä numero oikeassa muodossa (kokonaisluku)!")
        inpNum = input("Arvaa numero?:")

    if int(inpNum) < rundomNum:
        print ("Liian pieni arvaus")
    elif int(inpNum) > rundomNum:
        print("Liian suuri arvaus")
    else:
        print("Oikein")
        break
print("Ohjelma lopetettu")