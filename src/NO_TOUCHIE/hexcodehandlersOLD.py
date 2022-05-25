import randomcolor
import csv
import math

'''
def onetimeuse():
    rc = randomcolor.RandomColor()
    print(rc.generate(hue="red", count=3))
    print(rc.generate(hue="orange", count=3))
    print(rc.generate(hue="yellow", count=3))
    print(rc.generate(hue="green", count=3))
    print(rc.generate(hue="blue", count=3))
    print(rc.generate(hue="purple", count=3))
    print(rc.generate(hue="monochrome", count=3))
'''

'''
def generaterandomgrid():
    rc = randomcolor.RandomColor()
    with open("C:\\Users\\krishy\\IdeaProjects\\plzwork\\src\\pixelgridcapture\\grid.csv", "w") as file:
        writer = csv.writer(file)
        index = 0
        indey = 0
        while indey < 50:
            temp = []
            while index < 50:
                color = rc.generate()
                temp.append(color[0])
                index += 1
            index = 0
            indey += 1
            writer.writerow(temp)
'''


def checkenteredcode(hexcode):
    with open("C:\\Users\\krishy\\IdeaProjects\\plzwork\\src\\pixelgridcapture\\currentplayers.txt") as f:
        for line in f:
            wordList = line.split()
            if wordList[0] == hexcode:
                wordList.reverse()
                return wordList[0]
        return "none"


def giveusernewcode(family):
    rc = randomcolor.RandomColor()
    rando = rc.generate(hue=family)
    actualhexcode = rando[0]
    f = open("C:\\Users\\krishy\\IdeaProjects\\plzwork\\src\\pixelgridcapture\\currentplayers.txt", "a")
    f.write("\n")
    f.write(actualhexcode + " " + family)
    f.close()
    return actualhexcode


def watchoutforthatgridonthefloor():
    result = []
    with open("C:\\Users\\krishy\\IdeaProjects\\plzwork\\src\\pixelgridcapture\\grid.csv", newline="") as file:
        reader = csv.reader(file)
        for line in reader:
            result.append(line)
    return result


def editgrid(hexcode, xy):
    x = xy[0]
    y = xy[1]
    index = math.floor(x / 20)
    indey = math.floor(y / 20)
    storage = []
    with open("C:\\Users\\krishy\\IdeaProjects\\plzwork\\src\\pixelgridcapture\\grid.csv", newline="") as file:
        reader = csv.reader(file)
        for line in reader:
            storage.append(line)
    storage[indey][index] = hexcode
    with open("C:\\Users\\krishy\\IdeaProjects\\plzwork\\src\\pixelgridcapture\\grid.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(storage)
