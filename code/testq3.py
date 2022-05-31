import q3
import unittest

class Q3Test(unittest.TestCase):
    def testchecknumbers(self):
        self.assertEqual("False", q3.checknumbers("qwer3ty"),"isnumber = False")
        self.assertEqual("False",q3.checknumbers("qwerty"), "isnumber = false")
        self.assertEqual("True",q3.checknumbers("2345"), "isnumber = true")
