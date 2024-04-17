# import os

from helpers import generateRandomNumber, readFileLines, removeNewLineCharacterFromString


# playerName = input("Qual o seu nome? ")


wordsFileName = "words.txt"

readWordsFile = readFileLines(wordsFileName)

chosenWordIndex = generateRandomNumber(0, len(readWordsFile) -1)

chosenGameWord = readWordsFile[chosenWordIndex]

# head, two arms, body, two legs
maximumWrongWords = 6
currentWrongWords = 0 

isGameInCourse = True

print(chosenGameWord)

print("Que os jogos começem...")
print(f"A palavra escolhida tem {len(chosenGameWord)}")

while currentWrongWords < maximumWrongWords and isGameInCourse:
  # print("Feijão com arroz")
  dois = 2
  chosenLetter = input("Digite uma Letra")