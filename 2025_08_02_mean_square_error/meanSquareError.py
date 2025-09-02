# Complete the function that

# - accepts two integer arrays of equal length
# - compares the value each member in one array to the corresponding member
#   in the other
# - squares the absolute value difference between those two values
# - and returns the average of those squared absolute value difference
#   between each member pair.

# Examples

# [1, 2, 3], [4, 5, 6]              -->   9   because (9 + 9 + 9) / 3
# [10, 20, 10, 2], [10, 25, 5, -2]  -->  16.5 because (0 + 25 + 25 + 16) / 4
# [-1, 0], [0, -1]                  -->   1   because (1 + 1) / 2

# ArraysMathematicsAlgorithms

testArray11 = [1, 2, 3]
testArray12 = [4, 5, 6]
testArray21 = [10, 20, 10, 2]
testArray22 = [10, 25, 5, -2]
testArray31 = [-1, 0]
testArray32 = [0, -1]

def solution(array1, array2):
    if len(array1) != len(array2):
        return None
    else:
        differenceArray = [0] * len(array1)
        print(differenceArray)
        result = 0
        for i in range(len(array1)):
            differenceArray[i] = abs(array1[i] - array2[i])**2
            result = result + differenceArray[i]
        result = float(result) / len(array1)
        print(result)
        return result
        

solution(testArray11,testArray12)
solution(testArray21,testArray22)
solution(testArray31,testArray32)