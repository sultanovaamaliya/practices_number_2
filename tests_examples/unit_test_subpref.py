import unittest
from subprefix.subpref import brutforce, fast

class TestBrutforceFunction(unittest.TestCase):
    def test_brutforce(self):
        result = brutforce(["vegetable", "red", "redflag", "book", "notebook"])
        expected = (4, ["book", "notebook"])
        self.assertEqual(result, expected)

    def test_brutforce_not_pref(self):
        self.assertEqual(brutforce(["vegetable", "red", "cat", "book", "log"]), (0, []))

    def test_brutforce_1word(self):
        self.assertEqual(brutforce(["vegetable"]), (0, []))

    def test_brutforce_null(self):
        self.assertEqual(brutforce([]), (0, []))


class TestFastFunction(unittest.TestCase):
    def test_fast_parameterized(self):
        test_cases = [
            ([], (0, [])),
            (["red", "white", "violet", "violett"], (6, ["violett", "violet"])),
            (["tea"], (0, [])),
        ]

        for input_data, expected in test_cases:
            with self.subTest(input_data=input_data, expected=expected):
                self.assertEqual(fast(input_data), expected)

    def setUp(self):
        print("fixture")

    def test_fast(self):
        self.assertEqual(fast(["graf", "pets", "grafica", "giraf"]), (4, ["grafica", "graf"]))

    def test_fast_2same_word(self):
        self.assertEqual(fast(["graf", "graf", "pets", "ui"]), (0, []))


if __name__ == "__main__":
    unittest.main()