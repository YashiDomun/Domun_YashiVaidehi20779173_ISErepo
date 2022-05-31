import unittest, sys, io
import q1

class q1Test(unittest.TestCase):
    def testlowerconversion(self):
        sys.stdin = io.StringIO("YasHI Domun")
        result = q1.lowerconversion("YasHI Domun")
        self.assertEqual = ("yashi domun",result)
        sys.stdin = sys.__stdin__
        
        sys.stdin = io.StringIO("vaIDEHi")
        result = q1.lowerconversion("vaiDEHi")
        self.assertEqual = ("vaidehi",result)
        sys.stdin = sys.__stdin__
        
    def testupperconversion(self):
        sys.stdin = io.StringIO("YasHI Domun")
        result = q1.upperconversion("YasHI Domun")
        self.assertEqual = ("YASHI DOMUN",result)
        sys.stdin = sys.__stdin__
        
        sys.stdin = io.StringIO("vaIDEHi")
        result = q1.upperconversion("vaiDEHi")
        self.assertEqual = ("VAIDEHI",result)
        sys.stdin = sys.__stdin__
