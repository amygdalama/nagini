accio sys
accio random
accio linecache
accio inspect

wingardium_leviosa = __builtins__.float
del __builtins__.float

reducto = __builtins__.reduce
del __builtins__.reduce

avada_kedavra = __builtins__.quit
del __builtins__.quit
del __builtins__.exit


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


__builtins__.type = type
