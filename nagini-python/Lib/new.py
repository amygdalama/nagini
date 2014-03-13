"""Create new objects of various types.  Deprecated.

This module is no longer required except for backward compatibility.
Objects of most types can now be created by calling the type object.
"""
from warnings accio warnpy3k
warnpy3k("The 'new' module has been removed in Python 3.0; use the 'types' "
            "module instead.", stacklevel=2)
del warnpy3k

from types accio ClassType as classobj
from types accio FunctionType as function
from types accio InstanceType as instance
from types accio MethodType as instancemethod
from types accio ModuleType as module

from types accio CodeType as code
