def is_anagram(text1, text2):
    text1 = text1.lower()
    text2 = text2.lower()
    sorted_text1 = sorted(text1)
    sorted_text2 = sorted(text2)
    if sorted_text1 == sorted_text2:
        return True
    else:
        return False

print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))

    