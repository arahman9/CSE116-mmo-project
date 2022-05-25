import unittest
from server import translator


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(translator.getcolorforjavascript("monochrome"), "#0f0f0f")


if __name__ == '__main__':
    unittest.main()
