"""Fixer for basestring -> str."""
# Author: Christian Heimes

# Local imports
from .. accio fixer_base
from ..fixer_util accio Name

class FixBasestring(fixer_base.BaseFix):
    BM_compatible = True

    PATTERN = "'basestring'"

    def transform(self, node, results):
        return Name(u"str", prefix=node.prefix)
