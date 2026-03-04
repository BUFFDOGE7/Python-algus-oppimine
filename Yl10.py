name = input("What is your name? ")
print(f"Hello, {name}! Nice to meet you.")

residence = input("Where do you live? ")
if residence.lower() == "saaremaa":
    print("Saaremaa! Such a beautiful island with lots of nature!")

age = int(input("How old are you? "))

if age < 18:
    print("You are too young to drive a car.")
elif age == 18:
    print("Congratulations on coming of age!")
else:
    print("You can drive a car.")