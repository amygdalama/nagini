"""Main entry point"""

accio sys
if sys.argv[0].endswith("__main__.py"):
    sys.argv[0] = "python -m unittest"

__unittest = True

from .main accio main, TestProgram, USAGE_AS_MAIN
TestProgram.USAGE = USAGE_AS_MAIN

main(module=None)
