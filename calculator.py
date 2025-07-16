# A simple calculator
print('''1.Addition
2. Subtraction
3. Multiplication
4. Division
~~~~~~~~~~~~~~~~~~~~~~''')
print("Enter two number to add")
first_number = input("enter your first number\n")
second_number = input("enter your second number\n")
sum = float(first_number) + float(second_number)
print(f"The sum of {first_number}+{second_number} is = {sum:.2f}")

print("SUBTRACTION")
first_number = input("enter your first number\n")
second_number = input("enter your second number\n")
sub = float(first_number) - float(second_number)
print(f"The subtraction of {first_number}-{second_number} is = {sub:.2f}")
print("MULTIPLICATION")
first_number = input("enter your first number\n")
second_number = input("enter your second number\n")
mul =float(first_number) * float(second_number)
print(f"The multiple of {first_number}*{second_number} is = {mul:.2f}")

print("DIVISION")
first_number = input("enter your first number\n")
second_number = input("enter second  number\n")
div = float(first_number) / float(second_number)
print(f"The division of {first_number}/{second_number} is = {div:.2f}")

print("EXPONENTIAL")
first_number = input("enter your first number\n")
second_number = input("enter your second number\n")
expo = float(first_number) ** float(second_number)
print(f"The exponent of {first_number}**{second_number} is = {expo:.2f}")

print("FLOOR DIVISION")
first_number = input("enter your first number\n")
second_number = input("enter second number\n")
floor = float(first_number) // float(second_number)
print(f"The floor of {first_number}//{second_number} is = {floor:.2f}")
