import random
inpN = int(input("Anna arpakuutioiden lukumäärä: "))
n = []                  # arpakuutioiden silmäluvut
for i in range(1, inpN+1):
    n.append(random.randint(1,6)) #satunnaisten silmälukujen luominen
print (n)
print(f"Silmälukujen summa on {sum(n)}")