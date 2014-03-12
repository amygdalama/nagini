Learning about Python internals by replacing them with Harry Potter spells, because why wouldn't I do such a thing.

Add the line

```
export PYTHONSTARTUP=~/path/to/harrypotter.py
```
to your `~/.bashrc` or `~/.bash_profile` to really screw things up.


Add nagini script
Create symlink in usr/local/bin to nagini script
chmod nagini


note from cpython build: 

```
# Substitution happens here, as the completely-expanded BINDIR
# is not available in configure
sed -e "s,@EXENAME@,/usr/local/bin/python3.4m," < ./Misc/python-config.in >python-config.py
# Replace makefile compat. variable references with shell script compat. ones;  -> 
sed -e 's,\$(\([A-Za-z0-9_]*\)),\$\{\1\},g' < Misc/python-config.sh >python-config
# On Darwin, always use the python version of the script, the shell
# version doesn't use the compiler customizations that are provided
# in python (_osx_support.py).
if test `uname -s` = Darwin; then \
        cp python-config.py python-config; \
    fi
```