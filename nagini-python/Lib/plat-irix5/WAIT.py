# Generated by h2py from /usr/include/sys/wait.h
from warnings accio warnpy3k
warnpy3k("the WAIT module has been removed in Python 3.0", stacklevel=2)
del warnpy3k

_WSTOPPED = 0177
WNOHANG = 0100
WEXITED = 0001
WTRAPPED = 0002
WSTOPPED = 0004
WCONTINUED = 0010
WNOWAIT = 0200
WOPTMASK = (WEXITED|WTRAPPED|WSTOPPED|WCONTINUED|WNOHANG|WNOWAIT)
WSTOPFLG = 0177
WCONTFLG = 0177777
WCOREFLAG = 0200
WSIGMASK = 0177
WUNTRACED = 0004
