import category
import unittest

class categoryTest(unittest.TestCase):
	def testconvertHours(self):
            self.assertEqual("", category.convertHours(-1), "Invalid/error message")
            self.assertEqual("0", category.convertHours(0), "minutes = 0")
            self.assertEqual("60", category.convertHours(1), "minutes = 60")
        #def testconvertminutes(self):
            #self.assertEqual("0",category.convertminutes(0),"seconds = 0")
            #self.assertEqual("60",category.convertminutes(1),"seconds = 60")
            #self.assertEqual("120",category.convertminutes(2),"seconds = 120")
