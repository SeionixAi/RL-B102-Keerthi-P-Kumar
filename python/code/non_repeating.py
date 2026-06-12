def first_non_repeating_char(text):
    lower_text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    for char in text:
        if char_count[char] == 1:
            return char
    return None

print(first_non_repeating_char("hello world"))