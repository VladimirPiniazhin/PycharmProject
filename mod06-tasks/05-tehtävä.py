

def list_summa(list):
    b = []
    for n in list:
        if n % 2 == 0:
            b.append(n)
    return b

a = []

for i in range(5):
    numero = int(input("Syötä 5 kokonaislukua: "))
    a.append(numero)

list_summa(a)

print(a)
print(list_summa(a))