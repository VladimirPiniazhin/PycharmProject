
def list_summa(list):
    summa = 0
    for n in list:
        summa += n
    return summa

a = []
for i in range(5):
    numero = int(input("Syötä 5 kokonaislukua: "))
    a.append(numero)

print(list_summa(a))