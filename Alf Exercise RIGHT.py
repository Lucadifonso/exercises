'''
how many animals he has
each animal input name and species - if species not supported give an error
for each animal print name, species and human age
'''


print("welcome to 'WHAT IS YOUR PET AGE FOR DUMMIES', just answer some simple questions and you will know the age of your animals")

#how many animals you have


Amount_of_animal = int(input("How many pets do you have:"))
if Amount_of_animal >= 0:
    print ("Wow, you have" , Amount_of_animal, "pets")

keepAsking = True 

while(keepAsking == True):

    stdName = input(" Name: ")
    ageRecord = int(input("Age: "))


    name_array = list()
    age_array = list()      

    name_array.append(stdName)
    age_array.append(ageRecord)

    if Amount_of_animal == Amount_of_animal:
    break

