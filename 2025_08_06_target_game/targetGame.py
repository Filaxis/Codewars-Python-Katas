# Task

# In your favorite game, you must shoot a target with a water-gun to gain points.
# Each target can be worth a different amount of points.

# You are guaranteed to hit every target that you try to hit. You cannot hit
# consecutive targets though because targets are only visible for one second
# (one at a time) and it takes you a full second to reload your water-gun after
# shooting (you start the game already loaded).

# Given an array vals with the order of each target's point value, determine
# the maximum number of points that you can win.

# Example
# For vals = [1, 2, 3, 4], the result should be 6.

# your optimal strategy would be to let the first one pass and shoot the second
# one with value 2 and the 4th one with value 4 thus:

# vals[1](2) + vals[3](4) = 6

# For vals = [5, 5, 5, 5, 5], the result should be 15.

# your optimal strategy would be to shoot the 1st, 3rd and 5th value:

# 5 + 5 + 5 = 15

# You haven't shoot the 2nd, 4th value because you are reloading your water-gun
# after shooting other values.

# Note that the value can be zero or negative, don't shoot them ;-)

# For vals = [0, 0, -1, -1], the result should be 0.

# For vals = [5, -2, -9, -4], the result should be 5.

# Shoot the first one is enough.

# Input/Output
# [input] integer array vals
# The point values (negative or non-negative) of the targets (in order of appearance).

# [output] an integer
# The maximum number of points that you can score.

# Algorithms Arrays

test_array1 = [1, 2, 3, 4]
test_array2 = [1, 3, 1]
test_array3 = [5, 5, 5, 5, 5]

test_array4 = [36, 42, 93, 29, 0, 33, 15, 84, 14, 24, 81, 11]                               # 327
test_array5 = [73, 80, 40, 86, 14, 96, 10, 56, 61, 84, 82, 36, 85]                          # 490
test_array6 = [11, 82, 47, 48, 80, 35, 73, 99, 86, 32, 32]                                  # 353
test_array7 = [26, 54, 36, 35, 63, 58, 31, 80, 59, 61, 34, 54, 62, 73, 89, 7, 98, 91, 78]   # 615

test_array8 = [0, 0, -1, -1]

test_array9 = [1, 0, 0, 1]                                                                  # 2

test_array10 = [5, -2, -9, -4]

test_array11 = [1, 2, 3, 4, 5, 6, 8, 9]


def shootTargets(values):

    def testShoot(slice):
        max = 0
        nextSum = 0
        index = 0
        for i in range(len(slice)):
            for j in range(i,len(slice),2):
                if slice[j] >= 0:
                    nextSum = nextSum + slice[j]
            if i == 1 and nextSum > max:
                index += 1
            if nextSum > max:
                max = nextSum
                nextSum = 0
            else:
                nextSum = 0
            # print('partialSum = ' + str(max) + ', valueIndex = ' + str(index))
        return [max,index]
    
    evenSum = 0
    oddSum = 0
    totalSum = 0
    stepCounter = 0
    for k in range(len(values)):
        # print('k = ' + str(k))
        if stepCounter > 0:
            stepCounter = stepCounter - 1
            continue
        testSet = testShoot(values[k:len(values)])
        partialSum = testSet[0]
        valueIndex = testSet[1]
        # print('current range is ' + str(values[k:len(values)]))
        # print('odd range is ' + str(values[k+1:len(values)]))
        # print('partialSum = ' + str(testSet[0]))
        # print('valueIndex = ' + str(testSet[1]))
        if valueIndex == 0 and values[k] >= 0:
            totalSum = totalSum + values[k]
            stepCounter = stepCounter + 1
        elif valueIndex == 1 and values[k+1] >= 0:
            totalSum = totalSum + values[k+1]
            stepCounter = stepCounter + 2
        # print('stepCounter = ' + str(stepCounter))
        # print('partialSum = ' + str(partialSum))
        print('totalSum = ' + str(totalSum))
    print(str(totalSum))
    return totalSum

shootTargets(test_array6)
# shootTargets(test_array6)
# shootTargets(test_array7)
# shootTargets(test_array8)
# shootTargets(test_array10)