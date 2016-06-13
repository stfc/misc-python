import re
import random

maxlength=4
easymode=True

with open("dictionary.txt", "r") as dictionary:
    lines = dictionary.read().splitlines()

def getRandomWord(lines):
    word = ""
    while len(word) > maxlength or word == "":
        word = lines[random.randrange(0, len(lines))]

    return word

class RegExHangman:

    def __init__(self, word):
        self.origWord = word
        self.word = "_" * (len(word))
        self.prevGuesses = []        
        self.matchGuesses = []
        self.missGuesses = []
        self.letters = []
        self.limit = 20
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
        print("You have " + str(self.limit) + " tries remaining")
        print("Missed Guesses: " + str(self.missGuesses))
        print("Matched Guesses: " + str(self.matchGuesses))
        regString = raw_input("Enter a regular expression or a guess: ")
        while regString in self.prevGuesses:
            print("You already guessed " + regString + "!")
            regString = input("Enter a regular expression: ")

        self.prevGuesses.append(regString)
        search = re.match(regString, self.origWord)
        if search != None:
            self.matchGuesses.append(regString)
        else:
            self.missGuesses.append(regString)
        print(search)
        return search

    def buildWord(self, letters):
        tempWord = ""

        for i in range(len(self.origWord)):
            if easymode and i <2 :
                tempWord += self.origWord[i]
            else:
                tempWord += "_"

        self.word = tempWord

    def main(self):
        print(self.word + " (" + str(len(self.origWord)) + " characters)")
        regEx=""
        while regEx != self.origWord and self.limit != 0:
            regEx = self.getRegEx()
            
            if regEx:
                for letter in regEx.group(0):
                    self.letters.append(letter)
                 
                self.buildWord(self.letters)
                print(self.word)
            else:
                print("No matches!\n" + str(regEx))

            self.limit -= 1
        
        if regEx == self.origWord:
            print("You won!\n" + self.origWord + " guessed correctly!")
        else:
            guess = raw_input("Last chance, please enter a guess: ")
            if guess == self.origWord:
                print("Congratulations you figured it out... somehow")
            else:
                print("Bad luck. The word is: " + self.origWord)

hangman = RegExHangman(getRandomWord(lines))                  
