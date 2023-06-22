import unittest

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1,2,3]),6,"should be 6")
    def test_sum_tup(self):
        self.assertEqual(sum((11,12,1)),24,"should be 24")

if __name__=='__main__':
    unittest.main()
