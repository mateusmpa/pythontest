import unittest
from io import StringIO
import sys

def invertedstar(n):
    for i in range(n, 0, -1):
        print((n-i) * ' ' + i * '*')

class TestInvertedStar(unittest.TestCase):

    def setUp(self):
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        self.held_output.close()
        sys.stdout = sys.__stdout__

    def test_invertedstar(self):
        invertedstar(5)
        expected_output = "    *****\n     ****\n      ***\n       **\n        *\n"
        self.assertEqual(self.held_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
