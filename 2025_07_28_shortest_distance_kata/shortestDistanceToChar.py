# Given a string s and a character c, return an array of integers

# representing the shortest distance from the current character in s to c.

# Notes
# All letters will be lowercase.
# If the string is empty, return an empty array.
# If the character is not present, return an empty array.
# Examples
# s = "lovecodewars"
# c = "e"
# result = [3, 2, 1, 0, 1, 2, 1, 0, 1, 2, 3, 4]

# s = "aaaabbbb"
# c = "b"
# result = [4, 3, 2, 1, 0, 0, 0, 0]

# s = "aaaaa"
# c = "b"
# result = []

# s = ""
# c = "b"
# result = []

# s = "abcde"
# c = ""
# result = []

def shortest_to_char(inputString,c):
    if inputString == '':
        intArray = []
        # print(intArray)
        return intArray
    elif c == '':
        intArray = []
        # print(intArray)
        return intArray
    # elif type(inputString) != str:
    #     intArray = []
    #     return intArray
    # elif type(c) != str:
    #     intArray = []
    #     return intArray
    else:
        intArray = [char for char in str(inputString)]
        temporalIndex = 0
        assigner = False
        print(inputString)
        print(intArray)
        for i in range(len(intArray)):
            temporalIndex = i
            for j in range(i,len(inputString)):
                if inputString[j] == c:
                    #print(inputString[j])
                    #print(str(temporalIndex) + 'yeah!')
                    intArray[i] = j-i
                    temporalIndex = j-i
                    assigner = True
                    break
            for m in range(i,-1,-1):
                if inputString[m] == c:
                    #print(str(i-m))
                    if i-m < temporalIndex:
                        intArray[i] = i-m
                        temporalIndex = i-m
                    elif temporalIndex == 0:
                        intArray[i] = i-m
                        temporalIndex = i-m
                    break
        if assigner == False:
            intArray = []
            return intArray
        else:
            print(intArray)
            return intArray

shortest_to_char("", 'o')
shortest_to_char("hups", '')
shortest_to_char("motorbuddywhirlpoolbongo", 'o')
shortest_to_char("aaaaa", 'b')