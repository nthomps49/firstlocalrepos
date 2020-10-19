import unittest

class TruthTest(unittest.TestCase):
    
    def test_assert_true(self):
        self.assertTrue((5-2)==3)
#    @unittest.skip('Learning how to skip error test')
#can also do @unittet.skipIf(sys.version_info[0] < 3, 'This test requires python 3 or higher')  with import sys to see what version python 
#can also do @unittest.skipUnless(sys.platform.startswith('win'), 'Requires Windows') 
    def test_assert_false(self):
        self.assertFalse((5-2) == 4)
        
if __name__ == '__main__':
    unittest.main()