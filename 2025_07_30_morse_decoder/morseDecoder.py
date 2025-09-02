# In this kata you have to write a simple Morse code decoder.While the Morse code
# is now mostly superseded by voice and digital data communication channels, it
# still has its use in some applications around the world.
# The Morse code encodes every character as a sequence of "dots" and "dashes".
# For example, the letter A is coded as ·−, letter Q is coded as −−·−,
# and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally
# capital letters are used. When the message is written in Morse code, a single
# space is used to separate the character codes and 3 spaces are used to separate
# words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

# NOTE: Extra spaces before or after the code have no meaning and should be ignored.

# In addition to letters, digits and some punctuation, there are some special service
# codes, the most notorious of those is the international distress signal SOS
# (that was first issued by Titanic), that is coded as ···−−−···.
# These special codes are treated as single special characters, and usually are
# transmitted as separate words.

# Your task is to implement a function that would take the morse code as input
# and return a decoded human-readable string.

# For example:

# decode_morse('.... . -.--   .--- ..- -.. .')
# #should return "HEY JUDE"
# NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.

# All the test strings would contain valid Morse code, so you may skip checking
# for errors and exceptions. In C#, tests will fail if the solution code throws an exception,
# please keep that in mind. This is mostly because otherwise the engine would simply
# ignore the tests, resulting in a "valid" solution.

# Good luck!

# After you complete this kata, you may try yourself at Decode the Morse code, advanced.


# *** *** *** ***

# Here are the lines that were already prepared for the input (so I guess one should use the naming convention at least)

# from preloaded import MORSE_CODE

# def decode_morse(morse_code):
    # # Remember - you can use the preloaded MORSE_CODE dictionary:
    # # For example: 
    # # MORSE_CODE['.-'] = 'A'
    # # MORSE_CODE['--...'] = '7'
    # # MORSE_CODE['...-..-'] = '$'
    # pass

def decode_morse(morseString):
    import copy
    REV_MORSE_CODE_DICT = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z',
        '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'
    }
    morseString = morseString.strip()
    morseWords = str(morseString).split('   ')
    print(morseWords[1])
    morseChars = copy.copy(morseWords)
    translatedWords = copy.copy(morseWords)
    for i in range(len(morseWords)):
        morseChars[i] = morseWords[i].split(' ')
    print(morseChars)
    translatedChars = copy.copy(morseChars)
    for j in range(len(morseChars)):
        for k in range(len(morseChars[j])):
            translatedChars[j][k] = str(REV_MORSE_CODE_DICT.get(morseChars[j][k],'bloody hell'))
            #print(morseChars[j][k])
        translatedWords[j] = ''.join(translatedChars[j])
        print(translatedChars[j])
        print(translatedWords[j])
    translatedString = ''
    translatedString = ' '.join(translatedWords)
    print(translatedString)
    return translatedString

decode_morse('.... . -.--   .--- ..- -.. .')
#should return "HEY JUDE"