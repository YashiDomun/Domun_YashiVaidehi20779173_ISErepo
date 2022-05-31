import q4
import unittest

class Q4Test(unittest.TestCase):
    def testremovingnumbers(self):
        self.assertEqual("yashi", q4.removingnumbers("yas5hi"),"5 is removed")
        self.assertEqual("YASHI", q4.removingnumbers("YAS67HI"),"67 is removed")
        self.assertEqual("error", q4.removingnumbers("error"),"no number found to be removed")
