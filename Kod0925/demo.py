siffra = input("Skriv en siffra: ")

print(f"Du skrev: {siffra}")


for i in range(5, 12, -2):
   print(i)


while True:
    print("välkommen till våra fina användarmeny!")
    print("öäå. Alternativ 1")
    print("2. Alternativ 2")
    print("3. Avsluta programmet")
    print("CAPS. Testa")
    val = input("Välj ett alternativ i menyn: ")
    if val == "öäå":
        print("Du valde alternativ 1")
        input("Tryck på valfri tangent för att gå tillbaka till menyn.")
    elif val == "2":
        print("Du valde alternativ 2!")
        input("Tryck på valfri tangent för att gå tillbaka till menyn.")
    elif val == "3":
        print("Programmet avslutas.")
        exit()
    elif val == "CAPS":
        print("Python är Case sensitive")
    else:
        print("Ogiltigt val, försök igen.")
