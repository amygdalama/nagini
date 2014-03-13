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

$ ./configure --with-pydebug
$ make -s -j2
```

Got this warning message:

```
Python build finished, but the necessary bits to build these modules were not found:
_bsddb             dl                 imageop         
linuxaudiodev      ossaudiodev        readline        
spwd               sunaudiodev                        
To find the necessary bits, look in setup.py in detect_modules() for the module's name.
```


tried:

1. import_spell
    ```
    import_name: import_spell dotted_as_names
    import_from: ('from' ('.'* dotted_name | '.'+)
                  import_spell ('*' | '(' import_as_names ')' | import_as_names))
    import_spell: 'import' | 'accio'
    ```

    received error: 
    ```
    >>> import numpy
    SystemError: invalid node 339 for PyAST_FromNode
    [58574 refs]
    ```

2. import_name: 'import' dotted_as_names | 'accio' dotted_as_names
HOLY SHIT IT WORKS

3. import_from: (('from' ('.'* dotted_name | '.'+)
              'import' ('*' | '(' import_as_names ')' | import_as_names)) |
              ('from' ('.'* dotted_name | '.'+)
              'accio' ('*' | '(' import_as_names ')' | import_as_names)))
HOLY SHIT THAT WORKS TOO

`export PATH=/Users/amyhanlon/projects/nagini/cpython/:$PATH`
