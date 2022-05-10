from questions import quiz

score = 0

for question in quiz:
    remaining_attempts = 3
    while remaining_attempts > 0:
        print(quiz[question]['question'])
        answer = input("Your answer: ")
        if quiz[question]['question'].lower() == answer.lower():
            print(f"Correct! \nCurrent score: {score}")
            score += 1
            break
        remaining_attempts -= 1
        print(f"Nope, wrong answer. \nYou have {remaining_attempts} tries remaining.")

print(f"Final score: {score}")