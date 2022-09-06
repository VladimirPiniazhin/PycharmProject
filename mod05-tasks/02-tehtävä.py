
d = []
n = " "
while n != "":
    n = input("Syötä numero: ")
    if n.isnumeric():
        d.append(int(n))
    else:
        print("Se ei ole numero")

d1 = sorted(d, reverse=True)

for i in range(5):
    print(f"{i+1}. suurin numero: {d1[i]}")
