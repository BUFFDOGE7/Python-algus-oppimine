import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"\nCircle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")