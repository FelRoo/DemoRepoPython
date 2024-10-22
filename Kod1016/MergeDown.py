import subprocess
import sys

def kör_git_kommando(kommando):
    try:
        resultat = subprocess.run(kommando)
        return resultat.stdout
    except Exception as error:
        return f"Ett fel uppstod: {error}"

if __name__ == "__main__":
    input_PAT = sys.argv[1]

    print(f"Kör 'git checkout develop':")
    kör_git_kommando(f"git checkout develop")

    print(f"Kör 'git pull origin develop':")
    kör_git_kommando(f"git pull origin develop")

    print(f"Kör 'git merge main':")
    kör_git_kommando(f"git merge main")

    output = kör_git_kommando(f"git push https://felroo:{input_PAT}@github.com/felroo/DemoRepoPython.git develop")
    print(output)