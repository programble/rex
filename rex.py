#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       rex.py
#       
#       Copyright 2010 Curtis (Programble) <programble@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

__version__ = "0.1.1"

from optparse import OptionParser
import sys
import re
import glob
import os.path

class qprint:
    quiet = False
    def __init__(self, string):
        if not self.quiet: print string

def version_info():
    """Print version info"""
    # GNU Coding guidelines suggests:
    # GNU hello 2.3
    # Copyright (C) 2007 Free Software Foundation, Inc.
    # License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
    # This is free software: you are free to change and redistribute it.
    # There is NO WARRANTY, to the extent permitted by law.
    print "Rex", __version__
    print "Copyright (C) 2010 Curtis (Programble) <programble@gmail.com>"
    print "License GPLv3: GNU GPL version 3 <http://gnu.org/licenses/gpl.html>"
    print "This is free software: you are free to change and redistribute it."
    print "There is NO WARRANTY, to the extent permitted by law."

def match(expr, file, groups=[0], ignorecase=False, multiline=False, dotall=False):
    # Read in input
    data = file.read()
    file.close()
    
    regexpr = None
    flags = 0
    # Combine flags provided by args
    if ignorecase:
        flags = flags | re.IGNORECASE
    if multiline:
        flags = flags | re.MULTILINE
    if dotall:
        flags = flags | re.DOTALL
    try:
        regexpr = re.compile(expr, flags)
    except:
        qprint("Invalid expression")
        return 4
    
    # regexpr should always have a value by now
    if not regexpr:
        assert(False)
    
    m = regexpr.match(data)
    if not m:
        qprint("No match")
        return 1
    else:
        # Print each group that is wanted
        for gn in groups:
            qprint(m.group(gn))
        return 0

def search(expr, file, groups=[0], ignorecase=False, multiline=False, dotall=False):
    data = file.read()
    file.close()
    
    regexpr = None
    flags = 0
    if ignorecase:
        flags = flags | re.IGNORECASE
    if multiline:
        flags = flags | re.MULTILINE
    if dotall:
        flags = flags | re.DOTALL
    try:
        regexpr = re.compile(expr, flags)
    except:
        qprint("Invalid expression")
        return 4
    
    if not regexpr:
        assert(False)
    
    m = regexpr.search(data)
    if not m:
        qprint("No match")
        return 1
    else:
        for gn in groups:
            qprint(m.group(gn))
        return 0

def matchall(expr, file, count=False, groups=[0], ignorecase=False, multiline=False, dotall=False):
    data = file.read()
    file.close()
    
    regexpr = None
    flags = 0
    if ignorecase:
        flags = flags | re.IGNORECASE
    if multiline:
        flags = flags | re.MULTILINE
    if dotall:
        flags = flags | re.DOTALL
    try:
        regexpr = re.compile(expr, flags)
    except:
        qprint("Invalid expression")
        return 4
    
    if not regexpr:
        assert(False)
    
    miter = regexpr.finditer(data)
    # Count matches (to determine if there were any)
    mcount = 0
    for m in miter:
        if not count:
            for gn in groups:
                qprint(m.group(gn))
        mcount += 1
    if count:
        qprint(mcount)
        return 0
    if mcount == 0:
        qprint("No matches")
        return 1
    return 0

def split(expr, file, maxsplit=0, count=False, ignorecase=False, multiline=False, dotall=False):
    data = file.read()
    file.close()
    
    regexpr = None
    flags = 0
    if ignorecase:
        flags = flags | re.IGNORECASE
    if multiline:
        flags = flags | re.MULTILINE
    if dotall:
        flags = flags | re.DOTALL
    try:
        regexpr = re.compile(expr, flags)
    except:
        qprint("Invalid expression")
        return 4
    
    if not regexpr:
        assert(False)
    
    splits = regexpr.split(data, maxsplit)
    if count:
        qprint(len(splits))
        return 0
    for segment in splits:
        qprint(segment)
    return 0

def main():
    global quiet
	# Parse command line options
    parser = OptionParser(usage="%prog [options] <function> <expression> [files...]")
    parser.add_option("--version", dest="version", action="store_true", default=False, help="Print version info and exit")
    parser.add_option("--quiet", "-q", dest="quiet", action="store_true", default=False, help="Suppress output")
    parser.add_option("--match", "-m", dest="match", action="store", default=None, metavar="EXPR", help="Match expression with input")
    parser.add_option("--search", "-s", dest="search", action="store", default=None, metavar="EXPR", help="Search for expression match in input")
    parser.add_option("--match-all", "--all", "-a", dest="matchall", action="store", metavar="EXPR", default=None, help="Find all matches of expression in input")
    parser.add_option("--split", "-t", dest="split", action="store", metavar="EXPR", default=None, help="Split input at each match")
    parser.add_option("--maxsplit", dest="maxsplit", action="store", type="int", metavar="MAX", default=0, help="Used in comination with --split, sets a maximum amount of splits")
    parser.add_option("--count", "-c", dest="count", action="store_true", default=False, help="Used in combination with --match-all or --split, print number of matches/splits instead of matches/splits")
    parser.add_option("--group", "-g", dest="groups", action="append", default=[], type="int", metavar="GROUP", help="Print a group")
    parser.add_option("--ignorecase", "-i", dest="ignorecase", action="store_true", default=False, help="Ignore case when matching")
    parser.add_option("--multiline", "-l", dest="multiline", action="store_true", default=False, help="Treat input as multiline")
    parser.add_option("--dotall", "-n", dest="dotall", action="store_true", default=False, help="Make `.` match all, including newlines")
    (options, args) = parser.parse_args()
    
    if options.version:
        version_info()
        return 0
    
    qprint.quiet = options.quiet
    
    # Set default to print group 0 (whole match)
    if options.groups == []:
        options.groups = [0]
    
    # Open all files specified
    files = []
    if len(args) > 0:
        for arg in args:
            # Expand to glob (wildcards), user (~ or ~user) and vars ($VAR)
            expanded = glob.glob(os.path.expanduser(os.path.expandvars(arg)))
            # This also allows us to find out if a file does not exist /before/
            # trying to open it.
            if expanded == []:
                qprint("File not found " + arg)
                return 8
            for ex in expanded:
                try:
                    files.append(open(ex, 'r'))
                except IOError:
                    qprint("Cannot open input file " + ex)
                    return 8
    else:
        # If no files, read from stdin
        files = [sys.stdin]
    
    rcode = 0
    for file in files:
        if options.match:
            rcode += match(options.match, file, options.groups, options.ignorecase, options.multiline, options.dotall)
        elif options.search:
            rcode += search(options.search, file, options.groups, options.ignorecase, options.multiline, options.dotall)
        elif options.matchall:
            rcode += matchall(options.matchall, file, options.count, options.groups, options.ignorecase, options.multiline, options.dotall)
        elif options.split:
            rcode += split(options.split, file, options.maxsplit, options.count, options.ignorecase, options.multiline, options.dotall)
        else:
            # No function supplied
            parser.print_help()
            return 0
    
    return rcode

if __name__ == '__main__':
    # Exit with code returned by main() (like C)
    sys.exit(main())
