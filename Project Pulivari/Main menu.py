from Kulkuvaline import aircraft_valiko

def main_menu():
    print(f"Nykyinen sijaintisi: Helsinki-Vantaa\nValitse kulkuväline")
    print("1 - Liitokone \n2 - Lentokone \n3 - Helikopteri \n4 - Hävittäjä \n5 - Kuumailmapallo")

    n = 6
    while n >= 6 or n <= 0:
        n = int(input("Syötä kulkuvälineen numero: "))
        if n not in range(1,6):
            print("Virheellinen numero. Syötä numero uudelleen")
        else:
            print("Great!")
    return n

n = main_menu()

aircraft_valiko(n-1)