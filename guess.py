import random
number=random.randint(1,10)
guess=int(input("guess the number 1-10: "))
if(guess==number):
    print("correct")
else:
    print("wrong the number is",number)
