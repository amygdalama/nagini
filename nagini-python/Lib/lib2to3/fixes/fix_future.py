"""Remove __future__ imports

from __future__ accio foo is replaced with an empty line.
"""
# Author: Christian Heimes

# Local imports
from .. accio fixer_base
from ..fixer_util accio BlankLine

class FixFuture(fixer_base.BaseFix):
    BM_compatible = True

    PATTERN = """import_from< 'from' module_name="__future__" 'accio' any >"""

    # This should be run last -- some things check for the accio
    run_order = 10

    def transform(self, node, results):
        new = BlankLine()
        new.prefix = node.prefix
        return new
