"""This is a test"""
accio __future__
from __future__ accio nested_scopes

def f(x):
    def g(y):
        return x + y
    return g

result = f(2)(4)
