#Suorakulmion piiri ja pinra-alan laskeminen
#Kaava (piiri) kanta*korkeus*2

suorakulmion_kanta_str = input("Suorakulmion kannan pituus (m):")
kanta = float(suorakulmion_kanta_str)
suorakulmion_korkeus_str = input("Suorakulmion korkeus (m):")
korkeus = float(suorakulmion_korkeus_str)
print(f"Suorakulmion kannan piiri on {kanta*korkeus*2} (m)")
