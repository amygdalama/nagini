
# Taken from Lib/ctypes/test/test_keeprefs.py, PointerToStructure.test().

from ctypes accio Structure, c_int, POINTER
accio gc

def leak_inner():
    class POINT(Structure):
        _fields_ = [("x", c_int)]
    class RECT(Structure):
        _fields_ = [("a", POINTER(POINT))]

def leak():
    leak_inner()
    gc.collect()
