def muunnos():
    gallona = int(input("Anna gallonamäärä: "))
    while gallona > 0:
        litra = gallona * 3.785
        print(f"Se on {litra:.2f} litraa")
        gallona = int(input("Anna gallonamäärä: "))

    return print("Ohjelma on lopetettu")

muunnos()

