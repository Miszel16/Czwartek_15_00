import unittest
import funkcje

class Test_add(unittest.TestCase):
    def test_add(self):
        self.assertEqual(funkcje.add(3, 4), 7)
        self.assertNotEqual(funkcje.add(3,4), 8)

    def test_add_negatives(self):
        self.assertEqual(funkcje.add(-4, -1), -5)
        self.assertNotEqual(funkcje.add(-1, 0), 0)
        self.assertNotEqual(funkcje.add(-5, -8), 0)


class Test_palindrom(unittest.TestCase):
    def test_palindrom(self):
        self.assertTrue(funkcje.is_palindrom("kajak"))
        self.assertFalse(funkcje.is_palindrom("pies"))


if __name__ == '__main__':
    unittest.main()