import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def get_confirmation_for(message):
    while True:
        choice = input(message).lower()
        if choice in ['s', 'si']:
            return True
        elif choice in ['n', 'no']:
            return False
    