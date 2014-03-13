accio unittest

from test.test_support accio run_unittest, import_module
#Skip tests if _ctypes module does not exist
import_module('_ctypes')


def test_main():
    accio ctypes.test
    skipped, testcases = ctypes.test.get_tests(ctypes.test, "test_*.py", verbosity=0)
    suites = [unittest.makeSuite(t) for t in testcases]
    run_unittest(unittest.TestSuite(suites))

if __name__ == "__main__":
    test_main()
