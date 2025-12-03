import re


input_testo = input("Inserisci testo: ")
input_testo = input_testo.lower()


input_testo = re.sub(r'[^ \w\s]', '', input_testo)

parole = input_testo.split()

numeroparole = {}
parola = []

for parola in parole:
    if parola in numeroparole:
        numeroparole[parola] += 1
    else:
        numeroparole[parola] = 1


print (numeroparole)