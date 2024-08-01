#Guessing game using random module
import random as a
def guessgame():
    c=a.randint(1,100)
    count=0
    while(True):
        count=count+1
        n=int(input(f"enter your guess No{count} : "))
        if(n>c):
            print("please enter smaller than",n)
        elif(n<c):
            print("please enter bigger than",n)
        elif(n==c):
            print("your guess is right the number is",c)
            break
        else:
            print("invalid input")
    print(f"you have guessed the number in {count} attempts")