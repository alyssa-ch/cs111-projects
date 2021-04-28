# -*- coding: utf-8 -*-
# Your name: Alyssa Choi and Amanda Cheung
# Your username: ac111, ac119
# CS111 PS05 Task TODO
# poetry.py
# Submission date: 10/01/2020

import unicodedata # for working with accented vowels

# Import poems
from poems import *

#------#
# Data #
#------#

# A dictionary which specifies for each punctuation mark, how it should
# be represented when the poem is displayed (e.g., should there be a
# space before and/or after it?). These punctuation marks will be
# represented as one-character strings within poems.
PUNCTUATION = {
    '“': ' “',
    '”': '” ',
    '‘': ' ‘',
    '’': '’ ',
    '"': '"',
    "'": "'",
    ".": ". ",
    ",": ", ",
    ";": "; ",
    ":": ": ",
    "!": "! ",
    "?": "? ",
    "(": " (",
    ")": ") ",
    "/": "/",
    "-": "-",
    "_": "_",
    "「": "「",
    "」": "」",
    "，": "，",
    "。": "。",
    "¡": " ¡",
    "¿": " ¿",
    "…": "… ",
}


# This dictionary defines, for each supported language, the mode value
# that should be used for that language when calling estimateSyllables.
LANGUAGE_MODES = {
    "English": "mostVowelGroups",
    "German": "vowelGroups",
    "Spanish": "vowelGroups",
    "Japanese": "length",
    "JapaneseTransliterated": "vowelGroups",
    "Chinese": "length",
    "ChineseTransliterated": "vowelGroups",
    "VariableNames": "mostVowelGroups",
}


# For each language, whether or not spaces should be inserted between
# words in that language:
LANGUAGE_SPACES = {
    "English": True,
    "German": True,
    "Spanish": True,
    "Japanese": False,
    "JapaneseTransliterated": True,
    "Chinese": False,
    "ChineseTransliterated": True,
    "VariableNames": False,
}

#--------------------#
# Provided functions #
#--------------------#

def estimateSyllables(word, mode):
    """
    Estimates the number of syllables in a given word. It needs to know
    what estimation mode to use; supported mode values are:

        "vowelGroups": Estimates based on the number of consecutive
            vowel sequences. Works okay for a number of European
            languages that use Latin alphabets. Treats 'a', 'e', 'i',
            'o', 'u', and 'y' as vowels, including accented forms.
        "mostVowelGroups": Works like vowelGroups, but ignores trailing
            'e' and 'ed' sequences, for improved performance on English.
            Does not ignore trailing accented 'e's.
        "length": Simply measures the number of characters in the string.
            Works well for Chinese, and passably for Japanese written
            using only Hiragana/Katakana.
    """
    if mode == "vowelGroups":
        count_vowels = True
        ignore_trailing = False
    elif mode == "mostVowelGroups":
        count_vowels = True
        ignore_trailing = True
    elif mode == "length":
        count_vowels = False
    else:
        raise ValueError("Invalid syllable estimation mode '{}'.".format(mode))

    if count_vowels:
        if ignore_trailing and word.endswith('e'):
            word = word[:-1]
        elif ignore_trailing and word.endswith('ed'):
            word = word[:-2]

        # Build a simplified string where we remove accents:
        # Note: this idea comes from: https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-normalize-in-a-python-unicode-string
        normalized = unicodedata.normalize("NFD", word) # decompose
        simplified = ''
        for char in normalized:
            if not unicodedata.combining(char): # skip combining characters
                simplified += char

        count = 0
        previousWasVowel = False
        for letter in word:
            if letter in 'aeiouy': # accents have been stripped
                if not previousWasVowel:
                    count += 1
                previousWasVowel = True
            else:
                previousWasVowel = False

        return max(1, count) # can't have a zero-syllable word

    else:
        return len(word)


#----------------------#
# Write your code here #
#----------------------#

def displayPoem(poem, language):
    """

    """
    if language in LANGUAGE_SPACES:
        for line in poem:
            poemLine = ''
            for word in range(len(line)):
                    if line[word] in PUNCTUATION:
                        if LANGUAGE_SPACES[language]:
                            poemLine = poemLine[:-1] + PUNCTUATION[line[word]]
                                                   
                        else:
                            poemLine += PUNCTUATION[line[word]]
                    elif word != len(line) - 1:
                        if LANGUAGE_SPACES[language]:
                            poemLine += line[word] + ' '
                        else:
                            poemLine += line[word]
                    else:
                        poemLine += line[word]
            print (poemLine)

def countSyllables(poem, language):
    """
    """
    #TODO: Write this function
    newList = []
    for line in poem:
        lineSyll = 0
        for word in line:
            if word not in PUNCTUATION:
                lineSyll += estimateSyllables(word, LANGUAGE_MODES[language])
        newList.append(lineSyll)
    return newList

    


def showSyllableStructure(syllableList):
    """
    """
    structureLine = ''
    for item in syllableList:
        if item > 0:
            structureLine += str(item) + '-'
        else:
            if structureLine != '':
                print(structureLine[:-1])
            structureLine = ''
    if structureLine != '':
        print (structureLine[:-1])
                


#--------------#
# Testing code #
#--------------#

if __name__ == "__main__":
    print("Start of testing.")
    for poemVersions in ALL_POEMS:
        for language in poemVersions:
            poem = poemVersions[language]
            print()
            displayPoem(poem, language)
            print()
            showSyllableStructure(countSyllables(poem, language))
    print("End of testing.")
