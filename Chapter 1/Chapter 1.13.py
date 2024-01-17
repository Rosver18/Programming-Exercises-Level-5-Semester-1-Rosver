def calculate_product(lst):
    return 1 if not lst else lst[0] * calculate_product(lst[1:])

numbers = []

while True:
    numinput = input("Add a number to the list, type 'done' if finished: ")

    if numinput.lower() == 'done':
        break
    else:
        try:
            number = int(numinput)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done'.")

result = calculate_product(numbers)

print(f"The product of the list elements is: {result}")
