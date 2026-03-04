
user_input = input("Enter a string: ")

trimmed_string = user_input.strip()

if len(trimmed_string) < 7:
    print("Error: String must have at least 7 symbols.")
elif len(trimmed_string) % 2 == 0:
    print("Error: String must have an odd number of symbols.")
else:
    middle_index = len(trimmed_string) // 2
    three_middle = trimmed_string[middle_index - 1:middle_index + 2]
    print(f"The three middle symbols are: {three_middle}")