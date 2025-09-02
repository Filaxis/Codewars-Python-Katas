# Variation of this nice kata, the war has expanded and become dirtier and meaner;
# both even and odd numbers will fight with their pointy 1s. And negative integers
# are coming into play as well, with, ça va sans dire, a negative contribution
# (think of them as spies or saboteurs).

# A number's strength is determined by the number of set bits (1s) in its binary
# representation. Negative integers work against their own side so their strength
# is negative. For example -5 = -101 has strength -2 and +5 = +101 has strength +2.

# The side with the largest cumulated strength wins.

# Again, three possible outcomes: odds win, evens win and tie.

# Examples:

# [1,5,12]    => "odds win"  //   1 + 101 vs 1100,         3 vs 2
# [7,-3,20]   => "evens win" // 111 - 11  vs 10100,    3 - 2 vs 2
# [7,-3,-2,6] => "tie"       // 111 - 11  vs -1 + 110,  3 - 2 vs -1 + 2

# binary_digits = bin(10)[2:]
# print(binary_digits)  # Output: '1010'

# # Using format()
# print(format(10, 'b'))  # Output: '1010'

# # Using f-string
# print(f"{10:b}")        # Output: '1010'

# binary_str = '1010'
# integer = int(binary_str, 2)
# print(integer)  # Output: 10

array1 = [1, 2, 3, 4]

array2 = [1, -2, -3, 4]

array3 = [-1, -2, -3, -4, -5]

def bits_war(integerArray):
    returnStatement = ''
    evens = ''
    odds = ''
    negEvens = ''
    negOdds = ''
    evenSum = oddSum = 0
    for integer in integerArray:
        if (integer % 2) == 0 and integer > 0:
            evens = evens + format(integer, 'b')
            print("Add " + str(integer) + " to the evens.")
        elif (integer % 2) == 0 and integer < 0:
            negEvens = negEvens + format(integer, 'b')
        elif (integer % 2) == 1 and integer > 0:
            odds = odds + format(integer, 'b')
            print("Add " + str(integer) + " to the odds.")
        elif (integer % 2) == 1 and integer < 0:
            negOdds = negOdds + format(integer, 'b')
    for char in evens:
        if char == '1':
            evenSum += 1
    for char in odds:
        if char == '1':
            oddSum += 1
    for char in negEvens:
        if char == '1':
            evenSum += -1
    for char in negOdds:
        if char == '1':
            oddSum += -1
    if evenSum > oddSum:
        returnStatement = 'evens win'
    elif oddSum > evenSum:
        returnStatement = 'odds win'
    elif evenSum == oddSum:
        returnStatement = 'tie'
    print(evens)
    print(odds)
    print(evenSum)
    print(oddSum)
    print(returnStatement)
    return returnStatement

bits_war(array3)