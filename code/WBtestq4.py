import unittest, sys, io
import q4

class q4Test(unittest.TestCase):
    def testremovingnumbers(self):
        sys.stdin = io.StringIO("yashi2022")
        result = q4.removingnumbers("yashi 2022")
        self.assertEqual = ("yashi",result)
        sys.stdin = sys.__stdin__
        
        sys.stdin = io.StringIO("LOTR2")
        result = q4.removingnumbers("LOTR 2")
        self.assertEqual = ("LOTR",result)
        sys.stdin = sys.__stdin__
