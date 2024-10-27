import subprocess
import sys

def kör_git_kommando(kommando):
    try:
        resultat = subprocess.run(kommando)
        return resultat.stdout
    except Exception as error:
        return f"Ett fel uppstod: {error}"

def öppna_versions_fil():
    with open("Kod1016/release.txt", "r") as fil:
        currentVersion = fil.read()
        currentVersion = currentVersion.split(".") # ["1", "0", "0"]
        newVersion = int(currentVersion[0]) + 1
        return f"{newVersion}.0.0"

def spara_versions_fil(version):
    with open("Kod1016/release.txt", "w") as fil:
        fil.write(version)

if __name__ == "__main__":
    input_PAT = sys.argv[1]

    version = öppna_versions_fil()
    print(f"Nuvarande version: {version}")

    spara_versions_fil(version)

    print(f"Kör 'branch release-{version}':")
    kör_git_kommando(f"git checkout -b release-{version}")

    print(f"Kör 'git add release.txt':")
    kör_git_kommando(f"git add Kod1016/release.txt")

    print(f"Kör git commit -m 'Uppdaterat version till {version}':")
    kör_git_kommando(f"git commit -m \"Skapat release branch\"")

    output = kör_git_kommando(f"git push https://felroo:{input_PAT}@github.com/felroo/DemoRepoPython.git release-{version}")
    print(output)