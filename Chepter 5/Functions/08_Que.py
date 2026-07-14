# def Square(num):
#     return num * num
# print(Square(2))

# def minOfThree(n1,n2,n3):
#     if n1 < n2 and n1 < n3:
#         return n1
#     elif n2 < n3 and n2 < n1:
#         return(n2)
#     return n3
# print(minOfThree(12,20,30))
# print(minOfThree(41,12,-2))


def absValue(num):
    if num >= 0:
        return num
    return num * -1


# def absValue(num):
#     return abs(num)
print(absValue(-2))