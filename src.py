def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def main():
    operation = input("What operation would you like to perform? (add, subtract, multiply, divide): ")

    if operation == "add":
        first_number = int(input("What is the first number? "))
        second_number = int(input("What is the second number? "))
        print(first_number, " + ", second_number, " = ", add(first_number, second_number))
    elif operation == "subtract":
        first_number = int(input("What is the first number? "))
        second_number = int(input("What is the second number? "))
        print(first_number, " - ", second_number, " = ", subtract(first_number, second_number))
    elif operation == "multiply":
        first_number = int(input("What is the first number? "))
        second_number = int(input("What is the second number? "))
        print(first_number, " * ", second_number, " = ", multiply(first_number, second_number))
    elif operation == "divide":
        first_number = int(input("What is the first number? "))
        second_number = int(input("What is the second number? "))
        print(first_number, " / ", second_number, " = ", divide(first_number, second_number))
    else:
        print("Invalid operation.")

if __name__ == "__main__":
    main()
