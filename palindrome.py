# Ask for input
user_palindrome = input("Please enter a word: ")

# Reverse palindrom_list
reverse_palindrome = user_palindrome.lower()[::-1]

# Print word
print("\nYour word is {}".format(user_palindrome))
print("\nYour word backwards is {}".format(reverse_palindrome))

if user_palindrome.lower() == reverse_palindrome:
    print("\n{} is a palindrome!".format(user_palindrome))

else:
    print("\n{} is not a palindrome".format(user_palindrome))


