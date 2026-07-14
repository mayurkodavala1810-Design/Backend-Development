def find_Max(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        print(f"Max number is {n1}")
    elif(n2 > n1 and n2 > n3):
        print(f"Max number is {n2}")
    else:
        print(f"Max number is {n3}")
n1 = int(input("Enter a First num:- "))
n2 = int(input("Enter a First num:- "))
n3 = int(input("Enter a First num:- "))
find_Max(n1,n2,n3)