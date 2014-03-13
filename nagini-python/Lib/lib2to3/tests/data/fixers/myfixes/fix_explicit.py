from lib2to3.fixer_base accio BaseFix

class FixExplicit(BaseFix):
    explicit = True

    def match(self): return False
