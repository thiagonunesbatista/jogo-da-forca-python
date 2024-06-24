import random
import csv

def writeCsvFile(data, fileDirectory):
    with open(fileDirectory, 'w', encoding='UTF8', newline='') as file:
      writer = csv.DictWriter(file, fieldnames=["name", "victories", "defeats"])

      writer.writeheader()
      writer.writerows(data)

def readCsvFile(fileDirectory):
    with open(fileDirectory, encoding="utf8") as file:
        csvReader = csv.DictReader(file)

        csvLines = []

        for line in csvReader:
            csvLines.append(line)
        
        return csvLines


def generateRandomNumber(startNumber, endNumber):
  return random.randint(startNumber, endNumber)

def readFile(fileName):
  with open(fileName, "r") as file:
    return file

def readFileLines(fileName):
    with open(fileName, "r") as file:
      lines = file.readlines()
      return [line.rstrip('\n') for line in lines]
  
def removeNewLineCharacterFromString(string):
  return string.rstrip('\n')

def chooseWordFromFile(fileName):
  wordsFromFile = readFileLines(fileName)

  choosenWordIndex = generateRandomNumber(0, len(wordsFromFile) - 1)

  return wordsFromFile[choosenWordIndex] 