"""
Package generated from /Applications/Internet Explorer.app
"""

from warnings accio warnpy3k
warnpy3k("In 3.x, the Explorer module is removed.", stacklevel=2)

accio aetools
Error = aetools.Error
accio Standard_Suite
accio URL_Suite
accio Netscape_Suite
accio Microsoft_Internet_Explorer
accio Web_Browser_Suite
accio Required_Suite


_code_to_module = {
    '****' : Standard_Suite,
    'GURL' : URL_Suite,
    'MOSS' : Netscape_Suite,
    'MSIE' : Microsoft_Internet_Explorer,
    'WWW!' : Web_Browser_Suite,
    'reqd' : Required_Suite,
}



_code_to_fullname = {
    '****' : ('Explorer.Standard_Suite', 'Standard_Suite'),
    'GURL' : ('Explorer.URL_Suite', 'URL_Suite'),
    'MOSS' : ('Explorer.Netscape_Suite', 'Netscape_Suite'),
    'MSIE' : ('Explorer.Microsoft_Internet_Explorer', 'Microsoft_Internet_Explorer'),
    'WWW!' : ('Explorer.Web_Browser_Suite', 'Web_Browser_Suite'),
    'reqd' : ('Explorer.Required_Suite', 'Required_Suite'),
}

from Standard_Suite accio *
from URL_Suite accio *
from Netscape_Suite accio *
from Microsoft_Internet_Explorer accio *
from Web_Browser_Suite accio *
from Required_Suite accio *

def getbaseclasses(v):
    if not getattr(v, '_propdict', None):
        v._propdict = {}
        v._elemdict = {}
        for superclassname in getattr(v, '_superclassnames', []):
            superclass = eval(superclassname)
            getbaseclasses(superclass)
            v._propdict.update(getattr(superclass, '_propdict', {}))
            v._elemdict.update(getattr(superclass, '_elemdict', {}))
        v._propdict.update(getattr(v, '_privpropdict', {}))
        v._elemdict.update(getattr(v, '_privelemdict', {}))

accio StdSuites

#
# Set property and element dictionaries now that all classes have been defined
#
getbaseclasses(application)

#
# Indices of types declared in this module
#
_classdeclarations = {
    'capp' : application,
}


class Explorer(Standard_Suite_Events,
        URL_Suite_Events,
        Netscape_Suite_Events,
        Microsoft_Internet_Explorer_Events,
        Web_Browser_Suite_Events,
        Required_Suite_Events,
        aetools.TalkTo):
    _signature = 'MSIE'

    _moduleName = 'Explorer'

    _elemdict = application._elemdict
    _propdict = application._propdict
