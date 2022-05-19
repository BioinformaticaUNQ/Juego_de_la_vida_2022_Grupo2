from questions import quiz
import utils
import random


def begin(mode):

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
        utils.clear()

        handle_question(question, remaining_attempts, correct_answers, multiplier)        
        
        if not utils.get_confirmation_for("\n¿Siguiente pregunta? Si/No "):
            break

    if correct_answers[0] > len(quiz) / 2:
        print(f"¡Bien, tu puntuacion alcanzada es de {correct_answers[0] * multiplier} puntos!")
    else:
        print(f"Mmm... Mas suerte la proxima. Tu puntuacion alcanzada es de {correct_answers[0] * multiplier} puntos.")

def handle_question(question, remaining_attempts, correct_answers, multiplier):
    ask_question(question, remaining_attempts, correct_answers, multiplier)
    print("\n🧐 Explicacion: {}".format(quiz[question]["explanation"]))
    print("\n🌍 Mas info aca: {}".format(quiz[question]["reference"]))


def ask_question(question_number, remaining_attempts, correct_answers, multiplier):
    while remaining_attempts > 0:

        print(quiz[question_number]["question"] + "\n")

        option_enum = 1
        for option in quiz[question_number]["options"]:
            print(f"🔸 {option_enum}. {option}")
            option_enum += 1

        answer = 0

        while not (0 < answer < len(quiz[question_number]["options"]) + 1):
            try:
                answer = int(input("\nTu respuesta: "))
                if answer > len(quiz[question_number]["options"]):
                    print("Ingresa un valor numerico tal como lo indica la lista")
            except ValueError:
                print("Ingresa un valor numerico tal como lo indica la lista")

        if quiz[question_number]["options"][answer - 1] == quiz[question_number]["answer"]:
            correct_answers[0] += 1
            print(f"\n⭕ Correcto! {correct_answers[0] * multiplier} acumulados hasta ahora.")
            break

        remaining_attempts -= 1

        print("\n❌ Nop, incorrecto.")

        if remaining_attempts > 0:
            print(f"Te quedan {remaining_attempts} intento(s).")
            clue = random.choice(quiz[question_number]["clues"])
            print(f"Pista: {clue}\n")
    