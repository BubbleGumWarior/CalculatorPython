def add(numberOne, numberTwo):
    return numberOne + numberTwo


def subtract(numberOne, numberTwo):
    return numberOne - numberTwo


def multiply(numberOne, numberTwo):
    return numberOne * numberTwo


def divide(numberOne, numberTwo):
    return numberOne / numberTwo


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        next_calculation = input("Let's do next calculation? (Yes/No): ").capitalize()
        print(next_calculation)
        if next_calculation == "No":
            break

    else:
        print("Invalid Input")
