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

__version__ = "0.1.0"

from optparse import OptionParser
import sys
import re

quiet = False

def qprint(data):
    if not quiet:
        print data

def version_info():
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

def match(expr, file, ignorecase=False):
    data = file.read()
    file.close()
    
    regexpr = None
    if ignorecase:
        try:
            regexpr = re.compile(expr, re.IGNORECASE)
        except:
            qprint("Invalid expression")
            return 4
    else:
        try:
            regexpr = re.compile(expr)
        except:
            qprint("Invalid expression")
            return 4
    
    if not regexpr:
        assert(false)
    
    m = regexpr.match(data)
    if not m:
        qprint("No match")
        return 1
    else:
        qprint(m.group())
        return 0

def main():
	# Parse command line options
    parser = OptionParser(usage="%prog TODO")
    parser.add_option("--version", dest="version", action="store_true", default=False, help="Print version info and exit")
    parser.add_option("--quiet", "-q", dest="quiet", action="store_true", default=False, help="Suppress output")
    parser.add_option("--match", "-m", dest="match", action="store", default=None, help="Match the expression with the input")
    parser.add_option("--ignorecase", "-i", dest="ignorecase", action="store_true", default=False, help="Ignore case when matching")
    (options, args) = parser.parse_args()
    
    if options.version:
        version_info()
        return 0
    
    quiet = option.quiet
    
    file = sys.stdin
    if len(args) > 0:
        try:
            file = open(args[0], 'r')
        except IOError:
            qprint("Cannot open input file")
            return 8
    
    if options.match != None:
        return match(options.match, file, options.ignorecase)
    
	return 0

if __name__ == '__main__':
	sys.exit(main())
