#March 21, 2024
#Final Project

import math

# Calculate the area of a circle
def calculate_area_circle(radius):
    return math.pi * (radius ** 2)

# Solve a quadratic equation
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2

# Calculate the volume of a sphere
def calculate_volume_sphere(radius):
    return (4/3) * math.pi * (radius ** 3)

def main():
    while True:
        print("\nWelcome to the Math Helper. These are the options:")
        print("1. Calculate area of a circle")
        print("2. Solve a quadratic equation")
        print("3. Calculate volume of a sphere")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            radius = float(input("Enter the radius of the circle: "))
            print("Area of the circle:", round(calculate_area_circle(radius),2))
        elif choice == '2':
            a = float(input("Enter coefficient a: "))
            b = float(input("Enter coefficient b: "))
            c = float(input("Enter coefficient c: "))
            print("Roots of the quadratic equation:", solve_quadratic(a, b, c))
        elif choice == '3':
            radius = float(input("Enter the radius of the sphere: "))
            print("Volume of the sphere:", round(calculate_volume_sphere(radius),2))
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
