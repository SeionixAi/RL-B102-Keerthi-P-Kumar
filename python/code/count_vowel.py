def count_vowel(text):
    vowel_count = 0
    text = text.lower()
    for char in text:
        if char in "aeiouAEIOU":
            vowel_count += 1
    return vowel_count

print(count_vowel("Hello World"))