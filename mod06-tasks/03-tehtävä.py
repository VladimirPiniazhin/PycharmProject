

def muunnos(gallona):
    gallona = 0
    while gallona > 0:
        gallona = int(input("Anna gallonamäärä: "))
        litra = gallona * 3.785
    return print(f"Se on {litra} litraa")

    print("Ohjelma on lopetettu")
    #return litra

gallona = int(input("Anna gallonamäärä: "))
muunnos(gallona)