total = 0
count = 0

while True:
    user_input = input("Enter an integer:")

    if user_input.lower() == 'done':
        break

    try:
        num = int(user_input)
        total += num
        count += 1
    except ValueError:
        print("Invalid input. Please enter an integer.")

if count > 0:
    average = total / count
    print(f"Total: {total}, Count: {count}, Average: {average}")
else:
    print("No valid numbers entered.")





