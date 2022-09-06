#nimet = ["Heini", "Matti", "Miikka", "Ile", "Saana", "Chau", "Jarkko"]
#print(nimet[3])
#print(nimet[-2])
#print(nimet[1:3])
#print(nimet[2:])
#print(nimet)
#print (len(nimet))

nimet = []

nimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
while nimi!="":
    nimet.append(nimi)
    nimi = input("Anna seuraava nimi tai lopeta painamalla Enter: ")

print(nimet)
