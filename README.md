# Rex #
Rex is a regular expression (regex) swiss-army-knife. Rex provides multiple
functions for working with regular expressions on files or standard input. It
is similar to the `grep` tool, but provides more functionality and uses regex
instead of basic patterns.

A good regular expression reference can be found at 
http://www.regular-expressions.info/reference.html

## Installation ##
To install Rex, run the following as root
    make install
This will allow you to run Rex by simply typing
    rex

### Removal ###
To remove Rex, run the following as root
    make uninstall

## Usage ##
    Usage: rex.py [options] <function> <expression> [files...]

    Options:
      -h, --help            show this help message and exit
      --version             Print version info and exit
      -q, --quiet           Suppress output
      -m EXPR, --match=EXPR
                            Match expression with input
      -s EXPR, --search=EXPR
                            Search for expression match in input
      -a EXPR, --match-all=EXPR, --all=EXPR
                            Find all matches of expression in input
      -t EXPR, --split=EXPR
                            Split input at each match
      --maxsplit=MAX        Used in comination with --split, sets a maximum amount
                            of splits
      -c, --count           Used in combination with --match-all or --split, print
                            number of matches/splits instead of matches/splits
      -g GROUP, --group=GROUP
                            Print a group
      -i, --ignorecase      Ignore case when matching
      -l, --multiline       Treat input as multiline
      -n, --dotall          Make `.` match all, including newlines

### Examples ###
    rex -m "foobar[a-c]" example.file
Determine whether `example.file` starts with "foobar", then a letter from 'a' to
'c'.
    rex -g1 -s "foobar([a-c])" example.file
Search for "foobar", then a letter from 'a' to 'c' in `example.file`, and print
the found letter (group 1).
    rex -a "foo(.*)bar" example.file
Find all text in `example.file` that starts with "foo" and ends with "bar". For
example, "foobazbar".
    rex -t "foo" example.file
Split text in `example.file` at every occurance of "foo".
