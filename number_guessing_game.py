# guess the correct number 

import random

def play_guesser():
  secret = random.randint(1, 50)
  attempts = 0
  print("Picked a number between 1 and 50. Type 'q' if you want to quit.")

  while True:
    raw = input("Your guess: ").strip().lower()
    if raw == "q":
      print(f"Quit! The number was {secret}.")
      break
    if not raw.isdigit():
      print("Enter a valid number.")
      continue

    guess = int(raw)
    attempts += 1

    if guess < secret:
      print("Too low! try higher...")
    elif guess > secret:
      print("Too high! try lower...")
    else:
      print(f"Congrats!! You got {secret} in {attempts} attempt(s).")
      break


play_guesser()

