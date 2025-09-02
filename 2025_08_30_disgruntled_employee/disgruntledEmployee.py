# Sir Bobsworth is a custodian at a local data center. As he suspected,
# Bobsworth recently found out he is to be fired on his birthday after
# years of pouring his soul into maintaining the facility.

# Bobsworth, however, has other plans.

# Bobsworth knows there are 1 to n switches in the breaker box of
# the data center. Moving from switch 1 to n, Bob first flips every
# switch off. Beginning from the first switch again, Bob then flips
# every 2nd switch. Once again starting from the first switch,
# Bob then flips every 3rd switch. Bob continues this pattern
# until he flips every nth switch & makes n passes.

# At the end of Bobsworth's mayhem, how many switches are turned off?

# Specifications
# Create the function off, that receives the nth switch as argument n.
# The function should return an ascending array containing all of
# the switch numbers that remain off after Bob completes his revenge.

# Example: (Input --> Output)
# 1 --> [1]
# 2 --> [1]
# 4 --> [1, 4]
# The parameter n will always be a number >= 1.

def off(n):
    breakerBox = {i: "on" for i in range(1,n+1)}
    result = []
    print(breakerBox)
    for key in breakerBox.keys():
        print("Loop number " + str(key))
        for i in range(key,n+1,key):
            if breakerBox[i] == "on":
                breakerBox[i] = "off"
                print("Switch number " + str(i) + " turned OFF!")
            elif breakerBox[i] == "off":
                breakerBox[i] = "on"
                print("Switch number " + str(i) + " turned ON!")
    print(breakerBox)
    for key in breakerBox.keys():
        if breakerBox[key] == "off":
            result.append(key)
    print(result)
    return result


off(12)