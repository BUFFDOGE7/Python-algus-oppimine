
print("Multiplication table for 8:")
print("-" * 20)
for i in range(13):
    print(f"8 x {i} = {8 * i}")

print("\n" + "=" * 40 + "\n")

x = int(input("Enter a number for the multiplication table: "))
print(f"\nMultiplication table for {x}:")
print("-" * 20)
for i in range(13):
    print(f"{x} x {i} = {x * i}")