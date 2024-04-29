# n =[1,25,23,56,4,76,6,36,14,1,78]
# def len_fun(n):
#     return(n)
# print(len(n))



def com_interest(p, r, t):
    amount = p * (pow((1 + r / 100), t))
    CI = amount - p
    print("compound interest is", CI)
com_interest(10000, 10.5, 5)
