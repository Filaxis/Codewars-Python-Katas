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

test_array12 = [1, 2, 3, 1, 0, 0, 1, 5, 6, 8, 9, 1]

def shoot_game(input):
    def innerShooter(values):
        result = 0
        finalSum = 0
        index = 0
        if len(values) == 1:
            result = values[0]
        elif len(values) == 2:
            result = max(values[0],values[1])
        elif len(values) == 3:
            result = max(values[0] + values[2], values[1])
        else:
            for n in range(len(values)):
                print('This is loop number ' + str(n))
                if n+5 > len(values):
                    finalTestSum = [(values[n] + values[n+2]),(values[n+1] + values[n+3]),(values[n] + values[n+3])]
                    finalSum = finalSum + max(finalTestSum)
                    print('The sum of the last two added values is ' + str(max(finalTestSum)))
                    break
                else:
                    if index > 0:
                        index = index - 1
                        # print('Index lowered!')
                        continue
                    testSum = [(values[n] + values[n+2]),(values[n+1] + values[n+3]),(values[n] + values[n+3])]
                    maxSum = [0, 0, 0]
                    nextSum = testSum[0]
                    for i in range(n+4,len(values),2):
                        if values[i] >= 0:
                            nextSum = nextSum + values[i]
                    maxSum[0] = nextSum
                    nextSum = testSum[1]
                    for j in range(n+5,len(values),2):
                        if values[j] >= 0:
                            nextSum = nextSum + values[j]
                    maxSum[1] = nextSum
                    nextSum = testSum[2]
                    for k in range(n+4,len(values),2):
                        if values[k] >= 0:
                            nextSum = nextSum + values[k]
                    maxSum[2] = nextSum
                    nextSum = 0
                    print('Current maxSum is ' + str(maxSum))
                    if max(maxSum) == maxSum[0]: # case 1010
                        finalSum = finalSum + values[n]
                        index = 1
                        print('Case 1010, increment is ' + str(values[n]))
                    elif max(maxSum) == maxSum[1]: # case 0101
                        print('Case 0101, increment is 0')
                    elif max(maxSum) == maxSum[2]: # case 1001
                        finalSum = finalSum + values[n]
                        index = 2
                        print('Case 1001, increment is ' + str(values[n]))
                    print('Current total is ' + str(finalSum))
                    print('The current index is ' + str(index))
        return finalSum

    finalShot = innerShooter(input)
    print('And the final sum is ' + str(finalShot))
    return finalShot

shoot_game(test_array10)