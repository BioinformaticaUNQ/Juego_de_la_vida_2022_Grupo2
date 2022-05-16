import game
import utils

# mensaje incial

# modo de juego
def main():
    print("¡Hola! Bio_Quiz es un juego en donde te diviertes mientras aprendes conceptos biologicos... o algo asi.\n")
    print("Elige a continuacion una modalidad de juego...")
    print("1. Modo facil: Por cada respuesta correcta ganas 10 puntos, pistas para responder, y tres posibilidades por pregunta.")
    print("2. Modo normal: Por cada respuesta correcta ganas 15 puntos, pistas para responder, y una posibilidad para volver por pregunta")
    print("3. Modo dificil: Por cada respuesta correcta ganas 20 puntos, no hay pistas ni segundas oportunidades. ¡Buena suerte!")
    
    game_mode = 0

    while not (0 < game_mode < 4):
        try:
            game_mode = int(input("Modo de juego: "))
        except ValueError:
            print("Ingresa un valor numerico tal como lo indica la lista")

    game.begin(game_mode)


# loop principal
while True:
    utils.clear()
    main()
    answer = input("¿Que tal otra ronda? Si/No ")
    if answer.lower() in ["s","si"]:
        continue
    elif answer.lower() in ["n","no"]:
        print("¡Adios!")
        break
    else:
        print("Escribe \"si\" o \"no\" o Ctrl + C en caso extremo")
