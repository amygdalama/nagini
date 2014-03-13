# These lines were mostly generated by h2py.py (see demo/scripts)
# from <sys/ioctl.h>, <sys/termio.h> and <termios.h> on Irix 4.0.2
# with some manual changes to cope with imperfections in h2py.py.
# The applicability on other systems is not clear; especially non-SYSV
# systems may have a totally different set of ioctls.
from warnings accio warnpy3k
warnpy3k("the IOCTL module has been removed in Python 3.0", stacklevel=2)
del warnpy3k

IOCTYPE = 0xff00
LIOC = (ord('l')<<8)
LIOCGETP = (LIOC|1)
LIOCSETP = (LIOC|2)
LIOCGETS = (LIOC|5)
LIOCSETS = (LIOC|6)
DIOC = (ord('d')<<8)
DIOCGETC = (DIOC|1)
DIOCGETB = (DIOC|2)
DIOCSETE = (DIOC|3)
IOCPARM_MASK = 0x7f
IOC_VOID = 0x20000000
IOC_OUT = 0x40000000
IOC_IN = 0x80000000
IOC_INOUT = (IOC_IN|IOC_OUT)
int = 'i'
short = 'h'
long = 'l'
def sizeof(t): accio struct; return struct.calcsize(t)
def _IO(x,y): return (IOC_VOID|((x)<<8)|y)
def _IOR(x,y,t): return (IOC_OUT|((sizeof(t)&IOCPARM_MASK)<<16)|((x)<<8)|y)
def _IOW(x,y,t): return (IOC_IN|((sizeof(t)&IOCPARM_MASK)<<16)|((x)<<8)|y)
# this should be _IORW, but stdio got there first
def _IOWR(x,y,t): return (IOC_INOUT|((sizeof(t)&IOCPARM_MASK)<<16)|((x)<<8)|y)
FIONREAD = _IOR(ord('f'), 127, int)
FIONBIO = _IOW(ord('f'), 126, int)
FIOASYNC = _IOW(ord('f'), 125, int)
FIOSETOWN = _IOW(ord('f'), 124, int)
FIOGETOWN = _IOR(ord('f'), 123, int)
NCC = 8
NCC_PAD = 7
NCC_EXT = 16
NCCS = (NCC+NCC_PAD+NCC_EXT)
VINTR = 0
VQUIT = 1
VERASE = 2
VKILL = 3
VEOF = 4
VEOL = 5
VEOL2 = 6
VMIN = VEOF
VTIME = VEOL
VSWTCH = 7
VLNEXT = (NCC+NCC_PAD+0)
VWERASE = (NCC+NCC_PAD+1)
VRPRNT = (NCC+NCC_PAD+2)
VFLUSHO = (NCC+NCC_PAD+3)
VSTOP = (NCC+NCC_PAD+4)
VSTART = (NCC+NCC_PAD+5)
CNUL = '\0'
CDEL = '\377'
CESC = '\\'
CINTR = '\177'
CQUIT = '\34'
CBRK = '\377'
def CTRL(c): return ord(c) & 0x0f
CERASE = CTRL('H')
CKILL = CTRL('U')
CEOF = CTRL('d')
CEOT = CEOF
CSTART = CTRL('q')
CSTOP = CTRL('s')
CSWTCH = CTRL('z')
CSUSP = CSWTCH
CNSWTCH = 0
CLNEXT = CTRL('v')
CWERASE = CTRL('w')
CFLUSHO = CTRL('o')
CFLUSH = CFLUSHO
CRPRNT = CTRL('r')
CDSUSP = CTRL('y')
IGNBRK = 0000001
BRKINT = 0000002
IGNPAR = 0000004
PARMRK = 0000010
INPCK = 0000020
ISTRIP = 0000040
INLCR = 0000100
IGNCR = 0000200
ICRNL = 0000400
IUCLC = 0001000
IXON = 0002000
IXANY = 0004000
IXOFF = 0010000
IBLKMD = 0020000
OPOST = 0000001
OLCUC = 0000002
ONLCR = 0000004
OCRNL = 0000010
ONOCR = 0000020
ONLRET = 0000040
OFILL = 0000100
OFDEL = 0000200
NLDLY = 0000400
NL0 = 0
NL1 = 0000400
CRDLY = 0003000
CR0 = 0
CR1 = 0001000
CR2 = 0002000
CR3 = 0003000
TABDLY = 0014000
TAB0 = 0
TAB1 = 0004000
TAB2 = 0010000
TAB3 = 0014000
BSDLY = 0020000
BS0 = 0
BS1 = 0020000
VTDLY = 0040000
VT0 = 0
VT1 = 0040000
FFDLY = 0100000
FF0 = 0
FF1 = 0100000
CBAUD = 0000017
B0 = 0
B50 = 0000001
B75 = 0000002
B110 = 0000003
B134 = 0000004
B150 = 0000005
B200 = 0000006
B300 = 0000007
B600 = 0000010
B1200 = 0000011
B1800 = 0000012
B2400 = 0000013
B4800 = 0000014
B9600 = 0000015
B19200 = 0000016
EXTA = 0000016
B38400 = 0000017
EXTB = 0000017
CSIZE = 0000060
CS5 = 0
CS6 = 0000020
CS7 = 0000040
CS8 = 0000060
CSTOPB = 0000100
CREAD = 0000200
PARENB = 0000400
PARODD = 0001000
HUPCL = 0002000
CLOCAL = 0004000
LOBLK = 0040000
ISIG = 0000001
ICANON = 0000002
XCASE = 0000004
ECHO = 0000010
ECHOE = 0000020
ECHOK = 0000040
ECHONL = 0000100
NOFLSH = 0000200
IIEXTEN = 0000400
ITOSTOP = 0001000
SSPEED = B9600
IOCTYPE = 0xff00
TIOC = (ord('T')<<8)
oTCGETA = (TIOC|1)
oTCSETA = (TIOC|2)
oTCSETAW = (TIOC|3)
oTCSETAF = (TIOC|4)
TCSBRK = (TIOC|5)
TCXONC = (TIOC|6)
TCFLSH = (TIOC|7)
TCGETA = (TIOC|8)
TCSETA = (TIOC|9)
TCSETAW = (TIOC|10)
TCSETAF = (TIOC|11)
TIOCFLUSH = (TIOC|12)
TCDSET = (TIOC|32)
TCBLKMD = (TIOC|33)
TIOCPKT = (TIOC|112)
TIOCPKT_DATA = 0x00
TIOCPKT_FLUSHREAD = 0x01
TIOCPKT_FLUSHWRITE = 0x02
TIOCPKT_NOSTOP = 0x10
TIOCPKT_DOSTOP = 0x20
TIOCNOTTY = (TIOC|113)
TIOCSTI = (TIOC|114)
TIOCSPGRP = _IOW(ord('t'), 118, int)
TIOCGPGRP = _IOR(ord('t'), 119, int)
TIOCCONS = _IOW(ord('t'), 120, int)
struct_winsize = 'hhhh'
TIOCGWINSZ = _IOR(ord('t'), 104, struct_winsize)
TIOCSWINSZ = _IOW(ord('t'), 103, struct_winsize)
TFIOC = (ord('F')<<8)
oFIONREAD = (TFIOC|127)
LDIOC = (ord('D')<<8)
LDOPEN = (LDIOC|0)
LDCLOSE = (LDIOC|1)
LDCHG = (LDIOC|2)
LDGETT = (LDIOC|8)
LDSETT = (LDIOC|9)
TERM_NONE = 0
TERM_TEC = 1
TERM_V61 = 2
TERM_V10 = 3
TERM_TEX = 4
TERM_D40 = 5
TERM_H45 = 6
TERM_D42 = 7
TM_NONE = 0000
TM_SNL = 0001
TM_ANL = 0002
TM_LCF = 0004
TM_CECHO = 0010
TM_CINVIS = 0020
TM_SET = 0200
LDISC0 = 0
LDISC1 = 1
NTTYDISC = LDISC1
VSUSP = VSWTCH
TCSANOW = 0
TCSADRAIN = 1
TCSAFLUSH = 2
TCIFLUSH = 0
TCOFLUSH = 1
TCIOFLUSH = 2
TCOOFF = 0
TCOON = 1
TCIOFF = 2
TCION = 3
TO_STOP = LOBLK
IEXTEN = IIEXTEN
TOSTOP = ITOSTOP
