"""
Write a function that print all the factors of a number entered by user.
"""
def Num_Of_Fact():
    num = int(input("enter a number :- "))
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
Num_Of_Fact()