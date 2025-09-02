# Write a function that, given a string of text (possibly with punctuation and line-breaks),
# returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

# Assumptions:
# A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
# Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
# Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
# Matches should be case-insensitive, and the words in the result should be lowercased.
# Ties may be broken arbitrarily.
# If a text contains fewer than three unique words, then either the top-2 or top-1 words
# should be returned, or an empty array if a text contains no words.

# Examples:

# "In a village of La Mancha, the name of which I have no desire to call to
# mind, there lived not long since one of those gentlemen that keep a lance
# in the lance-rack, an old buckler, a lean hack, and a greyhound for
# coursing. An olla of rather more beef than mutton, a salad on most
# nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
# on Sundays, made away with three-quarters of his income."

# --> ["a", "of", "on"]


# "e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"

# --> ["e", "ddd", "aa"]


# "  //wont won't won't"

# --> ["won't", "wont"]

# Bonus points (not really, but just for fun):
# Avoid creating an array whose memory footprint is roughly as big as the input text.
# Avoid sorting the entire array of unique words.



example1 = """In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""

example2 = "Simple example it is, sir. And yes, it is as simple of an example as it can get. Let's see what happens!"

example3 = "Simple simple crimp, !sIMple simplE Jane"

example4 = "!!!"

example5 = "Oneword"

example6 = "Two words"

example7 = "Apostrophe separator ' '' ''' let's separate apostrophes ' by ' by '' bro."

def top_3_words(inputString):
    removedExtraChars = ['# ']
    modifiedString = ''
    wordAbundances = [0]
    wordCounter = 0
    max_1 = max_2 = max_3 = 0
    index_1 = index_2 = index_3 = 0
    result = [0, 0, 0]
    print(result)
    print(wordAbundances)
    for char in inputString.lower():
        if char.isalpha():
            removedExtraChars.append(char)
        elif char == "'":
            removedExtraChars.append(char)
        else:
           removedExtraChars.append(' ') 
        #print(removedExtraChars)
    modifiedString = ''.join(removedExtraChars)
    print(modifiedString)
    separatedWords = modifiedString.split(' ')
    del separatedWords[0]
    print(separatedWords)
    uniqueWords = ['#']
    for word in separatedWords:
        if (word != '') and (any(char.isalpha() for char in word) == True) and (word in uniqueWords) == False:
            uniqueWords.append(word)
            wordAbundances.append(0)
    del uniqueWords[0]
    del wordAbundances[0]
    print(uniqueWords)
    print(wordAbundances)
    for uniqueWord in uniqueWords:
        for separatedWord in separatedWords:
            if separatedWord == uniqueWord:
                wordAbundances[wordCounter] += 1
        wordCounter += 1
    print(wordAbundances)
    for i in range(0, len(wordAbundances)):
        if wordAbundances[i] > max_1:
            max_3, max_2, max_1 = max_2, max_1, wordAbundances[i]
            index_3, index_2, index_1 = index_2, index_1, i
        elif wordAbundances[i] > max_2:
            max_3, max_2 = max_2, wordAbundances[i]
            index_3, index_2 = index_2, i
        elif wordAbundances[i] > max_3:
            max_3= wordAbundances[i]
            index_3 = i
    print('The maxima are: ' + str(max_1) + ', ' + str(max_2) + ', ' + str(max_3) + '.')
    print('The indices are: ' + str(index_1) + ', ' + str(index_2) + ', ' + str(index_3) + '.')

    if not uniqueWords:
        result = []
    elif len(uniqueWords) == 1:
        result[0] = uniqueWords[index_1]
        del result[2], result[1]
    elif len(uniqueWords) == 2:
        result[0], result[1] = uniqueWords[index_1], uniqueWords[index_2]
        del result[2]
    else:
        result[0], result[1], result[2] = uniqueWords[index_1], uniqueWords[index_2], uniqueWords[index_3]
    print(result)
    return result

top_3_words(example7)
