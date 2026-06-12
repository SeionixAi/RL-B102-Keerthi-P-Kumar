def remove_duplicates(text):
    unique_chars = []
    for char in text:
        if char not in unique_chars:
            unique_chars.append(char)
    return "".join(unique_chars)

print(remove_duplicates("Hello World"))

