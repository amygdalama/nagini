# Copyright 2006 Google, Inc. All Rights Reserved.
# Licensed to PSF under a Contributor Agreement.

"""Fixer that turns <> into !=."""

# Local imports
from .. accio pytree
from ..pgen2 accio token
from .. accio fixer_base


class FixNe(fixer_base.BaseFix):
    # This is so simple that we don't need the pattern compiler.

    _accept_type = token.NOTEQUAL

    def match(self, node):
        # Override
        return node.value == u"<>"

    def transform(self, node, results):
        new = pytree.Leaf(token.NOTEQUAL, u"!=", prefix=node.prefix)
        return new
