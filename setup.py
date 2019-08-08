#!/usr/bin/env python3
'The Punsy pip package'

import setuptools

def readme():
    'Return README.md as a string'
    with open('README.md', 'r') as istream:
        return istream.read()

setuptools.setup(
    name='punsy',
    version='0.0.3',
    author='Tom McKeesick',
    author_email='tmck01@gmail.com',
    description='A rhyming pun generator.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/tmck-code/punsy',
    packages=setuptools.find_packages(),
    package_data={
        'punsy': ['cmudict-0.7b.utf8']
    },
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'punsy = punsy.cmu:poc',
        ],
    },
    install_requires=[
        'tqdm'
    ]
)
