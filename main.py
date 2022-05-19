import game
import utils

# modo de juego
def main():
    print("¡Hola! Bio_Quiz es un juego en donde te diviertes mientras aprendes conceptos biologicos... o algo asi.\n")
    print("Elige a continuacion una modalidad de juego...\n")
    print("1. Modo facil: Por cada respuesta correcta ganas 10 puntos, pistas para responder, y tres posibilidades por pregunta.")
    print("2. Modo normal: Por cada respuesta correcta ganas 15 puntos, pistas para responder, y una posibilidad para volver por pregunta")
    print("3. Modo dificil: Por cada respuesta correcta ganas 20 puntos, no hay pistas ni segundas oportunidades. ¡Buena suerte!\n")
    
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
    if not utils.get_confirmation_for("¿Que tal otra ronda? Si/No "):
        print("¡Adios!")
        break