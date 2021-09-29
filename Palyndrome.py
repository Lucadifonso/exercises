'''
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
'''


word = input("What word would you like to test?")


if word == word[::-1]:
    print()
    print("Yes, your world is a palindrome")
    print()
else:
    print()
    print("No, your word is not a palindrome")
    print()

tryagain = input("Do you want to try another word? 'y' for yes or any other letter for no")
               
while tryagain == "y":
    print()
    word = input("What word would you like to test?")
    if word == word[::-1]:
        print()
        print("Yes, your world is a palindrome")
        print()
        tryagain = input("Do you want to try another word? 'y' for yes or any other letter for no")
        
    else:
        print()
        print("No, your word is not a palindrome")
        print()
        tryagain = input("Do you want to try another word? 'y' for yes or any other letter for no")
        
        
if tryagain != "y":
    print()
    print("Ok, I hope you had fun!")
        
