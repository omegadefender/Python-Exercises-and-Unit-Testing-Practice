import unittest
from exercises.name_exercise import vowel

class TestCases(unittest.TestCase):

    def test_name_chop_test(self):
        self.assertEqual(vowel("james"), "ames")
        self.assertEqual(vowel("emma"), "emma")
        self.assertEqual(vowel(""), "noname")
        self.assertEqual(vowel("chetna"), "etna")
        self.assertEqual(vowel("byron"), "yron")
        self.assertEqual(vowel("bryon"), "on")
        self.assertEqual(vowel("ngh"), "ngh")

if __name__ == '__main__':
    unittest.main()