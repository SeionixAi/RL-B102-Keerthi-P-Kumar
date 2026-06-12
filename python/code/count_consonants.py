def count_consonents(text):
    vowels = "aeiou"
    count = 0
    for char in text:
        if char.isalpha() and char.lower() not in vowels:
            count += 1
    return count

print(count_consonents("Hello World"))
