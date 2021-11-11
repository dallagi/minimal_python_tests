import unittest
from my_sum import *

class MySumTests(unittest.TestCase):
    def test_my_sum(self):
        self.assertEqual(my_sum(1, 2), 3)

if __name__ == '__main__':
    unittest.main()
