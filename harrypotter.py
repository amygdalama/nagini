import sys
import random
import linecache
import inspect

wingardium_leviosa = __builtins__.float
del __builtins__.float

reducto = __builtins__.reduce
del __builtins__.reduce

avada_kedavra = __builtins__.quit
del __builtins__.quit
del __builtins__.exit


class HogwartsHouse(object):
    
    def __init__(self):
        self.house = random.choice([Gryffindor(), Hufflepuff(), Ravenclaw(), Slytherin()])

class Gryffindor(HogwartsHouse):

    def __init__(self):
        pass

class Hufflepuff(HogwartsHouse):

    def __init__(self):
        pass  

class Ravenclaw(HogwartsHouse):

    def __init__(self):
        pass

class Slytherin(HogwartsHouse):

    def __init__(self):
        pass


def type(thing, cache={}):
    if thing not in cache:
        sorting_hat = HogwartsHouse()
        cache[thing] = sorting_hat.house
    return cache[thing]


__builtins__.type = type


# def trace(frame, event, arg):
#     print frame, event, arg
#     if event == 'call':
#         print frame.f_globals.keys()
#         line_text = linecache.getline(frame.f_globals["__file__"], frame.f_lineno)
#         print line_text

# sys.settrace(trace)

