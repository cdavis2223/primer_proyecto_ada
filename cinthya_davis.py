import random

def repetir_juego():

    
    palabra = random.choice(palabras)
    vidas = 6
    letras_adivinadas = []
    letras_incorrectas = []

    while vidas > 0:
        # print("\n" + "-"*30)
        mostrar = ""
        for letra in palabra:
            mostrar += letra + " " if letra in letras_adivinadas else "_ "
        print("Palabra:", mostrar.strip())
        print("Vidas:", vidas)
        print("Letras incorrectas:", ", ".join(letras_incorrectas)) 

        

        intento = input("Ingresa una letra: ").lower()
        if len(intento) != 1 or not intento.isalpha():
            print("Por favor, ingresa solo una letra.")
            continue

        if intento in letras_adivinadas or intento in letras_incorrectas:
            print("Ya ingresaste esa letra. Intenta con otra.")
            continue

        if intento in palabra:
            letras_adivinadas.append(intento)
        else:
            letras_incorrectas.append(intento)
            vidas -= 1

        if all(letra in letras_adivinadas for letra in palabra):
            print("\n ¡Ganaste! La palabra era:", palabra)
            break

    if vidas == 0:
        print("\n ¡Perdiste! La palabra era:", palabra)

palabras = ["musica", "girasoles", "arquitectura", "atardecer", "futbol"]

while True:
    repetir_juego()
    # repetir_juego()
    # print("\n¡Gracias por jugar!")
    jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
    if jugar_otra_vez == 's':
        print("\n¡Gracias por jugar!")
    else:
        print("¡Gracias por jugar! Hasta la próxima.")
        break
    # print("Por favor, responde con 's' o 'n'.")
    # if jugar_otra_vez == 's':
    #     print("¡Genial! Reiniciando el juego...")
    # else:
    #     print("¡Gracias por jugar! Hasta la próxima.")