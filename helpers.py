import random

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