def readFile(username):
    with open("/Users/michaelluo/Desktop/demo/demo/dictionary.txt") as f:
        for line in f:
          wordList = line.split("\t")
          #print(wordList)
          if wordList[0] == username:
              wordList.reverse()
              return wordList[0]


print(readFile("beckyking"))