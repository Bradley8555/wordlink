import re
import enchant

d = enchant.Dict("en_US")

def takeword():
    word = input("Enter the word: ")
    x = re.findall("\d", word)
    if x:
        print("INVALID")
    else:
        print(len(word))

        if len(word) > 10 and len(word) == 0:
            print("Enter valid text")

        for i in word:
            if d.check(i):
                print(i)


            findit(i, word)


def findit(letter, array):
    for i in array:
        trail = i
        wordfound = letter + trail
        if len(wordfound) <= len(array):
            if d.check(wordfound):
                print(wordfound)
            findit(wordfound, array)


takeword()
