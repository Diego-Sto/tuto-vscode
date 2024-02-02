import random

palabras = ['gato', 'perro', 'elefante', 'jirafa', 'rinoceronte', 'leon', 'Sapo', 'hormiga', 'caballo', ]

palabra_secreta = random.choice(palabras)
palabra_oculta = "_" * len(palabra_secreta)

intentos = 0
letras_adivinadas = []
while intentos < 6:

    letra = input("Ingresa una letra: ")
    if letra in letras_adivinadas:
        print("Ya adivinaste esa letra, ¡intenta otra!")
    elif letra in palabra_secreta:
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == letra:
                palabra_oculta = palabra_oculta[:i] + letra + palabra_oculta[i+1:]
        print("¡Bien hecho! La palabra es:", palabra_oculta)
        if "_" not in palabra_oculta:
            print("¡Felicidades, adivinaste la palabra!")
            print("¡Sigue asi vas muy bien! :)")
            break
    else:
        intentos += 1
        print("Letra incorrecta, te quedan", 6-intentos, "intentos.")
        letras_adivinadas.append(letra)
        if intentos == 1:
            print("  O")
            print("¡Pucha empezamos mal causa!")
        elif intentos == 2:
            print("  O")
            print("  |")
            print("¡Concentrate pue wueon!")
        elif intentos == 3:
            print("  O")
            print(" /|")
            print("¡Ya, dejame morir!")
        elif intentos == 4:
            print("  O")
            print(" /|\\")
            print("¡No era enserio wueon!")
        elif intentos == 5:
            print("  O")
            print(" /|\\")
            print(" /")
            print("¡Ultimo intento, piensalo bien conchatumare!")
        elif intentos == 6:
            print("  O")
            print(" /|\\")
            print(" / \\")
            print("Lo siento, no adivinaste la palabra. La palabra era", palabra_secreta, "¡PENDEJO!")
            print("Debes hacer un intento de nuevo cierra la consola eh intentalo otravez")
            
            break
        