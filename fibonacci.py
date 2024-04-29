# def Fibonacci(n):
#     if n<=0:
#         print("Incorrect input")
#     elif n == 1:
#         return 0
#     elif n ==2:
#         return 1
#     else:
#         return Fibonacci(n-1)+Fibonacci(n-2)
# print(Fibonacci(10))

# import math

# def isPerfectSquare(x):
#     s = int(math.sqrt(x))
#     return s * s == x

# def isFibonacci(n):
#     return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

# # Test the function
# num = int(input("Enter a number to check if it's a Fibonacci number: "))
# if isFibonacci(num):
#     print(num, "is a Fibonacci number.")
# else:
#     print(num, "is not a Fibonacci number.")




# a = 0
# b = 1
# num = int(input("enter a no"))
# if num == 1:
#     print(a)
# else:
#     print(a)
#     print(b)
#     for i in range(2,num):
#         c = a+b
#         a = b
#         b = c
#         print(c)
#Python Program for Sum of squares of first n natural numbers




# n = int(input("Enter a no: "))
# sum = 0
# for i in range(1,n+1):
#     sum += i*i*i
# print(sum)


# def largest(arr,n):
#     max = arr[0]
#     for i in range(1,n):
#         if arr[i]>max:
#             max = arr[i]
#     return max
# arr = [10,233,43,5423,0]
# n = len(arr)
# ans = largest(arr,n)
# print("Largest in given array", ans)

