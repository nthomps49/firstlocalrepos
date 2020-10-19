import unittest
import shape_area

class TestArea(unittest.TestCase):

    def test_triangle(self):
        self.assertEqual(shape_area.triangle(10, 5), 25)

    def test_rectangle(self):
        self.assertEqual(shape_area.rectangle(6, 7), 26)

    def test_square(self):
        self.assertEqual(shape_area.square(7), 49)

if __name__ == '__main__':
    unittest.main()
    
#to call just one of these tests you do python -m unittest \ -q test_shape_area.TestArea.test_square -v
#-q for quiet mode to reduce console outpu