import unittest
from common.utils import read_file
from .ticket import NoteSheet, TicketMatcher


class TestTicketNotesV1(unittest.TestCase):
    def setUp(self):
        lines = read_file("d16/data/sample1.txt")
        self.notes = NoteSheet(lines)

    def test_fields(self):
        expected = {
            "class": ((1, 3), (5, 7)),
            "row": ((6, 11), (33, 44)),
            "seat": ((13, 40), (45, 50))
        }
        result = self.notes.fields

        self.assertEqual(expected, result)

    def test_my_ticket(self):
        expected = [7, 1, 14]
        result = self.notes.my_ticket_numbers

        self.assertEqual(expected, result)

    def test_nearby_numbers(self):
        expected = [[7, 3, 47], [40, 4, 50], [55, 2, 20], [38, 6, 12]]
        result = self.notes.nearby_numbers

        self.assertEqual(expected, result)

    def test_find_invalid_numbers(self):
        expected = {4, 55, 12}
        result = set(self.notes.find_invalid_numbers())

        self.assertEqual(expected, result)


class TestTicketNotesV2(unittest.TestCase):
    def setUp(self):
        lines = read_file("d16/data/sample2.txt")
        self.notes = NoteSheet(lines)

    def test_find_correct_fields(self):
        expected = ["row", "class", "seat"]
        result = TicketMatcher(self.notes)

        self.assertEqual(expected, result.fields)

    def test_get_my_ticket(self):
        expected = {"row": 11, "class": 12, "seat": 13}
        result = TicketMatcher(self.notes).make_ticket(
            self.notes.my_ticket_numbers)

        self.assertEqual(expected, result)
