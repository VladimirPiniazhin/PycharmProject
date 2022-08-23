#Ympyrän pinra-alan laskeminen
#Kaava Pii*r2
#Säde - "radius"
import math
radius = input ("Anna ympyrän säde (m):")
area = math.pi*float(radius)*float(radius)
print(f"{radius} (m) säteisin ympyrän pinta-ala on {area:.3f} neliömetriä")