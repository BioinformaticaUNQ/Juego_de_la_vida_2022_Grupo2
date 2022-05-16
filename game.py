from audioop import mul
from questions import quiz
import utils
import random


def begin(mode=1):

    correct_answers = [0]
    remaining_attempts = 0
    multiplier = 0

    match mode:
        case 1:
            remaining_attempts = 3
            multiplier = 10
        case 2:
            remaining_attempts = 2
            multiplier = 15
        case 3:
            remaining_attempts = 1
            multiplier = 20

    for question in quiz:
        ask_question(question, remaining_attempts, correct_answers, multiplier)

        explanation = quiz[question]["explanation"]
        print(f"\n🧐 Explicacion: {explanation}")
        reference = quiz[question]["reference"]
        print(f"🌍 Mas info aca: {reference} \n")

        next_question = input("¿Siguiente pregunta? Si/No ")
        if next_question.lower() in ["s", "si"]:
            continue
        elif next_question.lower() in ["n", "no"]:
            break
        else:
            print('Escribe "si" o "no" o Ctrl + C en caso extremo')

    if correct_answers[0] > len(quiz) / 2:
        print(f"¡Bien, tu puntuacion alcanzada es de {correct_answers[0] * multiplier} puntos!")
    else:
        print(f"Mmm... Mas suerte la proxima. Tu puntuacion alcanzada es de {correct_answers[0] * multiplier} puntos")


def ask_question(question_number, remaining_attempts, correct_answers, multiplier):
    utils.clear()
    while remaining_attempts > 0:
        print(quiz[question_number]["question"])

        option_enum = 1
        for option in quiz[question_number]["options"]:
            print(f"🔸 {option_enum}. {option}")
            option_enum += 1

        answer = 0
        while not (0 < answer < len(quiz[question_number]["options"]) + 1):
            try:
                answer = int(input("\nTu respuesta:"))
                if answer > len(quiz[question_number]["options"]):
                    print("Ingresa un valor numerico tal como lo indica la lista")
            except ValueError:
                print("Ingresa un valor numerico tal como lo indica la lista")

        if quiz[question_number]["options"][answer - 1] == quiz[question_number]["answer"]:

            correct_answers[0] += 1
            print(
                f"\n⭕ Correcto! {correct_answers[0] * multiplier} acumulados hasta ahora."
            )

            break

        remaining_attempts -= 1

        print("❌ Nop, incorrecto.")

        if remaining_attempts > 0:
            print(f"Te quedan {remaining_attempts} intento(s).")
            clue = random.choice(quiz[question_number]["clues"])
            print(f"Pista: {clue}\n")
