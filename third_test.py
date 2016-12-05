import unittest
import third

class TestingCounter(unittest.TestCase):

    def test_count_letter_in_string(self):
        self.assertEqual(third.count_letter_in_string('Apple', 'p'),2)

    def test_count_letter_in_string_empty(self):
        self.assertEqual(third.count_letter_in_string('', 'p'),0)

    def test_count_letter_in_string_not_valid(self):
        self.assertEqual(third.count_letter_in_string('Banana', 'p'),0)

    def test_count_letter_in_string_not_string(self):
        self.assertEqual(third.count_letter_in_string(526, 'p'),0)

if __name__ == '__main__':
    unittest.main()
