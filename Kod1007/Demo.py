
lista = []

lista.insert(0, "äpple")
lista.insert(0, "kiwi")
lista.insert(len(lista), "päron")
lista.reverse()

print(lista)


#------------------------------------------------------------


my_tuple = (1, 2, 3, "apple", "banana")

# En tuple med bara ett element måste följas av ett kommatecken
one_element_tuple = (5,)

print(my_tuple[0])  # Output: 1

my_tuple[0] = 10  # Detta kommer att orsaka ett TypeError


#------------------------------------------------------------


my_dict = {}

# Skapa en dictionary med nyckel-värde-par
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "Stockholm"
}

print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 25

#------------------------------------------------------------

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(f"{key}: {value}")

#------------------------------------------------------------

keys = my_dict.keys()
print(keys)  # Output: dict_keys(['name', 'city', 'country'])

values = my_dict.values()
print(values)  # Output: dict_values(['Alice', 'Stockholm', 'Sweden'])

items = my_dict.items()
print(items)  # Output: dict_items([('name', 'Alice'), ('city', 'Stockholm'), ('country', 'Sweden')])


#------------------------------------------------------------

class händelse:
    # Klassens konstruktor (initieringsmetod)
    def __init__(self, typ, alvarlighetsgrad):
        self.typ = typ  # Instansattribut
        self.alvarlighetsgrad = alvarlighetsgrad



    # En metod som tillhör klassen
    def information(self):
        return f"händelse av typen {self.typ} med alvarlighetsgrad {self.alvarlighetsgrad}"


händelse.information()
# t.ex. min_lista.append()

#------------------------------------------------------------

#Tomt returvärde

def min_funktion():
    return None

print(min_funktion())  # Output: None


#------------------------------------------------------------


my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "Stockholm"
}

#my_dict.clear()

del my_dict["age"]

print(my_dict)


#------------------------------------------------------------