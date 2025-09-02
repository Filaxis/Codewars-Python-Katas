# ORIGINAL TASK DESCRIPTION

# How can you tell an extrovert from an introvert at NSA?
# Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

# I found this joke on USENET, but the punchline is scrambled.
# Maybe you can decipher it?
# According to Wikipedia, ROT13 is frequently used to obfuscate
# jokes on USENET.

# For this task you're only supposed to substitute characters.
# Not spaces, punctuation, numbers, etc.

# Test examples:

# "EBG13 rknzcyr." -> "ROT13 example."

# "This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"

# Strings Ciphers Regular Expressions Algorithms

# HINT: A short code to get a dictionary with english alphabet letters
# as keys and their resp. ASCII codes as values

    # ascii_dict = {chr(i): chr(i-13) for i in range(65, 91)}  # Uppercase A-Z
    # ascii_dict.update({chr(i): chr(i-13) for i in range(97, 123)})  # Lowercase a-z

    # print(ascii_dict)
    
    # {
    #     'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71,
    #     'H': 72, 'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78,
    #     'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85,
    #     'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90,
    #     'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103,
    #     'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110,
    #     'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117,
    #     'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122
    # }

def rot13decipher(inputString):

    import re

    Alphabet = {
                    'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 'G': 'T',
                    'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A',
                    'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H',
                    'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M',
                    'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't',
                    'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a',
                    'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h',
                    'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm', ' ': ' '
                }
    
    letterIdentifier = re.compile(r'[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz]')

    outputString = ''

    for letter in inputString:
        if letterIdentifier.search(letter) != None:
            outputString = outputString + str(Alphabet[letter])
        else:
            outputString = outputString + letter
    
    print(outputString)
    return outputString


rot13decipher('EBG13 rknzcyr.')
rot13decipher('This is my first ROT13 excercise!')