#Find tri-angle hypotenuse

from math import sqrt

print("Enter the length")
a = float(input("a : "))
b = float(input("b : "))

c = sqrt(a**2 + b**2)
print(f"The triangle hypotenuse is {c}")