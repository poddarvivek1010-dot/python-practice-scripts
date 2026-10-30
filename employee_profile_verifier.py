# Day 2: Employee Profile Verifier - using String Slicing & Parsing

employee_email = "srkshotout100@git.in"
employee_messy_name = "  shARukH khAN  "
secret_code = "BWD-2026-SRK"

# parsing username using index slicing

position = employee_email.find("@")
username = employee_email[:position]

employee_clean_name = employee_messy_name.strip().title()

valid_format = secret_code.startswith("BWD")
valid_domain = employee_email.endswith(".in")

print(f"The Employee: {employee_clean_name}")
print(f"Parsed Account Username: {username}")
print(f"System Integrity Check (Code Format): {valid_format}")
print(f"Network Security Check (Domain Format): {valid_domain}")
