class Koira:
    jalka_maara = 4
    tehty = 0
    def __init__(self, nimi, syntymavuosi, rotu, paino, haukahdus = "vuh vuh"):
        self.nimi = nimi
        self.syntymavuosi = syntymavuosi
        self.rotu = rotu
        self.paino = paino
        self.haukahdus = haukahdus
        Koira.tehty = Koira.tehty + 1
    def hauku(self,kerrat):
        for i in range(kerrat):
            print(self.haukahdus)

#PÄÄOHJELMÄ
koira1 = Koira("Churro", 1999, "Saksanpaimenkoira", 25, "Räyh Räyh")
#print(f"Koira\nNimi: {koira1.nimi:s} \nSyntymavuosi: {koira1.syntymavuosi:d} \nRotu: {koira1.rotu:s} \nPaino: {koira1.paino:d}")
koira2 = Koira("Pulivari", 1938, "Berhandilainen", 40, "Mäy")
#print(f"Koira\nNimi: {koira2.nimi:s} \nSyntymavuosi: {koira2.syntymavuosi:d} \nRotu: {koira2.rotu:s} \nPaino: {koira2.paino:d}")

#koira1.hauku(5)
#koira2.hauku(1)

print(Koira.jalka_maara)
print(koira1.jalka_maara)
koira1.jalka_maara = 3
print(koira2.jalka_maara) # muutos koski vain koita1:tä  vaikka staattinen muutuja
print(f"Koiria on nyt {Koira.tehty}.")
koira1.tehty = 10
