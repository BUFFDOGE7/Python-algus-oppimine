def classify_triangle():
    """
    Classifies a triangle based on the lengths of its sides.
    Checks if the triangle can exist and determines if it's scalene, isosceles, or equilateral.
    """
    print("Triangle Classification Program")
    print("-" * 35)
    
    try:
        side1 = float(input("Enter the length of side 1: "))
        side2 = float(input("Enter the length of side 2: "))
        side3 = float(input("Enter the length of side 3: "))
    except ValueError:
        print("Error: Please enter valid numeric values.")
        return
    
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print("Error: All side lengths must be positive numbers.")
        return
    
    if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
        print("\nA triangle with these side lengths cannot exist.")
        print("The sum of any two sides must be greater than the third side.")
        return
    
    print("\nThe triangle exists!")
    
    if side1 == side2 == side3:
        print("Triangle type: Equilateral")
        print("(All three sides are equal)")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("Triangle type: Isosceles")
        print("(Two sides are equal)")
    else:
        print("Triangle type: Scalene (odd-angled)")
        print("(All three sides are different)")

if __name__ == "__main__":
    classify_triangle()