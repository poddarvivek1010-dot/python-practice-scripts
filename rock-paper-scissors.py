#rock, paper, scissors Game
import random

def play_game():
  options = ["rock", "paper", "scissors"]
  player = input("Choose rock, paper, or scissors: ").lower().strip()

  if player not in options:
    print("invalid choice. Please type rock, paper, or scissors")
    return

  computer = random.choice(options)

  if player == computer:
    result = "it's a tie!"
  elif (
      (player == "rock" and computer == "scissors")
      or (player == "paper" and computer == "rock")
      or (player == "scissors" and computer == "paper")
  ):
    result = "you win!"
  else:
    result = "computer wins!"

  print(f"you chose: {player} | computer chose: {computer} --> {result}")

play_game()
