#the word

def word():
    print("The pride of Africa")
    return input()
# reversed using slicing
def reverseConversion():
    text = word()
    reversed_text = text[::-1]
    print(f"Reversed string (slicing): {reversed_text}")

reverseConversion()
