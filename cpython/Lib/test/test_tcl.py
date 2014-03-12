import unittest
import sys
import os
from test import test_support
from subprocess import Popen, PIPE

# Skip this test if the _tkinter module wasn't built.
_tkinter = test_support.import_module('_tkinter')

from Tkinter import Tcl
from _tkinter import TclError

try:
    from _testcapi import INT_MAX, PY_SSIZE_T_MAX
except ImportError:
    INT_MAX = PY_SSIZE_T_MAX = sys.maxsize

tcl_version = _tkinter.TCL_VERSION.split('.')
try:
    for i in range(len(tcl_version)):
        tcl_version[i] = int(tcl_version[i])
except ValueError:
    pass
tcl_version = tuple(tcl_version)

_tk_patchlevel = None
def get_tk_patchlevel():
    global _tk_patchlevel
    if _tk_patchlevel is None:
        tcl = Tcl()
        patchlevel = []
        for x in tcl.call('info', 'patchlevel').split('.'):
            try:
                x = int(x, 10)
            except ValueError:
                x = -1
            patchlevel.append(x)
        _tk_patchlevel = tuple(patchlevel)
    return _tk_patchlevel


class TkinterTest(unittest.TestCase):

    def testFlattenLen(self):
        # flatten(<object with no length>)
        self.assertRaises(TypeError, _tkinter._flatten, True)


class TclTest(unittest.TestCase):

    def setUp(self):
        self.interp = Tcl()
        self.wantobjects = self.interp.tk.wantobjects()

    def testEval(self):
        tcl = self.interp
        tcl.eval('set a 1')
        self.assertEqual(tcl.eval('set a'),'1')

    def testEvalException(self):
        tcl = self.interp
        self.assertRaises(TclError,tcl.eval,'set a')

    def testEvalException2(self):
        tcl = self.interp
        self.assertRaises(TclError,tcl.eval,'this is wrong')

    def testCall(self):
        tcl = self.interp
        tcl.call('set','a','1')
        self.assertEqual(tcl.call('set','a'),'1')

    def testCallException(self):
        tcl = self.interp
        self.assertRaises(TclError,tcl.call,'set','a')

    def testCallException2(self):
        tcl = self.interp
        self.assertRaises(TclError,tcl.call,'this','is','wrong')

    def testSetVar(self):
        tcl = self.interp
        tcl.setvar('a','1')
        self.assertEqual(tcl.eval('set a'),'1')

    def testSetVarArray(self):
        tcl = self.interp
        tcl.setvar('a(1)','1')
        self.assertEqual(tcl.eval('set a(1)'),'1')

    def testGetVar(self):
        tcl = self.interp
        tcl.eval('set a 1')
        self.assertEqual(tcl.getvar('a'),'1')

    def testGetVarArray(self):
        tcl = self.interp
        tcl.eval('set a(1) 1')
        self.assertEqual(tcl.getvar('a(1)'),'1')

    def testGetVarException(self):
        tcl = self.interp
        self.assertRaises(TclError,tcl.getvar,'a')

    def testGetVarArrayException(self):
        tcl = self.interp
        self.assertRaises(TclError,tcl.getvar,'a(1)')

    def testUnsetVar(self):
        tcl = self.interp
        tcl.setvar('a',1)
        self.assertEqual(tcl.eval('info exists a'),'1')
        tcl.unsetvar('a')
        self.assertEqual(tcl.eval('info exists a'),'0')

    def testUnsetVarArray(self):
        tcl = self.interp
        tcl.setvar('a(1)',1)
        tcl.setvar('a(2)',2)
        self.assertEqual(tcl.eval('info exists a(1)'),'1')
        self.assertEqual(tcl.eval('info exists a(2)'),'1')
        tcl.unsetvar('a(1)')
        self.assertEqual(tcl.eval('info exists a(1)'),'0')
        self.assertEqual(tcl.eval('info exists a(2)'),'1')

    def testUnsetVarException(self):
        tcl = self.interp
        self.assertRaises(TclError,tcl.unsetvar,'a')

    def testEvalFile(self):
        tcl = self.interp
        filename = "testEvalFile.tcl"
        fd = open(filename,'w')
        script = """set a 1
        set b 2
        set c [ expr $a + $b ]
        """
        fd.write(script)
        fd.close()
        tcl.evalfile(filename)
        os.remove(filename)
        self.assertEqual(tcl.eval('set a'),'1')
        self.assertEqual(tcl.eval('set b'),'2')
        self.assertEqual(tcl.eval('set c'),'3')

    def test_evalfile_null_in_result(self):
        tcl = self.interp
        with open(test_support.TESTFN, 'wb') as f:
            self.addCleanup(test_support.unlink, test_support.TESTFN)
            f.write("""
            set a "a\0b"
            set b "a\\0b"
            """)
        tcl.evalfile(test_support.TESTFN)
        self.assertEqual(tcl.eval('set a'), 'a\xc0\x80b')
        self.assertEqual(tcl.eval('set b'), 'a\xc0\x80b')

    def testEvalFileException(self):
        tcl = self.interp
        filename = "doesnotexists"
        try:
            os.remove(filename)
        except Exception,e:
            pass
        self.assertRaises(TclError,tcl.evalfile,filename)

    def testPackageRequireException(self):
        tcl = self.interp
        self.assertRaises(TclError,tcl.eval,'package require DNE')

    @unittest.skipUnless(sys.platform == 'win32', "only applies to Windows")
    def testLoadWithUNC(self):
        # Build a UNC path from the regular path.
        # Something like
        #   \\%COMPUTERNAME%\c$\python27\python.exe

        fullname = os.path.abspath(sys.executable)
        if fullname[1] != ':':
            self.skipTest('unusable path: %r' % fullname)
        unc_name = r'\\%s\%s$\%s' % (os.environ['COMPUTERNAME'],
                                    fullname[0],
                                    fullname[3:])

        with test_support.EnvironmentVarGuard() as env:
            env.unset("TCL_LIBRARY")
            cmd = '%s -c "import Tkinter; print Tkinter"' % (unc_name,)

            try:
                p = Popen(cmd, stdout=PIPE, stderr=PIPE)
            except WindowsError as e:
                if e.winerror == 5:
                    self.skipTest('Not permitted to start the child process')
                else:
                    raise

            out_data, err_data = p.communicate()

            msg = '\n\n'.join(['"Tkinter.py" not in output',
                               'Command:', cmd,
                               'stdout:', out_data,
                               'stderr:', err_data])

            self.assertIn('Tkinter.py', out_data, msg)

            self.assertEqual(p.wait(), 0, 'Non-zero exit code')


    def test_exprstring(self):
        tcl = self.interp
        tcl.call('set', 'a', 3)
        tcl.call('set', 'b', 6)
        def check(expr, expected):
            result = tcl.exprstring(expr)
            self.assertEqual(result, expected)
            self.assertIsInstance(result, str)

        self.assertRaises(TypeError, tcl.exprstring)
        self.assertRaises(TypeError, tcl.exprstring, '8.2', '+6')
        self.assertRaises(TclError, tcl.exprstring, 'spam')
        check('', '0')
        check('8.2 + 6', '14.2')
        check('3.1 + $a', '6.1')
        check('2 + "$a.$b"', '5.6')
        check('4*[llength "6 2"]', '8')
        check('{word one} < "word $a"', '0')
        check('4*2 < 7', '0')
        check('hypot($a, 4)', '5.0')
        check('5 / 4', '1')
        check('5 / 4.0', '1.25')
        check('5 / ( [string length "abcd"] + 0.0 )', '1.25')
        check('20.0/5.0', '4.0')
        check('"0x03" > "2"', '1')
        check('[string length "a\xc2\xbd\xe2\x82\xac"]', '3')
        check(r'[string length "a\xbd\u20ac"]', '3')
        check('"abc"', 'abc')
        check('"a\xc2\xbd\xe2\x82\xac"', 'a\xc2\xbd\xe2\x82\xac')
        check(r'"a\xbd\u20ac"', 'a\xc2\xbd\xe2\x82\xac')
        check(r'"a\0b"', 'a\xc0\x80b')
        if tcl_version >= (8, 5):
            check('2**64', str(2**64))

    def test_exprdouble(self):
        tcl = self.interp
        tcl.call('set', 'a', 3)
        tcl.call('set', 'b', 6)
        def check(expr, expected):
            result = tcl.exprdouble(expr)
            self.assertEqual(result, expected)
            self.assertIsInstance(result, float)

        self.assertRaises(TypeError, tcl.exprdouble)
        self.assertRaises(TypeError, tcl.exprdouble, '8.2', '+6')
        self.assertRaises(TclError, tcl.exprdouble, 'spam')
        check('', 0.0)
        check('8.2 + 6', 14.2)
        check('3.1 + $a', 6.1)
        check('2 + "$a.$b"', 5.6)
        check('4*[llength "6 2"]', 8.0)
        check('{word one} < "word $a"', 0.0)
        check('4*2 < 7', 0.0)
        check('hypot($a, 4)', 5.0)
        check('5 / 4', 1.0)
        check('5 / 4.0', 1.25)
        check('5 / ( [string length "abcd"] + 0.0 )', 1.25)
        check('20.0/5.0', 4.0)
        check('"0x03" > "2"', 1.0)
        check('[string length "a\xc2\xbd\xe2\x82\xac"]', 3.0)
        check(r'[string length "a\xbd\u20ac"]', 3.0)
        self.assertRaises(TclError, tcl.exprdouble, '"abc"')
        if tcl_version >= (8, 5):
            check('2**64', float(2**64))

    def test_exprlong(self):
        tcl = self.interp
        tcl.call('set', 'a', 3)
        tcl.call('set', 'b', 6)
        def check(expr, expected):
            result = tcl.exprlong(expr)
            self.assertEqual(result, expected)
            self.assertIsInstance(result, int)

        self.assertRaises(TypeError, tcl.exprlong)
        self.assertRaises(TypeError, tcl.exprlong, '8.2', '+6')
        self.assertRaises(TclError, tcl.exprlong, 'spam')
        check('', 0)
        check('8.2 + 6', 14)
        check('3.1 + $a', 6)
        check('2 + "$a.$b"', 5)
        check('4*[llength "6 2"]', 8)
        check('{word one} < "word $a"', 0)
        check('4*2 < 7', 0)
        check('hypot($a, 4)', 5)
        check('5 / 4', 1)
        check('5 / 4.0', 1)
        check('5 / ( [string length "abcd"] + 0.0 )', 1)
        check('20.0/5.0', 4)
        check('"0x03" > "2"', 1)
        check('[string length "a\xc2\xbd\xe2\x82\xac"]', 3)
        check(r'[string length "a\xbd\u20ac"]', 3)
        self.assertRaises(TclError, tcl.exprlong, '"abc"')
        if tcl_version >= (8, 5):
            self.assertRaises(TclError, tcl.exprlong, '2**64')

    def test_exprboolean(self):
        tcl = self.interp
        tcl.call('set', 'a', 3)
        tcl.call('set', 'b', 6)
        def check(expr, expected):
            result = tcl.exprboolean(expr)
            self.assertEqual(result, expected)
            self.assertIsInstance(result, int)
            self.assertNotIsInstance(result, bool)

        self.assertRaises(TypeError, tcl.exprboolean)
        self.assertRaises(TypeError, tcl.exprboolean, '8.2', '+6')
        self.assertRaises(TclError, tcl.exprboolean, 'spam')
        check('', False)
        for value in ('0', 'false', 'no', 'off'):
            check(value, False)
            check('"%s"' % value, False)
            check('{%s}' % value, False)
        for value in ('1', 'true', 'yes', 'on'):
            check(value, True)
            check('"%s"' % value, True)
            check('{%s}' % value, True)
        check('8.2 + 6', True)
        check('3.1 + $a', True)
        check('2 + "$a.$b"', True)
        check('4*[llength "6 2"]', True)
        check('{word one} < "word $a"', False)
        check('4*2 < 7', False)
        check('hypot($a, 4)', True)
        check('5 / 4', True)
        check('5 / 4.0', True)
        check('5 / ( [string length "abcd"] + 0.0 )', True)
        check('20.0/5.0', True)
        check('"0x03" > "2"', True)
        check('[string length "a\xc2\xbd\xe2\x82\xac"]', True)
        check(r'[string length "a\xbd\u20ac"]', True)
        self.assertRaises(TclError, tcl.exprboolean, '"abc"')
        if tcl_version >= (8, 5):
            check('2**64', True)

    def test_passing_values(self):
        def passValue(value):
            return self.interp.call('set', '_', value)

        self.assertEqual(passValue(True), True if self.wantobjects else '1')
        self.assertEqual(passValue(False), False if self.wantobjects else '0')
        self.assertEqual(passValue('string'), 'string')
        self.assertEqual(passValue('string\xbd'), 'string\xbd')
        self.assertEqual(passValue('string\xe2\x82\xac'), u'string\u20ac')
        self.assertEqual(passValue(u'string'), u'string')
        self.assertEqual(passValue(u'string\xbd'), u'string\xbd')
        self.assertEqual(passValue(u'string\u20ac'), u'string\u20ac')
        self.assertEqual(passValue('str\x00ing'), 'str\x00ing')
        self.assertEqual(passValue('str\xc0\x80ing'), 'str\x00ing')
        self.assertEqual(passValue(u'str\x00ing'), u'str\x00ing')
        self.assertEqual(passValue(u'str\x00ing\xbd'), u'str\x00ing\xbd')
        self.assertEqual(passValue(u'str\x00ing\u20ac'), u'str\x00ing\u20ac')
        for i in (0, 1, -1, int(2**31-1), int(-2**31)):
            self.assertEqual(passValue(i), i if self.wantobjects else str(i))
        for f in (0.0, 1.0, -1.0, 1//3, 1/3.0,
                  sys.float_info.min, sys.float_info.max,
                  -sys.float_info.min, -sys.float_info.max):
            if self.wantobjects:
                self.assertEqual(passValue(f), f)
            else:
                self.assertEqual(float(passValue(f)), f)
        if self.wantobjects:
            f = passValue(float('nan'))
            self.assertNotEqual(f, f)
            self.assertEqual(passValue(float('inf')), float('inf'))
            self.assertEqual(passValue(-float('inf')), -float('inf'))
        else:
            f = float(passValue(float('nan')))
            self.assertNotEqual(f, f)
            self.assertEqual(float(passValue(float('inf'))), float('inf'))
            self.assertEqual(float(passValue(-float('inf'))), -float('inf'))
        self.assertEqual(passValue((1, '2', (3.4,))),
                         (1, '2', (3.4,)) if self.wantobjects else '1 2 3.4')

    def test_user_command(self):
        result = []
        def testfunc(arg):
            result.append(arg)
            return arg
        self.interp.createcommand('testfunc', testfunc)
        self.addCleanup(self.interp.tk.deletecommand, 'testfunc')
        def check(value, expected, expected2=None, eq=self.assertEqual):
            if expected2 is None:
                expected2 = expected
            del result[:]
            r = self.interp.call('testfunc', value)
            self.assertEqual(len(result), 1)
            self.assertIsInstance(result[0], (str, unicode))
            eq(result[0], expected2)
            self.assertIsInstance(r, (str, unicode))
            eq(r, expected2)
        def float_eq(actual, expected):
            expected = float(expected)
            self.assertAlmostEqual(float(actual), expected,
                                   delta=abs(expected) * 1e-10)
        def nan_eq(actual, expected):
            actual = float(actual)
            self.assertNotEqual(actual, actual)

        check(True, '1')
        check(False, '0')
        check('string', 'string')
        check('string\xbd', 'string\xbd')
        check('string\xe2\x82\xac', 'string\xe2\x82\xac', u'string\u20ac')
        check(u'string', u'string')
        check(u'string\xbd', 'string\xc2\xbd', u'string\xbd')
        check(u'string\u20ac', 'string\xe2\x82\xac', u'string\u20ac')
        check('str\xc0\x80ing', 'str\xc0\x80ing', u'str\x00ing')
        check('str\xc0\x80ing\xe2\x82\xac', 'str\xc0\x80ing\xe2\x82\xac', u'str\x00ing\u20ac')
        check(u'str\x00ing', 'str\xc0\x80ing', u'str\x00ing')
        check(u'str\x00ing\xbd', 'str\xc0\x80ing\xc2\xbd', u'str\x00ing\xbd')
        check(u'str\x00ing\u20ac', 'str\xc0\x80ing\xe2\x82\xac', u'str\x00ing\u20ac')
        for i in (0, 1, -1, 2**31-1, -2**31):
            check(i, str(i))
        for f in (0.0, 1.0, -1.0):
            check(f, repr(f))
        for f in (1/3.0, sys.float_info.min, sys.float_info.max,
                  -sys.float_info.min, -sys.float_info.max):
            check(f, f, eq=float_eq)
        check(float('inf'), 'Inf', eq=float_eq)
        check(-float('inf'), '-Inf', eq=float_eq)
        check(float('nan'), 'NaN', eq=nan_eq)
        check((), '')
        check((1, (2,), (3, 4), '5 6', ()), '1 2 {3 4} {5 6} {}')

    def test_splitlist(self):
        splitlist = self.interp.tk.splitlist
        call = self.interp.tk.call
        self.assertRaises(TypeError, splitlist)
        self.assertRaises(TypeError, splitlist, 'a', 'b')
        self.assertRaises(TypeError, splitlist, 2)
        testcases = [
            ('2', ('2',)),
            ('', ()),
            ('{}', ('',)),
            ('""', ('',)),
            ('a\n b\t\r c\n ', ('a', 'b', 'c')),
            (u'a\n b\t\r c\n ', ('a', 'b', 'c')),
            ('a \xe2\x82\xac', ('a', '\xe2\x82\xac')),
            (u'a \u20ac', ('a', '\xe2\x82\xac')),
            ('a\xc0\x80b c\xc0\x80d', ('a\xc0\x80b', 'c\xc0\x80d')),
            ('a {b c}', ('a', 'b c')),
            (r'a b\ c', ('a', 'b c')),
            (('a', 'b c'), ('a', 'b c')),
            ('a 2', ('a', '2')),
            (('a', 2), ('a', 2)),
            ('a 3.4', ('a', '3.4')),
            (('a', 3.4), ('a', 3.4)),
            ((), ()),
            (call('list', 1, '2', (3.4,)),
                (1, '2', (3.4,)) if self.wantobjects else
                ('1', '2', '3.4')),
        ]
        if tcl_version >= (8, 5):
            if not self.wantobjects:
                expected = ('12', '\xe2\x82\xac', '\xe2\x82\xac', '3.4')
            elif get_tk_patchlevel() < (8, 5, 5):
                # Before 8.5.5 dicts were converted to lists through string
                expected = ('12', u'\u20ac', u'\u20ac', '3.4')
            else:
                expected = (12, u'\u20ac', u'\u20ac', (3.4,))
            testcases += [
                (call('dict', 'create', 12, u'\u20ac', '\xe2\x82\xac', (3.4,)),
                    expected),
            ]
        for arg, res in testcases:
            self.assertEqual(splitlist(arg), res)
        self.assertRaises(TclError, splitlist, '{')

    def test_split(self):
        split = self.interp.tk.split
        call = self.interp.tk.call
        self.assertRaises(TypeError, split)
        self.assertRaises(TypeError, split, 'a', 'b')
        self.assertRaises(TypeError, split, 2)
        testcases = [
            ('2', '2'),
            ('', ''),
            ('{}', ''),
            ('""', ''),
            ('{', '{'),
            ('a\n b\t\r c\n ', ('a', 'b', 'c')),
            (u'a\n b\t\r c\n ', ('a', 'b', 'c')),
            ('a \xe2\x82\xac', ('a', '\xe2\x82\xac')),
            (u'a \u20ac', ('a', '\xe2\x82\xac')),
            ('a\xc0\x80b', 'a\xc0\x80b'),
            ('a\xc0\x80b c\xc0\x80d', ('a\xc0\x80b', 'c\xc0\x80d')),
            ('a {b c}', ('a', ('b', 'c'))),
            (r'a b\ c', ('a', ('b', 'c'))),
            (('a', 'b c'), ('a', ('b', 'c'))),
            (('a', u'b c'), ('a', ('b', 'c'))),
            ('a 2', ('a', '2')),
            (('a', 2), ('a', 2)),
            ('a 3.4', ('a', '3.4')),
            (('a', 3.4), ('a', 3.4)),
            (('a', (2, 3.4)), ('a', (2, 3.4))),
            ((), ()),
            (call('list', 1, '2', (3.4,)),
                (1, '2', (3.4,)) if self.wantobjects else
                ('1', '2', '3.4')),
        ]
        if tcl_version >= (8, 5):
            if not self.wantobjects:
                expected = ('12', '\xe2\x82\xac', '\xe2\x82\xac', '3.4')
            elif get_tk_patchlevel() < (8, 5, 5):
                # Before 8.5.5 dicts were converted to lists through string
                expected = ('12', u'\u20ac', u'\u20ac', '3.4')
            else:
                expected = (12, u'\u20ac', u'\u20ac', (3.4,))
            testcases += [
                (call('dict', 'create', 12, u'\u20ac', '\xe2\x82\xac', (3.4,)),
                    expected),
            ]
        for arg, res in testcases:
            self.assertEqual(split(arg), res)


class BigmemTclTest(unittest.TestCase):

    def setUp(self):
        self.interp = Tcl()

    @test_support.cpython_only
    @unittest.skipUnless(INT_MAX < PY_SSIZE_T_MAX, "needs UINT_MAX < SIZE_MAX")
    @test_support.precisionbigmemtest(size=INT_MAX + 1, memuse=5, dry_run=False)
    def test_huge_string(self, size):
        value = ' ' * size
        self.assertRaises(OverflowError, self.interp.call, 'set', '_', value)


def setUpModule():
    if test_support.verbose:
        tcl = Tcl()
        print 'patchlevel =', tcl.call('info', 'patchlevel')


def test_main():
    test_support.run_unittest(TclTest, TkinterTest, BigmemTclTest)

if __name__ == "__main__":
    test_main()
