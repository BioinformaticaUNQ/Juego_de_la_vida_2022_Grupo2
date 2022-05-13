import os
from questions import quiz

clear = lambda: os.system("cls")
clear()

correct_answers = 0

for question in quiz:

    remaining_attempts = 3

    while remaining_attempts > 0:

        print(quiz[question]['question'])

        option_enum = 1
        for option in quiz[question]['options']:            
            print(f"🔸 {option_enum}. {option}")
            option_enum += 1

        answer = int(input("Your answer: "))
        
        if 0 < answer <= len(quiz[question]['options']) and quiz[question]['options'][answer - 1] == quiz[question]['answer']:

            correct_answers += 1
            print(f"Correct! You got {correct_answers} correct answers so far.")
            break
        
        remaining_attempts -= 1

        print(f"Nope, wrong answer. \nYou have {remaining_attempts} attempts left.")

if correct_answers > len(quiz) / 2:
    print(f"Good, you got {correct_answers} of {len(quiz)} correct!")
else:
    print(f"Mmm... You got {correct_answers} of {len(quiz)} correct.")

