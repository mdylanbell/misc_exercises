import unittest
import re

from textblocking import invert_text, invert_text_strict

class textblocking_test(unittest.TestCase):

    ## Test basic version

    def test_single_line(self):
        self.assertEqual(
            ['A', 'B', 'C'],
            invert_text(['ABC'])
        )

    def test_long_string(self):
        self.assertEqual(
            ['A',
             'A',
             'A',
             'A',
             'A',
             'A',
             'A',
             'A',
             'A',
             'A',
             'A',
             'A',
             'A'],
            invert_text(['AAAAAAAAAAAAA'])
        )

    def test_multipe_lines(self):
        self.assertEqual(
            ['AHO',
             'BIP',
             'CJQ',
             'DKR',
             'ELS',
             'FMT',
             'GNU'
            ],
            invert_text(['ABCDEFG', 'HIJKLMN', 'OPQRSTU'])
        )

    def test_vertical_to_horizontal(self):
        self.assertEqual(
            ['AAAAA'],
            invert_text(['A', 'A', 'A', 'A', 'A'])
        )

    ## Test strict version

    def test_strict_single_line(self):
        self.assertEqual(
            ['A', 'B', 'C'],
            invert_text_strict(['ABC'])
        )

    def test_strict_multipe_lines(self):
        self.assertEqual(
            ['AHO',
             'BIP',
             'CJQ',
             'DKR',
             'ELS',
             'FMT',
             'GNU'
            ],
            invert_text_strict(['ABCDEFG', 'HIJKLMN', 'OPQRSTU'])
        )

    def test_strict_lowercase_fail(self):
        self.assertRaises(
            ValueError,
            invert_text_strict, ['abc']
        )

    def test_strict_lowercase_fail_message(self):
        self.assertRaisesRegexp(
            ValueError, re.escape('List argument contains improperly formatted elements (case) -- line 1'),
            invert_text_strict, ['abc']
        )

    def test_strict_mismatch_length_fail(self):
        self.assertRaises(
            ValueError,
            invert_text_strict, ['ABC', 'DE']
        )

    def test_strict_mismatch_length_fail_message(self):
        self.assertRaisesRegexp(
            ValueError, re.escape('List argument contains improperly formatted elements (line length) -- line 2'),
            invert_text_strict, ['ABC', 'DE']
        )

    def test_strict_too_many_elements_fail(self):
        self.assertRaises(
            ValueError,
            invert_text_strict, [str(x) for x in range(0, 51)]
        )

    def test_strict_too_many_elements_fail_message(self):
        self.assertRaisesRegexp(
            ValueError, 'List argument contains too many elements',
            invert_text_strict, [str(x) for x in range(0, 51)]
        )

if __name__ == '__main__':
    unittest.main()
