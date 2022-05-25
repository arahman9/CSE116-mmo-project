import json
import csv
import randomcolor


def csvtoarray():
    result = []
    with open("grid.csv", newline="") as file:
        reader = csv.reader(file)
        for line in reader:
            result.append(line)
    return json.dumps(result)


def txttocode(hexcode):
    borked = "#" + hexcode
    with open("currentplayers.txt") as f:
        for line in f:
            wordList = line.split()
            if wordList[0] == borked:
                wordList.reverse()
                print(wordList[0])
                return wordList[0]
        return "none"


def writecode(hex, fam):
    borked = "#" + hex
    f = open("currentplayers.txt", "a")
    f.write("\n")
    f.write(borked + " " + fam)
    f.close()
    return hex.strip("#")


def updategrid(hex, x, y):
    borked = "#" + hex
    x = int(x)
    y = int(y)
    storage = []
    with open("grid.csv", newline="") as file:
        reader = csv.reader(file)
        for line in reader:
            storage.append(line)
    storage[y][x] = borked
    with open("grid.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(storage)
    return hex.strip("#")


def getcolorforjavascript(family):
    rc = randomcolor.RandomColor()
    rando = rc.generate(hue=family)
    actualhexcode = rando[0].strip("#")
    return writecode(actualhexcode, family)
