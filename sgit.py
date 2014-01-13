#!/usr/bin/env python
# coding: utf-8

# Copyright (C) 2011 Andrey Vlasovskikh
# Copyright (C) 2014 Douglas Soares de Andrade
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import os
from subprocess import check_call, CalledProcessError

from plugins.colors import pprinter


def git(repo, argv):
    cwd = os.getcwd()
    os.chdir(repo)
    try:
        check_call(['git'] + argv)
    finally:
        os.chdir(cwd)


def gitdirs(basedir):
    for root, dirs, files in os.walk(basedir):
        for dir in dirs:
            if dir == '.git':
                yield os.path.normpath(root)


def main(argv=sys.argv[1:]):
    try:
        if argv[0] in ("-o", "-u"):
            from plugins.gh import GitHub
            hub = GitHub()
            hub.clone_repositories(argv)
        else:
            for path in gitdirs('.'):
                name = path if path != '.' else 'current'
                pprinter('Repository', name)
                git(path, argv)
    except CalledProcessError:
        print >> sys.stderr, 'terminated'
    except KeyboardInterrupt:
        print >> sys.stderr, 'interrupted'


if __name__ == '__main__':
    main()
