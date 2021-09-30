import random

for x in range(1):
    list_of_letters=["abc","def","ghi","jkl","mno","pqr"]
    list_of_letters1=["ABC","DEF","EFNO","43453"]
    list_of_numbers=["123","345","567","789"]

    x=input("Would you like to generate a password: ")
    if(x=="yes"):
        print(random.choice(list_of_letters[0:-1])+random.choice(list_of_letters1[0:-1])+random.choice(list_of_numbers))
    else:
        break
    
