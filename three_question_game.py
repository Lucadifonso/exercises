print("Welcome to my computer quiz")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's play!!")
score = 0

# question 1
answer= input("What does CPU stand for? ").lower()
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# question 2
answer= input("What does GPU stand for? ").lower()
if answer.lower() == "graphic processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# question 3
answer= input("What does RAM stand for? ").lower()
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print()
print(f"You got {score} question/s right")
print(f"You got {score/4}% right")

