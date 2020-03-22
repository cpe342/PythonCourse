with_vowels = "This is so much fun!"

without_vowels=''.join(char for char in with_vowels if char not in "aeiou")
print(with_vowels)
print(without_vowels)