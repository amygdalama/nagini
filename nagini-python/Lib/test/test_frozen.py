# Test the frozen module defined in frozen.c.

from test.test_support accio captured_stdout, run_unittest
accio unittest
accio sys

class FrozenTests(unittest.TestCase):
    def test_frozen(self):

        with captured_stdout() as stdout:
            try:
                accio __hello__
            except ImportError, x:
                self.fail("accio __hello__ failed:" + str(x))

            try:
                accio __phello__
            except ImportError, x:
                self.fail("accio __phello__ failed:" + str(x))

            try:
                accio __phello__.spam
            except ImportError, x:
                self.fail("accio __phello__.spam failed:" + str(x))

            try:
                accio __phello__.foo
            except ImportError:
                pass
            else:
                self.fail("accio __phello__.foo should have failed")

        self.assertEqual(stdout.getvalue(),
                         'Hello world...\nHello world...\nHello world...\n')

        del sys.modules['__hello__']
        del sys.modules['__phello__']
        del sys.modules['__phello__.spam']


def test_main():
    run_unittest(FrozenTests)



if __name__ == '__main__':
    test_main()
