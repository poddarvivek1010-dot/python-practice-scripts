# Cinema Ticket Fare Calculator - (booleans and conditionals)

starting_price = 20
age = 21
ticket_type = "Special"
show_timing = "Evening"
is_member = False
is_holiday = False

# Checking eligibility
if age < 18:
    print("Ticket booking failed: Underage restriction.")
    exit()

# Calculating Discounts
discount = 2.5
if is_member and age >= 21:
    discount = 2.5

# Calculating Extra Charges
extra_charges = 0
if show_timing == "Evening" or is_holiday:
    extra_charges = 3

# Calculating Service Charges based on ticket type
service_charges = 0
if ticket_type == "Premium":
    service_charges = 7
elif ticket_type == "Special":
    service_charges = 5
else:
    service_charges = 2

# Calculating final charges
final_price = starting_price + extra_charges + service_charges - discount

print(f"Starting Ticket Price: $ {starting_price}")
print(f"Extra Charges Applied: $ {extra_charges}")
print(f"Service Charges Applied: $ {service_charges}")
print(f"Discount Applied: $ {discount}")
print(f"Final Ticket Price: $ {final_price}")

