#Temperature converter (celsius & fahrenheit)


class TemperatureConverter:

  def __init__(self, celsius):
    self.celsius = celsius

  def to_fahrenheit(self):
    return round((self.celsius * 9 / 5) + 32, 2)

  def to_kelvin(self):
    return round(self.celsius + 273.15, 2)

  def display_all(self):
    print(f"Celsius    : {self.celsius}°C")
    print(f"Fahrenheit : {self.to_fahrenheit()}°F")
    print(f"Kelvin     : {self.to_kelvin()}K")


#Sample conversions...
reading_1 = TemperatureConverter(25)
reading_2 = TemperatureConverter(37)

reading_1.display_all()
print()
reading_2.display_all()
