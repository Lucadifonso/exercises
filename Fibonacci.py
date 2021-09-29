'''
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.

(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''

# Input from user

nterms = int(input("How long you want your Fibonacci sequence to be?"))

n_1 = 0
n_2 = 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")
             
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n_1)
   
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n_1)
       nth = n_1 + n_2
       # update values
       n_1 = n_2
       n_2 = nth
       count += 1

print()
print()
print("Let's see a method using a function now...")
print()
print()

def fibonacci():
    num = int(input("How many numbers that generates?:"))
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib
print(fibonacci())
input()

