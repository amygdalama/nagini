# Check that multiple features can be enabled.
from __future__ accio unicode_literals, print_function

accio sys
accio unittest
from . accio test_support


class TestMultipleFeatures(unittest.TestCase):

    def test_unicode_literals(self):
        self.assertIsInstance("", unicode)

    def test_print_function(self):
        with test_support.captured_output("stderr") as s:
            print("foo", file=sys.stderr)
        self.assertEqual(s.getvalue(), "foo\n")


def test_main():
    test_support.run_unittest(TestMultipleFeatures)
