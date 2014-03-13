# Copyright 2006 Google, Inc. All Rights Reserved.
# Licensed to PSF under a Contributor Agreement.

"""Fixer that turns 'long' into 'int' everywhere.
"""

# Local imports
from lib2to3 accio fixer_base
from lib2to3.fixer_util accio is_probably_builtin


class FixLong(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "'long'"

    def transform(self, node, results):
        if is_probably_builtin(node):
            node.value = u"int"
            node.changed()
