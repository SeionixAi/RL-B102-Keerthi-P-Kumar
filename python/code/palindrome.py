def is_palindrome(text):
    text = text.lower()
    text = text.replace(" ", "")
    if text == text[::-1]:
        return True
    else:
        return False
    
text = input("Enter name :")
print(is_palindrome(text))
