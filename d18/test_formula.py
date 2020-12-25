import unittest
from .tokenizer import Tokenizer


class TestFormula(unittest.TestCase):
    def test_simple(self):
        input = "1 + 2 * 3 + 4 * 5 + 6"
        expected = ("+", ("*", ("+", ("*", ("+", 1, 2), 3), 4), 5), 6)
        result = Tokenizer.simple(input).as_tuple()
        self.assertEqual(expected, result)

    def test_parens(self):
        input = "1 + (2 * 3) + (4 * (5 + 6))"
        expected = ("+", ("+", 1, ("*", 2, 3)), ("*", 4, ("+", 5, 6)))
        result = Tokenizer.simple(input).as_tuple()
        self.assertEqual(expected, result)

    def test_simple_calc(self):
        input = "1 + 2 * 3 + 4 * 5 + 6"
        expected = 71
        token = Tokenizer.simple(input)
        result = token.get_value()
        self.assertEqual(expected, result)

    def test_parens_calc(self):
        input = "1 + (2 * 3) + (4 * (5 + 6))"
        expected = 51
        token = Tokenizer.simple(input)
        result = token.get_value()
        self.assertEqual(expected, result)

    def test_parens_calc2(self):
        input = "2 * 3 + (4 * 5)"
        expected = 26
        token = Tokenizer.simple(input)
        result = token.get_value()
        self.assertEqual(expected, result)

    def test_parens_calc3(self):
        input = "5 + (8 * 3 + 9 + 3 * 4 * 3)"
        expected = 437
        token = Tokenizer.simple(input)
        result = token.get_value()
        self.assertEqual(expected, result)

    def test_parens_calc4(self):
        input = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
        expected = 12240
        token = Tokenizer.simple(input)
        result = token.get_value()
        self.assertEqual(expected, result)

    def test_parens_calc5(self):
        input = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
        expected = 13632
        token = Tokenizer.simple(input)
        result = token.get_value()
        self.assertEqual(expected, result)


class TestAdvanced(unittest.TestCase):
    def test_simple(self):
        input = "1 + 2 * 3 + 4 * 5 + 6"
        expected = ("*", ("*", ("+", 1, 2), ("+", 3, 4)), ("+", 5, 6))
        result = Tokenizer.advanced(input).as_tuple()
        self.assertEqual(expected, result)

    def test_parens(self):
        input = "1 + (2 * 3) + (4 * (5 + 6))"
        expected = ("+", ("+", 1, ("*", 2, 3)), ("*", 4, ("+", 5, 6)))
        result = Tokenizer.advanced(input).as_tuple()
        self.assertEqual(expected, result)

    def test_simple_calc(self):
        input = "1 + 2 * 3 + 4 * 5 + 6"
        expected = 231
        token = Tokenizer.advanced(input)
        result = token.get_value()
        self.assertEqual(expected, result)

    def test_parens_calc(self):
        input = "1 + (2 * 3) + (4 * (5 + 6))"
        expected = 51
        token = Tokenizer.advanced(input)
        result = token.get_value()
        self.assertEqual(expected, result)

    def test_parens_calc2(self):
        input = "2 * 3 + (4 * 5)"
        expected = 46
        token = Tokenizer.advanced(input)
        result = token.get_value()
        self.assertEqual(expected, result)

    def test_parens_calc3(self):
        input = "5 + (8 * 3 + 9 + 3 * 4 * 3)"
        expected = 1445
        token = Tokenizer.advanced(input)
        result = token.get_value()
        self.assertEqual(expected, result)

    def test_parens_calc4(self):
        input = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
        expected = 669060
        token = Tokenizer.advanced(input)
        result = token.get_value()
        self.assertEqual(expected, result)

    def test_parens_calc5(self):
        input = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
        expected = 23340
        token = Tokenizer.advanced(input)
        result = token.get_value()
        self.assertEqual(expected, result)
