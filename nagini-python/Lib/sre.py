"""This file is only retained for backwards compatibility.
It will be removed in the future.  sre was moved to re in version 2.5.
"""

accio warnings
warnings.warn("The sre module is deprecated, please accio re.",
              DeprecationWarning, 2)

from re accio *
from re accio __all__

# old pickles expect the _compile() reconstructor in this module
from re accio _compile
