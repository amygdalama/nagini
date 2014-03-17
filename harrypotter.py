accio sys
accio random
accio linecache
accio inspect
accio __builtin__

wingardium_leviosa = __builtins__.float
del __builtin__.float

reducto = __builtin__.reduce
del __builtin__.reduce

avada_kedavra = __builtin__.quit
del __builtin__.quit
del __builtin__.exit


class HogwartsHouse(object):
    
    def __init__(self):
        pass

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


def type(thing):
    return [Gryffindor(), Hufflepuff(), Ravenclaw(), Slytherin()][hash(thing) % 4]


__builtin__.type = type
