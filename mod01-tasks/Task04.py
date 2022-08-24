#Summan, tulon ja keskiarvon laskeminen
#Kaava (tulo) a*b*c
#Kaava (summa) a+b+c
#Kaava (Keskiarvo) (a+b+c)/3

a_str = input ("Eka luku:")
a = float(a_str)
b_str = input ("Toka luku:")
b = float(b_str)
c_str= input ("Kolmas luku:")
c = float(c_str)
tulo = a*b*c
summa = a+b+c
keskiarvo = (a+b+c)/3
print(f"Tulo: {tulo:.2f} ")
print(f"Summa: {summa:.2f} ")
print(f"Keskiarvo: {keskiarvo:.2f} ")