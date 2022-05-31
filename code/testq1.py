import q1
import unittest

class Q1Test(unittest.TestCase):
    def testlowerconversion(self):
        self.assertEqual("yashi", q1.lowerconversion("Yashi"),"yashi")
        self.assertEqual("yashi", q1.lowerconversion("YASHI"),"yashi")
        self.assertEqual("error", q1.menuinput(),"numbers cannot be converted")
