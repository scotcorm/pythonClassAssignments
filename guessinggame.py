import random

print("-----------------")
print("M&M Guessing Game")
print("-----------------")

mm_count = random.randint(1, 100)
attempt_limit = 5
attempts = 0

print("Guess the number of M&Ms in the jar and receive a prize!")
print()

while attempts < attempt_limit:
    guess_text = input("How many M&Ms are in the jar? ")
    guess = int(guess_text)
    attempts += 1

    if mm_count == guess:
        print(f"You win a free lunch! It was {guess}")
        break
    elif guess < mm_count:
        print("Sorry, that's too low!")
    else:
        print("That's too high!")

print(f"Bye, you're done in {attempts} tries!")
