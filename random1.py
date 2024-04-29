import random
target = random.randint(1,100)
while True:
    userchoice = int(input("Guess the target :"))
    if(userchoice == target):
        print("success: correct guess")
        break
    elif(userchoice < target):
        print("Your number was to small. Take a bigger guess")
    else:
        print("Your number was too big. Take a smaller guess..")
print("------GAME OVER------")