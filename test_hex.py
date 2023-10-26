import unittest
from hex import decimal_to_hex

class TestDecimalToHex(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(decimal_to_hex(40), "28")

    def test_zero_input(self):
        self.assertEqual(decimal_to_hex(0), "0")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            decimal_to_hex(-5)

    def test_large_input(self):
        self.assertEqual(decimal_to_hex(255), "FF")

if __name__ == '__main__':
    unittest.main()
