import math

print("Benvenuto nel calcolatore supremo cosa vuoi fare?")

def calculate():
    print("1. Addizione")
    print("2. Sottrazione")
    print("3. Moltiplicazione")
    print("4. Divisione")
    print("5. Radice quadrata")

    selezione = int(input("Seleziona una opzione: "))

#Addizione
    if selezione == 1:
        number1 = int(input("Scrivi il primo numero: "))
        number2 = int(input("Scrivi il secondo numero: "))
        number_1 = number1
        number_2 = number2
        addizione = number_1 + number_2 
        print(addizione)
        dinuovo()

#Sottrazione
    elif selezione == 2:
        number1 = int(input("Scrivi il primo numero: "))
        number2 = int(input("Scrivi il secondo numero: "))
        number_1 = number1
        number_2 = number2
        sottrazione = number_1 - number_2
        print(sottrazione)
        dinuovo()

#Moltiplicazione
    elif selezione == 3:
        number1 = int(input("Scrivi il primo numero: "))
        number2 = int(input("Scrivi il secondo numero: "))
        number_1 = number1
        number_2 = number2
        moltiplicazione = number_1 * number_2
        print(moltiplicazione)
        dinuovo()

#Divisione
    elif selezione == 4:
        number1 = int(input("Scrivi il primo numero: "))
        number2 = int(input("Scrivi il secondo numero: "))
        number_1 = number1
        number_2 = number2
        divisione = number_1 / number_2
        print(divisione)
        dinuovo()

#Radice quadrata
    elif selezione == 5:
        number1 = int(input("Scrivi il primo numero: "))
        number_1 = number1
        radice = math.sqrt(number_1)
        print(radice)
        dinuovo()

#Calcolare ancora
def dinuovo():
    selezione = input("Vuoi calcolare ancora?")
    if selezione == 'Y' or selezione == 'y' or selezione == 'yes' or selezione == 'Yes' or selezione == 'YES':
        calculate()

    elif selezione == 'N' or selezione == 'n' or selezione == 'no' or selezione == 'No' or selezione == 'NO':
        print('Ci vediamo!')

calculate()
