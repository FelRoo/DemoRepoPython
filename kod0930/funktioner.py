from greeting import greeting

# skriver ut alla tal mellan 1-20 som inte är jämnt delbara med 2 eller 5.
for number in range(1, 21):
    if number % 2 == 0:
        continue 
    elif number % 5 == 0:
        continue
    else:
        print(number)

def addera(tal1,tal2):
    summa = tal1 + tal2
    return summa

def subtrahera(tal1,tal2):
    differens = tal1 - tal2
    return differens

def print_hej(name="felix"):
    print("Hej " + name)

def addera_med_felhantering(tal1: int, tal2: int) -> int:

    if not isinstance(tal1, int) or not isinstance(tal2, int):
        print("Felaktig inmatning")
    else:
        summa = tal1 + tal2
        return summa

greeting("felix") #Tillgänglig i denna filen.