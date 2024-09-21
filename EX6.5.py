numbers = []

while True:
    user_input = input("Enter a number: ")

    if user_input.lower() == 'done':
        break

    try:

        number = float(user_input)
        numbers.append(number)
    except ValueError:

        print("Invalid input. Please enter a valid number.")


if numbers:
    print("Maximum value:",  max(numbers))
    print("Minimum value:", min(numbers))
else:
    print("No valid numbers were entered.")
