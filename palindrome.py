# A palindrome is a word, phrase, number, or sequence of characters that reads the same forward and backward
#Create a function is_palindrome(word) that returns True if a given word is a palindrome (reads the same backward) and False otherwise.
def is_palindrome(word):
    # Clean the word by removing spaces and converting to lowercase
    cleaned_word = word.replace(" ", "").lower()

    # Check if the cleaned word is the same when reversed
    if cleaned_word == cleaned_word[::-1]:
        print(f"{word} is a palindrome.")
        return True
    else:
        print(f"{word} is not a palindrome.")
        return False


# Testing the function
word_to_check = "level"
is_palindrome(word_to_check)

def is_palindrome(word):
    cleaned_word = word.replace("","").lower()
    if cleaned_word == cleaned_word[::-1]:
        print (f"{word} is a palindrome.")
        return True
    else:
        print (f"{word} is not a palindrome.")
        return False

word_to_check= "A mad man"
is_palindrome(word_to_check)
