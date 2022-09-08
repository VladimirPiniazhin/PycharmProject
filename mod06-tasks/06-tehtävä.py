import math

def pizza_hinta (halkaisija , hinta):
    yksikko_hinta = hinta /((math.pi * halkaisija * halkaisija)/4)

    return yksikko_hinta

# funktiokutsu
pizza_a_hal = int(input("Anna 1. pizzan halkaisija (cm): "))
pizza_a_hin = int(input("Anna 1. pizzan hinta (eur): "))
pizza_b_hal = int(input("Anna 2. pizzan halkaisija (cm): "))
pizza_b_hin = int(input("Anna 2. pizzan hinta (eur): "))

a1 = pizza_hinta(pizza_b_hal, pizza_a_hin)
b1 = pizza_hinta(pizza_b_hal, pizza_b_hin)

if a1 > b1:
    print("2. pizza antaa paremman vastineen rahalle")
elif a1 < b1:
    print("1. pizza antaa paremman vastineen rahalle")
else:
    print("Sama hinta")



