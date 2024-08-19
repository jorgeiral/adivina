import random

def juego_adivina():
    numeroSecreto=random.randint(1,100)
    intentos=0
    adivinado=False
    print("Bien venido al juego")
    print("debes adivinar un número entre 1-100")
    print("¡Intentos a adivinar!")

    while not adivinado:
        adivinanza=input("Introduzca un número entre 1 al 100:")

        if adivinanza.isdigit():
            adivinanza=int(adivinanza)
            intentos +=1

            if adivinanza<numeroSecreto:
                print(f"El número es mayor {adivinanza}")
            elif adivinanza>numeroSecreto:
                print(f"El número es menor {adivinanza}")
            else:
                print(f"Felicitaciones has ganado el número {adivinanza} lo ha logrado {intentos} intentos.") 
        else: 
              print("Por favor intyroduzca un número válido")
              juego_adivina()