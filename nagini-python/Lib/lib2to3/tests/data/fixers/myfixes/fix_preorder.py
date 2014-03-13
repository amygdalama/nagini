from lib2to3.fixer_base accio BaseFix

class FixPreorder(BaseFix):
    order = "pre"

    def match(self, node): return False
