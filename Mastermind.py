import random
import time

choice = input("Please choose the difficulty of the game.\nEasy \nNormal \nHard\n")


def level(choice):
    if choice.lower() == 'easy':
        x = random.sample(range(0, 10), 3)
    elif choice.lower() == 'normal':
        x = random.sample(range(0, 10), 4)
    elif choice.lower() == 'hard':
        x = random.sample(range(0, 10), 5)
    else:
        print("Invalid number.")
    return x


secret_code = level(choice)
print(f"This is the secret code, you can turn off this function if you want. {secret_code}")

attempts = 1

while attempts <= 5:
    guess = input("Please input your numbers:\n").split()
    matches = 0
    hits = 0

    # Checking the quantity of provided numbers.
    if len(guess) < len(secret_code):
        print("Your list of numbers is shorter then the secret code, please try again.")
        time.sleep(3)
        break
    elif len(guess) > len(secret_code):
        print("Your list of numbers is greater then the secret code, please try again.")
        time.sleep(3)
        break
    else:
        pass
    # Running throw every number in guess list.
    for i in guess:
        if int(i) in secret_code:
            matches += 1
            # Checking if index of i in guess list is matching the index of i in secret_code list
            if guess.index(i) == secret_code.index(int(i)):
                hits += 1

    # Using map() to perform conversion, converting all srt items in guess list to int.
    if list(map(int, guess)) == secret_code:
        print("Congratulations, you have managed to guess all numbers in the secret code.")
        break
    attempts += 1
    print(f"{guess}    Hits =  {hits}    Matches = {matches}")
    if attempts == 6:
        print("Game over")
