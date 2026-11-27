def convert_base(num_str, from_base):
  decimal_val = int(num_str, from_base)
  return {
      "decimal (base 10)": str(decimal_val),
      "binary (base 2)": bin(decimal_val)[2:],
      "octal (base 8)": oct(decimal_val)[2:],
      "hexadecimal (base 16)": hex(decimal_val)[2:].upper(),
  }


def main():
  bases = {"1": 2, "2": 8, "3": 10, "4": 16}
  while True:
    print(
        "\ninput base: 1) binary  2) octal  3) decimal  4) hexadecimal  q) quit"
    )
    choice = input("select base: ").strip().lower()
    if choice == "q":
      break
    if choice not in bases:
      print("invalid option.")
      continue

    num_str = input("enter number: ").strip()
    try:
      results = convert_base(num_str, bases[choice])
      for label, val in results.items():
        print(f"{label}: {val}")
    except ValueError:
      print("invalid digits for the selected base.")


if __name__ == "__main__":
  main()
