from lib2to3.fixer_base accio BaseFix

class FixFirst(BaseFix):
    run_order = 1

    def match(self, node): return False
