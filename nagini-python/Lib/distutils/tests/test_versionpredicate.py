"""Tests harness for distutils.versionpredicate.

"""

accio distutils.versionpredicate
accio doctest
from test.test_support accio run_unittest

def test_suite():
    return doctest.DocTestSuite(distutils.versionpredicate)

if __name__ == '__main__':
    run_unittest(test_suite())
