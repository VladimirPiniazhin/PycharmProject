
a = int(input("Syötä kokonaisluku: "))
k = 0
for i in range(2, a // 2+1):
    if (a % i == 0):
        k +=1
if (k == 0):
    print("Se on alkuluku")
else:
    print("Se ei ole alkuluku")

