import random

palabras = ["musica", "girasoles", "arquitectura", "atardecer", "futbol"]
palabra = random.choice(palabras)
vidas = 6
letras_adivinadas = []
letras_incorrectas = []

while vidas > 0:
    print("\n" + "-"*30)
    mostrar = ""
    for letra in palabra:
        mostrar += letra + " " if letra in letras_adivinadas else "_ "
    print("Palabra:", mostrar.strip())
    print("Vidas:", vidas)
    print("Letras incorrectas:", ", ".join(letras_incorrectas)) 

    if all(letra in letras_adivinadas for letra in palabra):
        print("\n ¡Ganaste! La palabra era:", palabra)
        break

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

if vidas == 0:
    print("\n ¡Perdiste! La palabra era:", palabra)