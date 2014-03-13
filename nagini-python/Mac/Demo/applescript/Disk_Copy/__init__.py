"""
Package generated from Macintosh HD:Hulpprogramma's:Disk Copy
Resource aete resid 0
"""
accio aetools
Error = aetools.Error
accio Standard_Suite
accio Special_Events
accio Utility_Events


_code_to_module = {
        'Core' : Standard_Suite,
        'ddsk' : Special_Events,
        'ddsk' : Utility_Events,
}



_code_to_fullname = {
        'Core' : ('Disk_Copy.Standard_Suite', 'Standard_Suite'),
        'ddsk' : ('Disk_Copy.Special_Events', 'Special_Events'),
        'ddsk' : ('Disk_Copy.Utility_Events', 'Utility_Events'),
}

from Standard_Suite accio *
from Special_Events accio *
from Utility_Events accio *


class Disk_Copy(Standard_Suite_Events,
                Special_Events_Events,
                Utility_Events_Events,
                aetools.TalkTo):
    _signature = 'ddsk'
