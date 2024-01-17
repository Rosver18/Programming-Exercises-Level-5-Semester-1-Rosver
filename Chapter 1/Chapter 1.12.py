import math

def area_of_square():
    sidelength = float(input("Input the side length of the square: "))
    area = sidelength ** 2
    print(f"Area of the square is: {area}")

def area_of_circle():
    radius = float(input("Input the radius of the circle: "))
    area = math.pi * (radius ** 2)
    print(f"Area of the circle is: {area}")

def area_of_triangle():
    base = float(input("Input the base length of the triangle: "))
    height = float(input("Input the height of the triangle: "))
    area = 0.5 * base * height
    print(f"Area of the triangle is: {area}")

menu_options = {
    '1': area_of_square,
    '2': area_of_circle,
    '3': area_of_triangle,
    '4': exit
}

while True:
    print("\nCalculation Menu:")
    print("1: Area of a square")
    print("2: Area of a circle")
    print("3: Area of a triangle")
    print("4: Quit")

    choice = input("Enter your choice (1-4): ")

    selectoption = menu_options.get(choice)
    if selectoption:
        selectoption()
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")