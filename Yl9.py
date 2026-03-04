def classify_triangle():
    a = float(input("Enter side 1: "))
    b = float(input("Enter side 2: "))
    c = float(input("Enter side 3: "))

    if a <= 0 or b <= 0 or c <= 0:
        print("Sides must be positive numbers.")
        return

    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        print("These sides cannot form a triangle.")
        return

    if a == b == c:
        print("Equilateral triangle (all sides equal)")
    elif a == b or b == c or a == c:
        print("Isosceles triangle (two sides equal)")
    else:
        print("Scalene triangle (all sides different)")

classify_triangle()