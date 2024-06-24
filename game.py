from operator import itemgetter
from termcolor import colored

from helpers import readCsvFile, writeCsvFile, chooseWordFromFile

def registerPlayerResult(currentPlayer, fileDirectory):
    results = readCsvFile(fileDirectory)

    newResults = []
    hasFoundPlayerHistory = False

    for currentLine in results:
        if currentLine["name"] == currentPlayer["name"]:
            hasFoundPlayerHistory = True

            if currentPlayer["result"] == 1:
                currentLine['victories'] = int(currentLine['victories']) + 1
            else:
                currentLine['defeats'] = int(currentLine['defeats']) + 1

        newResults.append(currentLine)
            
    if not hasFoundPlayerHistory:
        playerResult = {
            "name": '',
            "victories": 0,
            "defeats": 0
        }
        playerResult['name'] = currentPlayer['name']
        
        if currentPlayer["result"] == 1:
            playerResult["victories"] += 1
        else:
            playerResult["defeats"] += 1

        newResults.append(playerResult)

    writeCsvFile(newResults,'./playersRanking.csv')

def replaceCharactersInHiddenWord(hiddenWord, originalWord, chosenCharacter):
    newWord = ''

    for currentIndex, currentCharacter in enumerate(originalWord):
        if chosenCharacter == currentCharacter:
            newWord += currentCharacter
        else:
            newWord += hiddenWord[currentIndex]

    return newWord

def startGameMenu():
    def wrongMenuOption():
        print("Como você é burro, tente novamente !!!")

    while True:
        print("Jogo da Forca de Órgãos")
        print("1. Iniciar Jogo")
        print("2. Ver Ranking")
        print("3. Sair")

        selectedOption = int(input("Opção: "))
        print("\n")

        if selectedOption == 1:
            startGame()
        elif selectedOption == 2:
            showRanking()
        elif selectedOption == 3:
            exitGame()
            break
        else:
            wrongMenuOption()

def showRanking():
    print("Ranking")
    
    results = readCsvFile("./playersRanking.csv")

    resultsInt = []
    
    for currentLine in results:
        currentLine["victories"] = int(currentLine["victories"]) 
        currentLine["defeats"] = int(currentLine["defeats"]) 
        resultsInt.append(currentLine)

    sortedResults = sorted(resultsInt, key=itemgetter('victories'), reverse=True)

    for index, currentResult in enumerate(sortedResults):
        print(f"{index + 1}º - {currentResult['name']} - {currentResult['victories']} vitórias")

    print("\n")

def exitGame():
    print("Saindo...")

def startGame():
  drawGameWord = chooseWordFromFile("words.txt").lower()
  loserMustPayOrgan = chooseWordFromFile("humanOrgans.txt").lower() 
  winnerMustReceiveOrgan = chooseWordFromFile("humanOrgans.txt").lower()

  playerName = input("Olá meu caro(a), qual seu nome? ").lower()

  # head, arm 1, arm2, body, leg 1 and leg 2
  maximumWrongWords = 6

  chosenWordLength = len(drawGameWord)
  hiddenWordLabel = "_" * (chosenWordLength)

  wrongPlayedCharacters = []
    
  def showGameInstructions():
      print("🔪 Começando o Jogo 🔪")
      print(f"A palavra sorteada tem esse tamanho todo: {chosenWordLength} 😏")
      print(f"Se você ganhar, você recebe de mim: {winnerMustReceiveOrgan}")
      print(f"Se você perder, você me deve: {loserMustPayOrgan}")
      print("\n")

  showGameInstructions()

  while(True):
      print(f"Palavra Para Descobrir: {hiddenWordLabel}")
      playedCharacter = input("Digite uma letra: ").lower()
      playedCharacterIndex = drawGameWord.find(playedCharacter)

      if playedCharacterIndex == -1:
          wrongPlayedCharacters.append(playedCharacter)
      else:
          hiddenWordLabel = replaceCharactersInHiddenWord(hiddenWordLabel, drawGameWord, playedCharacter)

      wrongPlayedCharactersQuantity = len(wrongPlayedCharacters)
        
      if "_" not in hiddenWordLabel:
            print(colored("Você é o bichão memo hein!!!", "green", attrs=["reverse", "bold"]))
            print(f"Palavra adivinhada: {hiddenWordLabel}\n")
            registerPlayerResult({ "name": playerName ,"result": 1}, "./playersRanking.csv")
            break

      if wrongPlayedCharactersQuantity == maximumWrongWords:
          print(colored("Você é Muleke!!!\n", "red", attrs=["reverse", "bold"]))
          registerPlayerResult({ "name": playerName ,"result": 0}, "./playersRanking.csv")
          print(f"A palavra era: {drawGameWord}")
          break

      if (wrongPlayedCharactersQuantity > 0):
          print(f"Jogadas Erradas: {wrongPlayedCharactersQuantity}/{maximumWrongWords}")
          print("Caracteres errados: " + "|".join(wrongPlayedCharacters))
        
      print("\n")
