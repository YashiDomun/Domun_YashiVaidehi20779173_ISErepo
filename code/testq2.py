import q2
import unittest

class Q2Test(unittest.TestCase):
    def testnumbersfound(self):
        self.assertEqual("True", q2.numbersfound("qwer3ty"),"isnumber = true")
        self.assertEqual("False",q2.numbersfound("qwerty"), "isnumber = false")
        self.assertEqual("True",q2.numbersfound("2345"), "isnumber = true")
