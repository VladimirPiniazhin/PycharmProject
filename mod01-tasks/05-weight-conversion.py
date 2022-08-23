#Keskiaikaisten massan mittojen laskeminen
#Kaava (leviska) 20*naula
#Kaava (naula) 32*luoti
#Kaava (luoti) 13.3 grammaa

a_str = input ("Anna leiviskät:")
a = float(a_str)
b_str = input ("Anna naulat:")
b = float(b_str)
c_str= input ("Anna luodit:")
c = float(c_str)
leviska = a*20*32*13.3
naula = b*20*13.3
luoti = c*13.3
massa = leviska + naula + luoti
massa_kg = int(massa/1000)
massa_gr = massa - massa_kg*1000
print(f"Massa nykymittojen mukaan: \n{massa_kg} kilogrammaa ja {massa_gr:.2f} grammaa  ")


