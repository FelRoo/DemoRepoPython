import random

#Lista med namn.
lista = ["felix", "Martin", "Tedros", "Karlos", "David", "Nikola"]

#Slumpar fram 3 namn från listan.
sample = random.sample(lista, 3)

print(sample)

#------------------------------------------------------------

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def globalfunktion():
    # Modifierar global variabel
    global a
    a = [3,4,5]

globalfunktion()

print(a)


#------------------------------------------------------------


mitt_set = set()

mitt_set.add(11)

print(mitt_set)

mitt_andra_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Skapar en ny mängd som innehåller element som inte finns i båda mängderna.
test = mitt_set.difference(mitt_andra_set)

print(test)


#------------------------------------------------------------

#Förslag på lösning för att ta fram grupper av namn.

gruppstorlek = 3
namn_lista = []
temp_lista = []
temp_lista.extend(namn_lista)

for i in range(1, len(temp_lista), gruppstorlek):
    if gruppstorlek > len(temp_lista):
        gruppstorlek = len(temp_lista)
    grupp = random.sample(temp_lista, gruppstorlek)
    for namn in grupp:
        temp_lista.remove(namn)
    print("Grupp: " + grupp)



#------------------------------------------------------------