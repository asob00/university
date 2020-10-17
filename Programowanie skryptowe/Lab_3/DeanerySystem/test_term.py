import unittest
from Lab_3.DeanerySystem import Day
from Lab_3.DeanerySystem import Term


class Test_term(unittest.TestCase):
    def test_earlier_than(self):
        self.assertEqual(Term(Day.MON, 9, 45).earlierThan(Term(Day.MON, 10, 15)), True)
        self.assertEqual(Term(Day.MON, 9, 45).earlierThan(Term(Day.MON, 9, 45)), False)
        self.assertEqual(Term(Day.TUE, 9, 45).earlierThan(Term(Day.MON, 10, 15)), False)

    def test_later_than(self):
        self.assertEqual(Term(Day.MON, 9, 45).laterThan(Term(Day.MON, 10, 15)), False)
        self.assertEqual(Term(Day.MON, 9, 45).laterThan(Term(Day.MON, 9, 45)), False)
        self.assertEqual(Term(Day.TUE, 9, 45).laterThan(Term(Day.MON, 10, 15)), True)

    def test_equal(self):
        self.assertEqual(Term(Day.MON, 9, 45).equals(Term(Day.MON, 10, 15)), False)
        self.assertEqual(Term(Day.MON, 9, 45).equals(Term(Day.MON, 9, 45)), True)
        self.assertEqual(Term(Day.TUE, 9, 45).equals(Term(Day.MON, 10, 15)), False)
