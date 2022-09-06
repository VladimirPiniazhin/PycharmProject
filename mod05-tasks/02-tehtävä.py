d = []
n = input("Syötä numero: ")
while n != "":
    n = input("Syötä numero: ")
    if n.isnumeric():
        d.append(n)
    else:
        print("Se ei ole numero")

print (sorted(d,reverse=True))
#print(d)
#for i in range(0,4):
    #print(f"Suurin numero: {print(d[:4])}")
#print(f"Yhteensä numeroita on {len(d)}; Max-arvo on {max(d)}; Min-arvo on {min(d)};")