# Program to perform basic arithmetic operations: addition, subtraction, multiplication, and division

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing operations
sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2
if num2 != 0:
    div_result = num1 / num2
else:
    div_result = "Undefined (division by zero)"

# Displaying the results
print("\nResults:")
print(f"Addition: {num1} + {num2} = {sum_result}")
print(f"Subtraction: {num1} - {num2} = {diff_result}")
print(f"Multiplication: {num1} × {num2} = {prod_result}")
print(f"Division: {num1} ÷ {num2} = {div_result}")
