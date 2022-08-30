pituus = float (input("Syötä kuhan pituuden (cm):"))
if pituus < 37:
    print (f"Laske se takasin järveen koska kuhan pituus on {37 - pituus} sentti(ä) alimmasta sallitusta pyyntimitasta puuttuu")
else:
    print("Kuha ei ole alamittainen")