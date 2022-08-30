input_year = input("Mikä vuosiluku on?:")
year = int(input_year)
if year % 400 == 0:
    print("%d Vuosi on karkausvuosi" %year)
elif year % 100 == 0:
    print("%d  Vuosi ei ole karkausvuosi" %year)
elif year % 4 == 0:
    print("%d Vuosi on karkausvuosi" %year)
else:
    print("%d Vuosi ei ole karkausvuosi" %year)