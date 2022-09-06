#n = input("Syötä kokonaisluku: ")

#while n.isnumeric():
    #if int(n) / 1 == int(n) and int(n) / int(n)  == 1:
        #print("Se on alkuluku")
        #break
    #else:
       # print("Se ei ole alkuluku")

#print("Se ei ole numero")
#n = " "
#while n != 1 and n:
n = int(input("Syötä numero: "))
for i in range(1, n+1):
    if 1 <= n <= 3:
        print("Se on alkuluku")
        break
    elif n % i == 0 and n != i:
        print("Se ei ole alkuluku")
        break
    else:
        print("Se on alkuluku")
        break

#d1 = len(d)

#print(len(d))

#for i in range(1, n):
    #if n / i == int and (i != int(n) and int(n) / i == 1):
        #print(f"Se on alkuluku")
    #else:
        #print("Se ei ole alkuluku")