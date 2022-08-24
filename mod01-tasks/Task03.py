#Suorakulmion piiri ja pinra-alan laskeminen
#Kaava (piiri) kanta*korkeus*2
#Kaava (pinta-ala) kanta*korkeus/2

suorakulmion_kanta_str = input("Suorakulmion kannan pituus (m):")
kanta = float(suorakulmion_kanta_str)
suorakulmion_korkeus_str = input("Suorakulmion korkeus (m):")
korkeus = float(suorakulmion_korkeus_str)
piiri = (kanta+korkeus)*2
pintaala = kanta*korkeus
print(f"Suorakulmion kannan piiri: {piiri} (m)")
print(f"Suorakulmion pinta-ala: {pintaala} (m^2)")
