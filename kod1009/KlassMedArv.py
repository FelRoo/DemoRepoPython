class Djur:
    def __init__(self, namn):
        self.namn = namn
    def göra_ljud(self):
        return f"{self.namn} gör ett ljud."

class Hund(Djur):
    def göra_ljud(self):
        return f"{self.namn} skäller."

class Katt(Djur):
    def göra_ljud(self):
        return f"{self.namn} jamar."

djur = Djur("Ett djur")
hund = Hund("Rex")
katt = Katt("Misse")

print(djur.göra_ljud())
print(hund.göra_ljud())
print(katt.göra_ljud())