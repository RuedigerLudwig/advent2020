import unittest
from common.utils import read_file
from . import monster


class TestMonsterParser(unittest.TestCase):
    def setUp(self):
        self.lines = read_file("d19/data/sample1.txt")
        pass

    def test_got_words(self):
        expected = ["ababbb", "bababa", "abbbab", "aaabbb", "aaaabbb"]
        _, words = monster.parse_lines(self.lines)
        self.assertEqual(expected, words)

    def test_got_char_rules(self):
        expected = "CharRule(5, b)"
        rules, _ = monster.parse_lines(self.lines)
        self.assertEqual(expected, str(rules[5]))

    def test_got_seq_rules(self):
        expected = "SequenceRule(0, [4, 1, 5])"
        rules, _ = monster.parse_lines(self.lines)
        self.assertEqual(expected, str(rules[0]))

    def test_got_alt_rules(self):
        expected = "AltRule(2, [4, 4], [5, 5])"
        rules, _ = monster.parse_lines(self.lines)
        self.assertEqual(expected, str(rules[2]))


class TestMonsterMatcher(unittest.TestCase):
    def setUp(self):
        self.lines = read_file("d19/data/sample1.txt")
        pass

    def test_matches(self):
        message = "aaaabb"
        expected = True
        rules, _ = monster.parse_lines(self.lines)
        result = rules[0].matches(message, rules)
        self.assertEqual(expected, result)

    def test_matches2(self):
        message = "abbbab"
        expected = True
        rules, _ = monster.parse_lines(self.lines)
        result = rules[0].matches(message, rules)
        self.assertEqual(expected, result)

    def test_matches_not(self):
        message = "abbbaa"
        expected = False
        rules, _ = monster.parse_lines(self.lines)
        result = rules[0].matches(message, rules)
        self.assertEqual(expected, result)


class TestMingledMonsterMatcher(unittest.TestCase):
    def setUp(self):
        self.lines = read_file("d19/data/sample2.txt")
        pass

    def test_check_mingled_match(self):
        expected = True
        rules, _ = monster.parse_lines(self.lines)
        rules = monster.mingle_rules(rules)
        result = rules[0].matches("aaaaabbaabaaaaababaa", rules)
        self.assertEqual(expected, result)

    def test_check_mingled_match2(self):
        expected = True
        rules, _ = monster.parse_lines(self.lines)
        new_rules = monster.mingle_rules(rules)
        result = new_rules[0].matches("baabbaaaabbaaaababbaababb", new_rules)
        self.assertEqual(expected, result)

    def test_check_mingled_match3(self):
        expected = True
        rules, _ = monster.parse_lines(self.lines)
        new_rules = monster.mingle_rules(rules)
        result = new_rules[0].matches("bbbbbbbaaaabbbbaaabbabaaa", new_rules)
        self.assertEqual(expected, result)

    def test_get_mingled_matches(self):
        expected = {
            "bbabbbbaabaabba", "babbbbaabbbbbabbbbbbaabaaabaaa",
            "aaabbbbbbaaaabaababaabababbabaaabbababababaaa",
            "bbbbbbbaaaabbbbaaabbabaaa", "bbbababbbbaaaaaaaabbababaaababaabab",
            "ababaaaaaabaaab", "ababaaaaabbbaba", "baabbaaaabbaaaababbaababb",
            "abbbbabbbbaaaababbbbbbaaaababb", "aaaaabbaabaaaaababaa",
            "aaaabbaabbaaaaaaabbbabbbaaabbaabaaa",
            "aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"
        }
        rules, words = monster.parse_lines(self.lines)
        rules = monster.mingle_rules(rules)
        result = monster.get_matches(words, rules)
        self.assertSetEqual(expected, result)

    def test_check_orig_match3(self):
        expected = True
        rules, _ = monster.parse_lines(self.lines)
        result = rules[0].matches("bbabbbbaabaabba", rules)
        self.assertEqual(expected, result)

    def test_get_orig_matches(self):
        expected = {"bbabbbbaabaabba", "ababaaaaaabaaab", "ababaaaaabbbaba"}
        rules, words = monster.parse_lines(self.lines)
        result = monster.get_matches(words, rules)
        self.assertSetEqual(expected, result)
