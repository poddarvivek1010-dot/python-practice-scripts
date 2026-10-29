first_name = 'Taylor'
last_name = 'Swift'

full_name = first_name + ' ' + last_name
address = 'States of New York'
address += ', Building number 10'
employee_age = 27

employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)

experience_years = 2
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

position = 'Junior Python Developer'
salary = 45000

employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: INR {salary}'
print(employee_card)

employee_code = 'DEV-2026-CS-004'
department = employee_code[0:3]
print(department)

year_code = employee_code[4:8]
print(year_code)

initials = employee_code[9:11]
print(initials)

last_three = employee_code[-3:]
print(last_three)
