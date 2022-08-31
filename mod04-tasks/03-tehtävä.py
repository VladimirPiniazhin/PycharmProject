d = []
n = ""
while not n.isspace():
    n = input("Syötä numero: ")
    if n.isnumeric():
        d.append(n)
    else:
        print("Se ei ole numero")

print(f"Yhteensä numeroita on {len(d)}; Max-arvo on {max(d)}; Min-arvo on {min(d)};")
