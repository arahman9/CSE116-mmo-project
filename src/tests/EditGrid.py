import unittest

import pixelgridcapture


class MyTestCase(unittest.TestCase):
    def CheckEntered(self):
        self.assertEqual(hexcodehandlers.checkenteredcode("#12ba2e"),"#12ba2e")
        self.assertEqual(hexcodehandlers.checkenteredcode("#12ba"), "none")
        self.assertEqual(hexcodehandlers.checkenteredcode("#adadad"), "#adadad")
    def testHue(self):
        expected_colors = ['#b98bd3', '#ac5ed1', '#a786d6']
        self.assertEqual(hexcodehandlers.giveusernewcode("purple") in expected_colors)

if __name__ == '__main__':
    unittest.main()
