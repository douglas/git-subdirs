# coding: utf-8

from setuptools import setup

setup(
    name='sgit',
    version='0.0.1',
    py_modules=['sgit', 'plugins/__init__', 'plugins/gh', 'plugins/colors'],
    entry_points={
        'console_scripts': ['sgit = sgit:main']
    },
    author='Andrey Vlasovskikh, Douglas Soares de Andrade',
    author_email='andrey.vlasovskikh@gmail.com, contato@douglasandrade.com',
    description='Small wrapper for performing git commands on nested '
                'repositories in subdirectories',
    license='MIT',
    url='https://github.com/douglas/sgit',
    install_requires=[
        'pygithub'
    ],
)
