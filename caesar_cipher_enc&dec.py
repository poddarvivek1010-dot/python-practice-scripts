# caesar cipher encryptor & decryptor....
def caesar_cipher(text, shift, mode):
  if mode == "decrypt":
    shift = -shift

  result = []
  for char in text:
    if char.isalpha():
      base = ord("A") if char.isupper() else ord("a")
      shifted = (ord(char) - base + shift) % 26 + base
      result.append(chr(shifted))
    else:
      result.append(char)
  return "".join(result)


def main():
  print("<<<<< Caesar cipher encryptor & decryptor >>>>>")
  while True:
    choice = (
        input("\nType 'encrypt', 'decrypt', or 'q' to quit: ").strip().lower()
    )
    if choice == "q":
      print("exiting cipher tool.")
      break
    if choice not in ("encrypt", "decrypt"):
      print("invalid option. Choose among 'encrypt', 'decrypt', or 'q'.")
      continue

    message = input("enter your message: ")
    shift_raw = input("enter shift key (1-25): ").strip()
    if not shift_raw.isdigit():
      print("shift key must be a positive number.")
      continue

    output = caesar_cipher(message, int(shift_raw), choice)
    print(f"result ({choice}ed): {output}")


if __name__ == "__main__":
  main()
