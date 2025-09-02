# Create a function that takes a string and separates it into
# a sequence of letters.

# The array will be formatted as so:

# [['J','L','L','M']
# ,['u','i','i','a']
# ,['s','v','f','n']
# ,['t','e','e','']]
# The function should separate each word into individual letters,
# with the first word in the sentence having its letters in
# the 0th index of each 2nd dimension array, and so on.

# Shorter words will have an empty string in the place once
# the word has already been mapped out.
# (See the last element in the last part of the array.)

# Examples:

# sep_str("Just Live Life Man")

# # => [['J','L','L','M'],
# # => ['u','i','i','a'],
# # => ['s','v','f','n'],
# # => ['t','e','e','']]);

# sep_str("The Mitochondria is the powerhouse of the cell")

# # => [ [ 'T', 'M', 'i', 't', 'p', 'o', 't', 'c' ],
# # => [ 'h', 'i', 's', 'h', 'o', 'f', 'h', 'e' ],
# # => [ 'e', 't', '', 'e', 'w', '', 'e', 'l' ],
# # => [ '', 'o', '', '', 'e', '', '', 'l' ],
# # => [ '', 'c', '', '', 'r', '', '', '' ],
# # => [ '', 'h', '', '', 'h', '', '', '' ],
# # => [ '', 'o', '', '', 'o', '', '', '' ],
# # => [ '', 'n', '', '', 'u', '', '', '' ],
# # => [ '', 'd', '', '', 's', '', '', '' ],
# # => [ '', 'r', '', '', 'e', '', '', '' ],
# # => [ '', 'i', '', '', '', '', '', '' ],
# # => [ '', 'a', '', '', '', '', '', '' ]]

string1 = "This is test string number one."

string2 = "This is very long word: hepatocardiomaniac"

def sep_str(string):
    words = string.split(' ')
    longestWord = ''
    counter = 0
    print(words)
    for word in words:
        if len(word) > len(longestWord):
            longestWord = word
    print(longestWord)
    lettersMatrix = [['' for _ in range(len(longestWord))] for _ in range(len(words))]
    for i in range(0,len(words)):
        print(words[i])
        counter = 0
        for char in words[i]:
            lettersMatrix[i][counter] = char
            counter += 1
    result = [['' for _ in range(len(words))] for _ in range(len(longestWord))]
    for j in range(0,len(words)):
        for k in range(0,len(longestWord)):
            result[k][j] = lettersMatrix[j][k]
    print(lettersMatrix)
    for row in result:
        print(' '.join(row))
    return result

sep_str(string1)