# Rex #
Rex is a regular expression (regex) swiss-army-knife. Rex provides multiple
functions for working with regular expressions on files or standard input.

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
      --dotall              Make . match all, including newlines
