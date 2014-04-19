Nagini is a custom Harry Potter-themed Python. More information on how I made Nagini can be found in this [blog post](http://mathamy.com/import-accio-bootstrapping-python-grammar.html).


# Usage

### Launching the `nagini` interpreter

    $ nagini

### `accio`ing modules

    >>> accio random
    >>> random.random()
    0.6507285787268219

### Checking the type of an object

    >>> type(3)
    <__main__.Slytherin object at 0x1004c3290>

### Converting from `int` to `float`

    >>> wingardium_leviosa(3)
    3.0

### Functional Programming

    >>> reducto(lambda a, x: a + x, range(5))
    10

### Quitting the `nagini` interpreter

    >>> avada_kedavra()


# Installation

1. Clone repository

        $ git clone https://github.com/amygdalama/nagini.git

2. Compile intermediary Python

        $ cd nagini/cpython
        $ ./configure
        $ make

3. Create a symlink for the intermediary Python and add it to the `PATH`

        $ ln -s python.exe python
        $ export PATH=$(pwd):$PATH

4. Compile Nagini

        $ cd ../nagini-python
        $ ./configure
        $ make

5. Make the `nagini` script executable

        $ cd ../
        $ chmod a+x nagini

6. Add the location of the `nagini` script to your path

        $ export PATH=$(pwd):$path

    Or, if you want access to the `nagini` command for all terminal sessions, add the following line to your `.bashrc` or `.bash_profile`:

        export PATH=/path/to/nagini:$PATH
