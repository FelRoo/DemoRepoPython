#TestaExceptions
def dela():
    try:
        tal1 = int(input("Ange ett tal: "))
        tal2 = int(input("Ange ett annat tal: "))
        resultat = tal1 / tal2
        print(f"Resultatet är: {resultat}")
    except Exception as error:
        print(f"Fel: {error}.")

def kör_dela():
    try:
        dela()
    except Exception as error:
        print(f"Fel: {error}.")
        dela()

#-------------------------------------------------

class MittEgetFel(Exception):
    pass
#-------------------------------------------------
def kontrollera_positivt(tal):
    if tal < 0:
        raise MittEgetFel("Värdet är negativt!")
    else:
        print(f"{tal} är ett positivt tal.")
#-------------------------------------------------
try:
    kontrollera_positivt(-5)
except MittEgetFel as egetFel:
    print(f"Nu kastades {egetFel}")

#-------------------------------------------------


import subprocess

def kör_git_kommando(kommando):
    try:
        # Kör git-kommandot med subprocess
        resultat = subprocess.run(kommando)
        return resultat.stdout
    except Exception as error:
        return f"Ett fel uppstod: {error}"

print("Kör 'git status':")
output = kör_git_kommando("git status")
print(output)

#-------------------------------------------------