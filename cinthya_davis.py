import random

palabras = ["musica", "girasoles", "arquitectura", "atardecer", "futbol"]
palabra = random.choice(palabras)
vidas = 6
letras_adivinadas = []
letras_incorrectas = []

while vidas > 0:
    mostrar = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            mostrar += letra + " "
        else:
            mostrar += "_ "
    print("Palabra:", mostrar.strip())
    print("Vidas:", vidas)
    print("Letras incorrectas:", letras_incorrectas)

    intento = input("Ingresa una letra: ").lower()
    if len(intento) != 1 or not intento.isalpha():
        print("Por favor, ingresa solo una letra.")
        continue

    if intento in palabra:
        letras_adivinadas.append(intento)
    else:
        if intento not in letras_incorrectas:
            letras_incorrectas.append(intento)
            vidas -= 1
