# num = [12,45,52,65,-64,-74,1,23,99]
num = [-1,-5,-4,-8,-6]

maxi = float("-inf")
for i in num:
    if i > maxi:
        maxi = i
print(f"Maximum num is {maxi}")
