#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2013 Douglas Soares de Andrade
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

import os

from os.path import exists, join, abspath
from subprocess import check_call

from github import Github
from .colors import pprinter


class GitHub(object):
    def __init__(self):
        token = os.environ.get('SGIT_GITHUB_TOKEN', '')
        self.gh = Github(token)

    def clone_repositories(self, args):
        repos = self.get_repositories(args)
        for repo in repos:
            repo_basename = repo.split('/')[-1][:-4]

            if exists(join(abspath(os.curdir), repo_basename)):
                pprinter('Repository already exists:', repo_basename)
            else:
                pprinter('Cloning Repository', repo)
                check_call(['git', 'clone', repo])

    def get_repositories(self, args):
        owner_type = args[0]
        owner_name = args[1]

        if owner_type == "-o":
            org = self.gh.get_organization(owner_name)
            return [repo.clone_url for repo in org.get_repos()]
        elif owner_type == "-u":
            user = self.gh.get_user(owner_name)
            return [repo.clone_url for repo in user.get_repos('owner')]
