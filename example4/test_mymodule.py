# file: test_mymodule.py
import unittest
import mymodule

class TestMyModule(unittest.TestCase):
    def test_add(self):
        self.assertEqual(mymodule.add(3, 5), 8)

    def test_subtract(self):
        self.assertEqual(mymodule.subtract(10, 3), 7)

    def test_multiply(self):
        self.assertEqual(mymodule.multiply(4, 6), 24)

if __name__ == '__main__':
    unittest.main()
