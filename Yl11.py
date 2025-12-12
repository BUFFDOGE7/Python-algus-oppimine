
pet = input("Enter a pet: ")

print(f"First letter of your pet: {pet[0]}")

animals = ["dog", "cat", "bird"]

animals.append(pet)

print(f"List of pets: {animals}")

last_pet = animals[-1]
last_letter = last_pet[-1]
print(f"Last letter of the last element: {last_letter}")