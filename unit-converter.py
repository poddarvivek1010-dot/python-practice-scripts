# temperature & Distance Converter
def c_to_f(c):
  return (c * 9 / 5) + 32

def f_to_c(f):
  return (f - 32) * 5 / 9

def km_to_miles(km):
  return km * 0.621371

def miles_to_km(miles):
  return miles / 0.621371

conversions = {
    "1": ("celsius -> fahrenheit", "°F", c_to_f),
    "2": ("fahrenheit -> celsius", "°C", f_to_c),
    "3": ("kilometers -> miles", "miles", km_to_miles),
    "4": ("miles -> kilometers", "km", miles_to_km),
}


def main():
  print("<<<<<< Interactive unit converter >>>>>>")
  while True:
    print(
        "\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n3. Kilometers"
        " to Miles\n4. Miles to Kilometers\nq. Quit"
    )
    choice = input("Select an option: ").strip().lower()

    if choice == "q":
      print("Goodbye!!")
      break
    if choice not in conversions:
      print("Invalid option. Please choose 1-4 or q.")
      continue

    raw_val = input("enter value to convert: ").strip()
    try:
      value = float(raw_val)
    except ValueError:
      print("please enter a valid number.")
      continue

    label, unit, func = conversions[choice]
    result = func(value)
    print(f"{label}: {result:.2f} {unit}")


if __name__ == "__main__":
  main()
