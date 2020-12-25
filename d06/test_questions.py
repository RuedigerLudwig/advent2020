from common.utils import read_file
import unittest
from .answers import AnswerEval


class TestQuestions(unittest.TestCase):
    def setUp(self):
        self.all_answers = read_file("d06/data/sample1.txt")

    def test_anyone(self):
        expected = 11
        answers = AnswerEval.by_anyone(self.all_answers)
        result = sum(len(a) for a in answers)

        self.assertEqual(expected, result)

    def test_everyone(self):
        expected = 6
        answers = AnswerEval.by_everyone(self.all_answers)
        result = sum(len(a) for a in answers)

        self.assertEqual(expected, result)
