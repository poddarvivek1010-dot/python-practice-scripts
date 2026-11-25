
import string

def check_password(password):
  score = 0
  if len(password) >= 8:
    score += 1
  if any(c.isupper() for c in password):
    score += 1
  if any(c.islower() for c in password):
    score += 1
  if any(c.isdigit() for c in password):
    score += 1
  if any(c in string.punctuation for c in password):
    score += 1

  levels = {
      0: "very weak",
      1: "very weak",
      2: "weak",
      3: "medium",
      4: "strong",
      5: "very strong",
  }
  return levels[score]


while True:
  pwd = input("enter a password to check (or 'q' to quit): ")
  if pwd.lower() == "q":
    break
  print("strength:", check_password(pwd))
