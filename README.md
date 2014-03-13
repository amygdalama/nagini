Learning about Python internals by replacing them with Harry Potter spells, because why wouldn't I do such a thing.

Add the line

```
export PYTHONSTARTUP=~/path/to/harrypotter.py
```
to your `~/.bashrc` or `~/.bash_profile` to really screw things up.


Add nagini script
Create symlink in usr/local/bin to nagini script
chmod nagini


clone cpython, lol:

```
$ hg clone http://hg.python.org/cpython
destination directory: cpython
requesting all changes
adding changesets
adding manifests
adding file changes
added 89634 changesets with 197780 changes to 10122 files (+2 heads)
updating to branch default
3835 files updated, 0 files merged, 0 files removed, 0 files unresolved

$ cd cpython
$ hg checkout 2.7
3752 files updated, 0 files merged, 913 files removed, 0 files unresolved

$ ./configure
$ make
```