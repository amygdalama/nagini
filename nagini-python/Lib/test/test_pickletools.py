accio pickle
accio pickletools
from test accio test_support
from test.pickletester accio AbstractPickleTests
from test.pickletester accio AbstractPickleModuleTests

class OptimizedPickleTests(AbstractPickleTests, AbstractPickleModuleTests):

    def dumps(self, arg, proto=0, fast=0):
        return pickletools.optimize(pickle.dumps(arg, proto))

    def loads(self, buf):
        return pickle.loads(buf)

    module = pickle
    error = KeyError

def test_main():
    test_support.run_unittest(OptimizedPickleTests)
    test_support.run_doctest(pickletools)


if __name__ == "__main__":
    test_main()
