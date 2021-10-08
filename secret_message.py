# a - z 97 - 122
# A - Z 65 - 90

My_message = input("enter a string to hide in UPPERCASE : ")
Secret_message = ""

for char in My_message:
    Secret_message += str(ord(char))

print("Secret message is: ", Secret_message)

Secret_message = ""

for i in range(0, len(Secret_message)-1, 2):
    char_code = Secret_message[i] + Secret_message [i + 1]
    My_message += chr(int(char_code))

print("Original Message is: ", My_message)
