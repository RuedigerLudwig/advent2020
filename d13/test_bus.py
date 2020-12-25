import unittest
from common.utils import read_file
from .bus import BusFactory


class TestBuch(unittest.TestCase):
    def test_sample(self):
        expected = 939, [7, 13, None, None, 59, None, 31, 19]
        lines = read_file("d13/data/sample1.txt")
        result = BusFactory.create_timetable(lines)
        self.assertEqual(expected, result)

    def test_analyse_timetable(self):
        expected = 295
        lines = read_file("d13/data/sample1.txt")
        earliest, busses = BusFactory.create_timetable(lines)
        bus, wait = BusFactory.get_best_bus(earliest, busses)
        self.assertEqual(expected, bus * wait)

    def test_best_departure(self):
        expected = 1068781
        lines = read_file("d13/data/sample1.txt")
        _, busses = BusFactory.create_timetable(lines)
        best_time = BusFactory.get_best_departure(busses)
        self.assertEqual(expected, best_time)

    def test_best_departure2(self):
        lines = read_file("d13/data/sample2.txt")
        expected, busses = BusFactory.create_timetable(lines)
        best_time = BusFactory.get_best_departure(busses)
        self.assertEqual(expected, best_time)

    def test_best_departure3(self):
        lines = read_file("d13/data/sample3.txt")
        expected, busses = BusFactory.create_timetable(lines)
        best_time = BusFactory.get_best_departure(busses)
        self.assertEqual(expected, best_time)

    def test_best_departure4(self):
        lines = read_file("d13/data/sample4.txt")
        expected, busses = BusFactory.create_timetable(lines)
        best_time = BusFactory.get_best_departure(busses)
        self.assertEqual(expected, best_time)

    def test_best_departure5(self):
        lines = read_file("d13/data/sample5.txt")
        expected, busses = BusFactory.create_timetable(lines)
        best_time = BusFactory.get_best_departure(busses)
        self.assertEqual(expected, best_time)

    def test_best_departure6(self):
        lines = read_file("d13/data/sample6.txt")
        expected, busses = BusFactory.create_timetable(lines)
        best_time = BusFactory.get_best_departure(busses)
        self.assertEqual(expected, best_time)

    def _test_best_real(self):
        expected = 0
        lines = read_file("d13/data/input.txt")
        _, busses = BusFactory.create_timetable(lines)
        best_time = BusFactory.get_best_departure(busses)
        self.assertEqual(expected, best_time)
