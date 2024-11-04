current_year = 2024

def calculate_age(birth_year):
    return current_year - int(birth_year)

age = calculate_age(1999)
print(f"Function returned {age}.")

def print_age(birth_year):
    print(f"Your age is {calculate_age(birth_year)}.")

print_age(1997)