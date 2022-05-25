import random

def randomColorGen(ColorGroup):
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    print((red,green,blue))
    dic = {"red": 0, "blue": 1, "green": 2}
    if ColorGroup == 0:
        while (red < blue) or (red < green):
            red = random.randint(0, 255)
            print(red)
            blue = random.randint(0, 255)
            green = random.randint(0, 255)
    elif ColorGroup == 1:
        while (blue < red) or (blue < green):
            red = random.randint(0, 255)
            blue = random.randint(0, 255)
            green = random.randint(0, 255)
    else:
        while (green < red) or (green < blue):
            red = random.randint(0,255)
            blue = random.randint(0,255)
            green = random.randint(0,255)
    color = (red, green, blue)
    print(color)
    return color
