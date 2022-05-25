import unittest
from NO_TOUCHIE import randomColorGen


def testRandColor(rgb,color):
    if color == "red" and ((rgb[0] > rgb[1]) and (rgb[0] > rgb[2])):
        return True
    elif color == "green" and ((rgb[1] > rgb[0]) and (rgb[1] > rgb[2])):
        return True
    elif color == "blue" and ((rgb[2] > rgb[0]) and (rgb[2] > rgb[1])):
        return True
    else:
        return False

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(testRandColor(randomColorGen.randomColorGen(0), "red"), True)
        self.assertEqual(testRandColor(randomColorGen.randomColorGen(1), "blue"), True)
        self.assertEqual(testRandColor(randomColorGen.randomColorGen(2), "green"), True)


if __name__ == '__main__':
    unittest.main()