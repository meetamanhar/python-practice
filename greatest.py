#WAP to find the greatest of 3 numbers entered by the user
num1 = int(input("Enter first no"))
num2 = int(input("Enter second no"))
num3 = int(input("Enter third no"))
num4 = int(input("Enter forth no"))
if(num1 >= num2 and num1>=num3):
    if(num1>=num4):
        print("num1 is largest")
elif(num2>=num3 and num2>=num4):
        print("num2 is largest")
elif(num3>=num4 and num3>=num1):
        print("num3 is largest")
else:
        print("num4 is largest")
