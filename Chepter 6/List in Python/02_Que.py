def Dose_Target_Exists(lst, target):
    for num in lst:
        if num == target:
            return True
    return False
num = [-1,-5,-4,-8,-6]
print(Dose_Target_Exists(num, -8))