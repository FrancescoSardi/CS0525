print(f"Calcolatore di perimetri delle seguenti figure geometriche: Quadrato, Rettangolo, Cerchio \n")

print()

print("Digita 1 per calcolare il perimetro del quadrato \n")
print("Digita 2 per calcolare il perimetro del cerchio \n")
print("Digita 3 per calcolare il perimetro del rettangolo \n")
print("Digita 4 per usciredal calcolatore \n")


scelta =input(f"Fai la tua scelta: \n")



if scelta == "1":

        
        lato = float(input("Inserisci il lato \n"))

        perimetro = lato * 4 

        print(f"Il perimetro del quadrato è di: {perimetro}")
        
elif scelta == "2":

        raggio = float(input("Inserisci il raggio: \n"))

        circ = raggio * 2*(3.14)

        print(f"La circonferenza del cerchio è di: {circ}")

elif scelta =="3":

        base = float(input("Inserisci base: \n"))

        altezza = float(input("Inserisci altezza: \n"))

        perimetro = (base *2) + ( altezza * 2)

        print(f"Il perimetro del rettangolo è di: {perimetro}")

elif scelta =="4":

        print("Sei uscito dal calcolaore \n")

else: 

        print("La figura non esiste")

