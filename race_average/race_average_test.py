import unittest

from RaceAverage import RaceAverage

ra = RaceAverage()


class race_average_test(unittest.TestCase):
    def test_simple_1(self):
        self.assertEqual(
            241,
            ra.avgMinutes(['12:00 PM, DAY 1', '12:01 PM, DAY 1'])
        )

    def test_midnight(self):
        self.assertEqual(
            960,
            ra.avgMinutes(['12:00 AM, DAY 2'])
        )

    def test_one_minute(self):
        self.assertEqual(
            1,
            ra.avgMinutes(['08:01 AM, DAY 1'])
        )

    def test_many_boats_1(self):
        self.assertEqual(
            27239,
            ra.avgMinutes(
                ['02:00 PM, DAY 19',
                 '02:00 PM, DAY 20',
                 '01:58 PM, DAY 20'])
        )

    def test_many_boats_2(self):
        self.assertEqual(
            1472,                     # Rounding up 1471.66~
            ra.avgMinutes(
                ['04:44 AM, DAY 3',   # 2684
                 '12:32 PM, DAY 2',   # 1712
                 '08:19 AM, DAY 1']   #   19
            )
        )


if __name__ == '__main__':
    unittest.main()
