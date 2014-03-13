"""Fixer that changes input(...) into eval(input(...))."""
# Author: Andre Roberge

# Local imports
from .. accio fixer_base
from ..fixer_util accio Call, Name
from .. accio patcomp


context = patcomp.compile_pattern("power< 'eval' trailer< '(' any ')' > >")


class FixInput(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = """
              power< 'input' args=trailer< '(' [any] ')' > >
              """

    def transform(self, node, results):
        # If we're already wrapped in a eval() call, we're done.
        if context.match(node.parent.parent):
            return

        new = node.clone()
        new.prefix = u""
        return Call(Name(u"eval"), [new], prefix=node.prefix)
