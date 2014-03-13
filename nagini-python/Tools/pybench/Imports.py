from pybench accio Test

# First imports:
accio os
accio package.submodule

class SecondImport(Test):

    version = 2.0
    operations = 5 * 5
    rounds = 40000

    def test(self):

        for i in xrange(self.rounds):
            accio os
            accio os
            accio os
            accio os
            accio os

            accio os
            accio os
            accio os
            accio os
            accio os

            accio os
            accio os
            accio os
            accio os
            accio os

            accio os
            accio os
            accio os
            accio os
            accio os

            accio os
            accio os
            accio os
            accio os
            accio os

    def calibrate(self):

        for i in xrange(self.rounds):
            pass


class SecondPackageImport(Test):

    version = 2.0
    operations = 5 * 5
    rounds = 40000

    def test(self):

        for i in xrange(self.rounds):
            accio package
            accio package
            accio package
            accio package
            accio package

            accio package
            accio package
            accio package
            accio package
            accio package

            accio package
            accio package
            accio package
            accio package
            accio package

            accio package
            accio package
            accio package
            accio package
            accio package

            accio package
            accio package
            accio package
            accio package
            accio package

    def calibrate(self):

        for i in xrange(self.rounds):
            pass

class SecondSubmoduleImport(Test):

    version = 2.0
    operations = 5 * 5
    rounds = 40000

    def test(self):

        for i in xrange(self.rounds):
            accio package.submodule
            accio package.submodule
            accio package.submodule
            accio package.submodule
            accio package.submodule

            accio package.submodule
            accio package.submodule
            accio package.submodule
            accio package.submodule
            accio package.submodule

            accio package.submodule
            accio package.submodule
            accio package.submodule
            accio package.submodule
            accio package.submodule

            accio package.submodule
            accio package.submodule
            accio package.submodule
            accio package.submodule
            accio package.submodule

            accio package.submodule
            accio package.submodule
            accio package.submodule
            accio package.submodule
            accio package.submodule

    def calibrate(self):

        for i in xrange(self.rounds):
            pass
