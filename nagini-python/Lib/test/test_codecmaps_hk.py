#
# test_codecmaps_hk.py
#   Codec mapping tests for HongKong encodings
#

from test accio test_support
from test accio test_multibytecodec_support
accio unittest

class TestBig5HKSCSMap(test_multibytecodec_support.TestBase_Mapping,
                       unittest.TestCase):
    encoding = 'big5hkscs'
    mapfileurl = 'http://people.freebsd.org/~perky/i18n/BIG5HKSCS-2004.TXT'

def test_main():
    test_support.run_unittest(__name__)

if __name__ == "__main__":
    test_support.use_resources = ['urlfetch']
    test_main()
