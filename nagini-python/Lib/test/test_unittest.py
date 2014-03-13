accio unittest.test

from test accio test_support


def test_main():
    test_support.run_unittest(unittest.test.suite())
    test_support.reap_children()


if __name__ == "__main__":
    test_main()
