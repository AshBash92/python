import random

print("""
  _   _                 _                  _____                     _                _____                      
 | \ | |               | |                / ____|                   (_)              / ____|                     
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _  | |  __  __ _ _ __ ___   ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` | | | |_ |/ _` | '_ ` _ \ / _ \\
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| | | |__| | (_| | | | | | |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |  \_____|\__,_|_| |_| |_|\___|
                                                                              __/ |                              
                                                                             |___/                               
""")

print('Welcome to the Number Guessing Game!')

print('I\'m thinking of a number between 1 and 100.')

difficulty = input("\nChoose a difficulty: 'easy' or 'hard'\n").lower()

if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5

number = random.randrange(1,101)

while attempts > 0:
    guess = input("\nGuess a number.\n").lower()

    if int(guess) == number:
        print("You guessed correctly!")
        break
    elif int(guess) > number:
        print("\nToo high. Try again.")
        attempts -= 1
        print(str(attempts) + " atempts left.")
    elif int(guess) < number:
        print("\nToo low. Try again.")
        attempts -= 1
        print(str(attempts) + " attempts left.")