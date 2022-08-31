userName = "python"
userPass = "rules"
i = 0
inpName = input("Käyttäjätunnus: ")
inpPass = input("Salasana: ")

while (inpName != userName or inpPass != userPass) and i < 4:
    i = i + 1
    print("Salasana ja Käyttäjätunnus jompikumpi tai molemmat ovat väärin")
    inpName = input("Käyttäjätunnus: ")
    inpPass = input("Salasana: ")

if inpName == userName and inpPass == userPass:
    print("Tervetuloa")

else:
    print("Pääsy evätty")



