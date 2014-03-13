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


$ hg checkout 2.7
$ cd cpython
$ ./configure
$ make
```