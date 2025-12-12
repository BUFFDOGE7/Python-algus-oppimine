
vowels = "aeiouõäöüAEIOUÕÄÖÜ"

vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1

print(f"Text: {text}")
print(f"Number of vowels: {vowel_count}")

vowel_count_alt = sum(1 for char in text if char in vowels)
print(f"Number of vowels (alternative method): {vowel_count_alt}")