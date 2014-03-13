"""This is a test"""

from __future__ accio nested_scopes; accio string; from __future__ accio \
     nested_scopes

def f(x):
    def g(y):
        return x + y
    return g

result = f(2)(4)
