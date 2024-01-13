calculator = True
while calculator:
    print("welcome to the py_calculator")

    first_number = float(input("type the first number= "))
    operation = input("type the operation do you want to do (+,-,*,/)= ")
    second_number = float(input("type the second number= "))

    def calculate(n1, operator, n2):
        if operation == "+":
            return n1 + n2
        elif operation == "-":
            return n1 - n2
        elif operation == "*":
            return n1 * n2
        elif operation == "/":
            return n1 / n2


    solution = calculate(first_number, operation, second_number)
    print(f"{first_number} {operation} {second_number} = {solution}")

    count_continue = True
    while count_continue:
        restart = input("\ndo you want to continue with the result? type 'y or n'  ").lower()

        if restart == "y":
            print("\nfirst_number : ", solution)
            first_number = solution
            operation = input("type the operation do you want to do (+,-,*,/)= ")

            if operation == "+" or operation == "-" or operation == "*" or operation == "/":
                second_number = float(input("type the second number= "))
                solution = calculate(first_number, operation, second_number)
                print(f"{first_number} {operation} {second_number} = {solution}")
            else:
                print("chose the correct operation.")

        elif restart == "n":
            print("Bye")
            count_continue = False

    if input("do you want to exit from calculator? y/n: ").lower() == "y":
        calculator = False






