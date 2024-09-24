number1 = int(input("Enter the first number:"))
# print(number1)

operator = input("Enter the operator (+ - * /):")
# print(operator)

number2 = int(input("Enter the second number:"))
# print(number2)

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    result = number1 / number2
else:
    print("ERROR: Cannot recognize the operator!")

print(number1, operator, number2, "=", result)