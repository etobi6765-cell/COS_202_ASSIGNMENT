def mathematical_calculator():
    print("=" * 45)
    print("      SIMPLE MATHEMATICAL CALCULATOR (MC)    ")
    print("=" * 45)
    print("Available Operations:")
    print(" [+] Add          [-] Subtract     [*] Multiply")
    print(" [/] Divide       [\\] Floor Div    [^] Power")
    print(" [%] Modulo       [C] Clear/Reset  [OFF] Exit")
    print("=" * 45)

    stored_value = None

    while True:
        # If there's an active result, carry it over; otherwise, ask for a new first number
        if stored_value is None:
            user_input = input("\nEnter first number (or type 'OFF' to quit): ").strip()
            if user_input.upper() == 'OFF':
                print("Calculator powering down. Goodbye!")
                break
            try:
                num1 = float(user_input)
            except ValueError:
                print("Error: Invalid number. Please enter numeric digits.")
                continue
        else:
            print(f"\nCurrent value: {stored_value}")
            num1 = stored_value

        # Get the operation
        op = input("Enter operator (+, -, *, /, \\, ^, %, C, OFF): ").strip()

        # Selection controls for quick actions
        if op.upper() == 'OFF':
            print("Calculator powering down. Goodbye!")
            break
        elif op.upper() == 'C':
            print("Screen Cleared.")
            stored_value = None
            continue

        # Get the second number
        user_input2 = input("Enter second number: ").strip()
        try:
            num2 = float(user_input2)
        except ValueError:
            print("Error: Invalid number. Start operation over.")
            continue

        # Selection Control Statements to execute the math operations
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Error: Division by zero is undefined.")
                continue
            result = num1 / num2
        elif op == '\\':
            if num2 == 0:
                print("Error: Integer division by zero is undefined.")
                continue
            result = num1 // num2  # Double slash is floor division in Python
        elif op == '^':
            result = num1 ** num2  # Double asterisk is power/exponent in Python
        elif op == '%':
            if num2 == 0:
                print("Error: Modulo by zero is undefined.")
                continue
            result = num1 % num2
        else:
            print(f"Error: Unknown operator '{op}'")
            continue

        # Print final calculation result and save state
        print(f"Calculation: {num1} {op} {num2} = {result}")
        stored_value = result

if __name__ == "__main__":
    mathematical_calculator()
