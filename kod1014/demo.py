
#------------------------------------------------------------------------

namn_lista = ["felix", "Tarique", "Ali", "Muhammad"]

#Öppna (eller skapa) en textfil och skriv till den
with open("namn.txt", "w") as fil:
    for namn in namn_lista:
        fil.write(namn + "\n")

print("Textfil skapad och sparad.")

#------------------------------------------------------------------------

import json

person = {
    "namn": "Anna",
    "ålder": 28,
    "intressen": ["Läsning", "Fotboll", "Musik"]
}

#Öppna (eller skapa) en json-fil och skriv till den
with open("person_info.json", "w") as fil:
    json.dump(person, fil, ensure_ascii=False, indent=4)

print("JSON-fil skapad och sparad.")

#------------------------------------------------------------------------

path = r'C:\Repos\DemoRepoPython\kod1014\test.txt'

with open(path, "r") as fil:
    innehall = fil.read()

print(innehall)

#------------------------------------------------------------------------

with open("namn.txt", "r") as fil:
        for rad in fil:
            print(rad.strip())

#------------------------------------------------------------------------

import json

with open('filnamn.json', 'r') as fil:
    data = json.load(fil)

print(data)

#------------------------------------------------------------------------

try:
    with open("namn.txt", "r") as fil:
        innehall = fil.read()
        print(innehall)
except FileNotFoundError:
    print("Filen kunde inte hittas. Kontrollera att filnamnet är korrekt.")
except OSError:
    print("Ett fel uppstod vid läsningen av filen.")
except Exception as e:
    print(f"Ett oväntat fel uppstod: {e}")


