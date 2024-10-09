class bil:

    def __init__(self, model, färg):
        self.model = model
        self.färg = färg

    def __str__(self) -> str:
         pass

min_bil = bil("Volvo", "röd")
print(min_bil.model)

