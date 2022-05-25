import json

def changeHex (file,x,y,hex):
    f = open(file)
    varia = json.load(f)
    varia[y][x] = hex
