import re
import random

with open("dictionary.txt", "r") as dictionary:
    lines = dictionary.read().splitlines()

def getRandomWord(lines):
    word = lines[random.randrange(0, len(lines))]

    return word

class RegExHangman:

    def __init__(self, word):
        self.origWord = word
        self.word = "_" * (len(word))
        self.prevGuesses = []
        self.letters = []
        self.limit = 10
        self.main()

    def getWord(self):
        return self.word

    def getOrigWord(self):
        return self.origWord

    def getPrevGuesses(self):
        return self.wrongGuesses

    def getLimit(self):
        return self.limit

    def getRegEx(self):
        regString = input("Enter a regular expression: ")

        while regString in self.prevGuesses:
            print("You already guessed " + regString + "!")
            regString = input("Enter a regular expression: ")

        self.prevGuesses.append(regString)
        search = re.search(regString, self.origWord)

        return search

    def buildWord(self, letters):
        tempWord = ""

        for i in range(len(self.origWord)):
            if self.origWord[i] in letters:
                tempWord += self.origWord[i]
            else:
                tempWord += "_"

        self.word = tempWord

    def main(self):
        print(self.word + " (" + str(len(self.origWord)) + " characters)")
        
        while self.word != self.origWord and self.limit != 0:
            regEx = self.getRegEx()
            
            if regEx:
                for letter in regEx.group(0):
                    self.letters.append(letter)
                 
                self.buildWord(self.letters)
                print(self.word)
            else:
                print("No matches!\n" + self.word)

            self.limit -= 1

        if self.word == self.origWord:
            print("You won!\n" + self.origWord + " guessed correctly!")
        else:
            print("You lost! \nThe word was " + self.origWord)

hangman = RegExHangman(getRandomWord(lines))                  
