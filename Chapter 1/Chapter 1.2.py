num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum_result = num1 + num2
diff = num1 - num2
product = num1 * num2

if num2 != 0:
    quotient = num1 / num2
    remainder = num1 % num2
else:
    quotient = "Not Possible"
    remainder = "Not Possible"

print(f"Sum (+): {sum_result}")
print(f"Diff (-): {diff}")
print(f"Product (x): {product}")
print(f"Quotient (/): {quotient}")
print(f"Remainder (%): {remainder}")