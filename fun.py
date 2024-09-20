import random
import os
import time as t

def random_number():
    random_numbers = random.randint(1, 10)
    a = int(input("[Choose Number between 1 to 10]: "))
    if a == random.randint(1, 10):
        print("Congratulations! You Got It. The number was:", random_numbers)
    else:
        print("Sorry, the number was:", random_numbers)

def rockandpaperscirros():
    print("Choose Your Option")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Cirrus")
    a = input("[Choose]>")
    b = random.randint(1, 4)
    if a == "1":
        if b == 1:
            print("Draw!")
        elif b == 2:
            print("You Lose!")
        else:
            print("You Win!")
    elif a == "2":
        if b == 1:
            print("You Win!")
        elif b == 2:
            print("Draw!")
        else:
            print("You Lose!")
    elif a == "3":
        if b == 1:
            print("You Lose!")
        elif b == 2:
            print("You Win!")
        else:
            print("Draw!")
    elif a == "4":
        if b == 1:
            print("Draw!")

def guesword():
    word = ["Gemcast","Username","Password"]
    random_word = random.choice(word)
    guess_word = ""
    while guess_word!= random_word:
        guess_word = input(f"Guess the word ({len(random_word)} letters): ")
        if guess_word == random_word:
            print("Congratulations! You Win!")
        elif len(guess_word) < len(random_word):
            print("Too short!")
        else:
            print("Too long!")

while True:
    t.sleep(2)
    os.system("cls")
    print("Choose To Play That game")
    print("1. Guess Number")
    print("2. Rps")
    print("3. guess the word")
    a = input("[Choose]>")
    if a == "1":
        random_number()
    elif a == "2":
        rockandpaperscirros()
    elif a == "3":
        guesword()
