# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1 
# 6 5 4 3 2 1 
# 7 6 5 4 3 2 1 
# 8 7 6 5 4 3 2 1 
# 9 8 7 6 5 4 3 2 1 
# 10 9 8 7 6 5 4 3 2 1 
n = int(input("Enter a num :- "))
10
for i in range(1,n + 1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()