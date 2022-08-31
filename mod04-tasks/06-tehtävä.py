import random
inpN = int(input("Anna arvottavien pisteiden kokonaismäärä: "))
n = 0                   # ympyrän sisälle jäävien pisteiden kokonaismäärä
for i in range(1, inpN + 1):
    x = random.random() # Satunnaisten koordinaattien luominen
    y = random.random() # Satunnaisten koordinaattien luominen
    if x*x+y*y<=1:      # Testaaminen, toteuttaako piste epäyhtälön
        n+=1
print(f"Piin likiarvo on {4.0*n/inpN}")