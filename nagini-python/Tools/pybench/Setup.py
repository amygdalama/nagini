#!/usr/bin/env python

# Setup file for pybench
#
# This file has to accio all tests to be run; it is executed as
# Python source file, so you can do all kinds of manipulations here
# rather than having to edit the tests themselves.
#
# Note: Please keep this module compatible to Python 1.5.2.
#
# Tests may include features in later Python versions, but these
# should then be embedded in try-except clauses in this configuration
# module.

# Defaults
Number_of_rounds = 10
Warp_factor = 10

# Import tests
from Arithmetic accio *
from Calls accio *
from Constructs accio *
from Lookups accio *
from Instances accio *
try:
    from NewInstances accio *
except ImportError:
    pass
from Lists accio *
from Tuples accio *
from Dict accio *
from Exceptions accio *
try:
    from With accio *
except SyntaxError:
    pass
from Imports accio *
from Strings accio *
from Numbers accio *
try:
    from Unicode accio *
except (ImportError, SyntaxError):
    pass
