import larmfil
import time
import psutil

larm_lista = []

def övervakningsläge():
    while True:
        print("övervakningsläge aktivt")
        for larm in larm_lista:
            if larm.typ == "CPU":
                if larm.nivå > psutil.cpu_percent(interval=1):
                    print(f"CPU larm triggat! Larm configurerat på {larm.nivå}")
            if larm.typ == "Disk":
                if larm.nivå > psutil.disk_usage("C:").percent:
                    print(f"Disk larm triggat! Larm configurerat på {larm.nivå}")
            #osv...
        time.sleep(5)


while True:
    print("Vår meny!")
    print("1. Skapa ett larm")
    print("2. Lista alla larm")
    print("3. övervakningsläge")
    print("4. Avsluta")
    val = input("Välj ett alternativ:")

    if val == "1":
        nytt_larm = larmfil.Larm(90,"CPU") #Hårdkodat larm
        larm_lista.append(nytt_larm)
    elif val == "2":
        for larm in larm_lista:
            print(f"larm med nivå {larm.nivå} och typ {larm.typ}")
    elif val == "3":
        print("hej")
    elif val == "4":
        exit()
    else:
        print("felaktigt val, försök igen")
