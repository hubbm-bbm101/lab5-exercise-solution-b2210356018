import random
a = random.randint(0,10)
number_of_guesses=0
guess=0
while number_of_guesses<11 and guess != a:
    print("Guess a number between 0 and 10.")
    guess=int(input("Please enter a number."))
    number_of_guesses=number_of_guesses+1
    if guess < a:
        print("This is smaller than the number. Guess bigger.")
    if guess >a:
        print("This is bigger than the number. Guess smaller.")
    if guess == a:
        print("Well done!")
