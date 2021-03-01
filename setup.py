from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.md')) as f:
    str_readme      = f.read()

with open(path.join(path.dirname(path.abspath(__file__)), 'VERSION')) as f:
    str_version     = f.read().strip()

str_depNotes = """

1. manually add the dependency to install_requires as numpy
2. pip install -e .
3. test run
4. pip freeze > requirements.txt (which generates something like numpy==1.19

"""

setup(
    name                            =   'pfapi',
    version                         =   str_version,
    packages                        =   ['pfapi'],
    url                             =   'https://github.com/FNNDSC/pfapi',
    license                         =   'MIT',
    author                          =   'Rudolph Pienaar',
    author_email                    =   'Rudolph.Pienaar@childrens.harvard.edu',
    description                     =   'Base chassis providing FAST-API engine',
    long_description                =   str_readme,
    long_description_content_type   =   'text/markdown',
    python_requires                 =   '>=3.8',
    install_requires                =   ['pudb', 'pyyaml', 'jinja2', 'fastapi', 'uvicorn'],
    entry_points={
        'console_scripts': [
            'pfapi = pfapi.__main__:main'
            ]
        },
    package_data={
        'pfapi': ['templates/*']
    },
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Topic :: Software Development',
        'Topic :: System :: Software Distribution'
    ]
)
