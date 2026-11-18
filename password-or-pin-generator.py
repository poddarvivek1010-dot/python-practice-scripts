# Random strong password and numeric PIN generator
import random
import string


def generate_password(length=13):
  if length < 6:
    return "password length must be at least 6 characters."

  letters = string.ascii_letters
  digits = string.digits
  symbols = "!@%$*^*#"
  all_chars = letters + digits + symbols

  # Ensure at least one letter, one digit, and one symbol...
  password = [
      random.choice(string.ascii_uppercase),
      random.choice(string.ascii_lowercase),
      random.choice(digits),
      random.choice(symbols),
  ]

  password += [random.choice(all_chars) for _ in range(length - 4)]
  random.shuffle(password)
  return "".join(password)


def generate_pin(digits_count=6):
  return "".join(random.choice(string.digits) for _ in range(digits_count))


#Sample outputs.....
print("Generated credentials.....")
print("12-Char password :", generate_password(13))
print("16-Char password :", generate_password(17))
print("4-Digit PIN      :", generate_pin(5))
print("6-Digit PIN      :", generate_pin(8))

