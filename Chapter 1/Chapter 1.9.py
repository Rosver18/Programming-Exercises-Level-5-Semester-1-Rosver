number_list = [10, 2, 7, 11, 12, 4, 7, 9, 5, 8]

print("List of numbers:")
print(*number_list, sep=" ")

highest = max(number_list)
lowest = min(number_list)
print(f"\nHighest number in the list: {highest}")
print(f"Lowest number in the list: {lowest}")

number_list.sort()
print("\nSorted in Ascending Order:")
print(*number_list, sep=" ")

number_list.sort(reverse=True)
print("\nSorted in Descending Order:")
print(*number_list, sep=" ")

number_list.extend([1, 15])

print("\nList after being updated:")
print(*number_list, sep=" ")