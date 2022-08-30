sukupolvi = ""
while sukupolvi != "mies" and sukupolvi != "nainen":
    sukupolvi = input("Mikä sinun sukupolvi on? (mies/nainen):")
    if sukupolvi.lower() == "mies":
        print("Selvä")
    elif sukupolvi.lower() == "nainen":
        print("Selvä")
    else:
        print("Virheellinen sukupolvi. Syötä sukupolvi oikeassa muodossa (mies/nainen)!")

hemoglobiiniarvon = input("Mikä sinun hemoglobiiniarvon on?(g/l):")

while type(hemoglobiiniarvon) != int:
    try:
        hemoglobiiniarvon = int(hemoglobiiniarvon)
    except:
        print("Virheellinen arvo. Syötä hemoglobiiniarvon oikeassa muodossa (kokonaisluku)!")
        hemoglobiiniarvon = input("Mikä sinun hemoglobiiniarvon on?(g/l):")

if sukupolvi == "mies":
    if hemoglobiiniarvon < 134:
        print("Hemoglobiiniarvon on alhainen")
    elif hemoglobiiniarvon > 195:
        print("Hemoglobiiniarvon on korkea")
    else:
        print("Hemoglobiiniarvon on normaali")

elif sukupolvi == "nainen":
        if hemoglobiiniarvon < 117:
            print("Hemoglobiiniarvon on alhainen")
        elif hemoglobiiniarvon > 175:
            print("Hemoglobiiniarvon on korkea")
        else:
            print("Hemoglobiiniarvon on normaali")
