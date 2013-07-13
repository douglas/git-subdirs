# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='git-subdirs',
    version='0.4',
    py_modules=['gitsubdirs', 'plugins/__init__', 'plugins/gh', 'plugins/colors'],
    entry_points={
        'console_scripts': ['sgit = gitsubdirs:main']
    },
    author='Andrey Vlasovskikh, Douglas Andrade',
    author_email='andrey.vlasovskikh@gmail.com, contato@douglasandrade.com',
    description='Small wrapper for performing git commands on nested '
                'repositories in subdirectories',
    license='MIT',
    url='https://github.com/vlasovskikh/git-subdirs',
    install_requires=['pygithub'],
)
