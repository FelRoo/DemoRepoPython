# Funktion för att visa huvudmenyn
def visa_meny():
    print("1. str(String)")
    print("2. int(Integer)")
    print("3. bool(Boolean)")
    print("4. float")
    print("5. complex")
    print("6. Avsluta programmet")

def forklara_string():
    print(f"En string är en datatyp som används för att lagra text. Exempel på en string är: 'Hej världen!'")

def forklara_int():
    print(f"En int(integer) är en datatyp som används för att lagra heltal. Exempel på en integer är: 42")

def forklara_bool():
    print(f"En bool(boolean) är en datatyp som används för att lagra sant eller falskt. Värdena är således antingen True eller False")

def forklara_float():
    print(f"En float är en datatyp som används för att lagra decimaltal. Exempel på en float är: 3.14")

def forklara_complex():
    print(f"En complex är en datatyp som används för att lagra komplexa tal. Exempel på en complex är: 1 + 5j")

def avsluta_programmet():
    print("Programmet avslutas.")
    exit()

# Huvudfunktion som kör menyn i en loop
def huvudprogram():
    while True:
        visa_meny()
        val = input("Välj ett alternativ: ")
        if val == "1":
            forklara_string()
            input("Tryck på valfri tangent för att gå tillbaka till menyn.")
        elif val == "2":
            forklara_int()
            input("Tryck på valfri tangent för att gå tillbaka till menyn.")
        elif val == "3":
            forklara_bool()
            input("Tryck på valfri tangent för att gå tillbaka till menyn.")
        elif val == "4":
            forklara_float()
            input("Tryck på valfri tangent för att gå tillbaka till menyn.")
        elif val == "5":
            forklara_complex()
            input("Tryck på valfri tangent för att gå tillbaka till menyn.")
        elif val == "6":
            exit()
        else:
            print("Ogiltigt val, försök igen.")

# Startar huvudprogrammet
print("\nVälkommen till menyn! Förklaring till de grundläggande datatyperna inom Python!")
huvudprogram()

