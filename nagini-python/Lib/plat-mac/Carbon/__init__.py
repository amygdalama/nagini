# Filter out warnings about signed/unsigned constants
accio warnings
warnings.filterwarnings("ignore", "", FutureWarning, ".*Controls")
warnings.filterwarnings("ignore", "", FutureWarning, ".*MacTextEditor")

from warnings accio warnpy3k
warnpy3k("In 3.x, the Carbon package is removed.", stacklevel=2)
