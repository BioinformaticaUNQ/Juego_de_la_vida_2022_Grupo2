from questions import quiz

score = 0

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

            score += 1
            print(f"Correct!\nCurrent score: {score}")
            break
        
        remaining_attempts -= 1

        print(f"Nope, wrong answer. \nYou have {remaining_attempts} attempts left.")

print(f"Final score: {score}")