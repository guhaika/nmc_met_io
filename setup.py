# _*_ coding: utf-8 _*_

from os import path
from setuptools import find_packages, setup
from codecs import open


name = 'nmc_met_io'
author = __import__(name).__author__
version = __import__(name).__version__

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=name,

    version=version,

    description=("Collection of tools for I/O or"
                 "accessing meteorological data."),
    long_description=long_description,

    # author
    author=author,
    author_email='kan.dai@foxmail.com',

    # LICENSE
    license='GPL3',

    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],

    python_requires='>3.5',
    zip_safe = False,

    packages=find_packages(exclude=['docs', 'tests', 'build', 'dist']),
    include_package_data=True,
    exclude_package_data={'': ['.gitignore']},

    install_requires=['numpy', 'scipy', 'xarray', 'pandas',
                      'protobuf', 'urllib3', 'tqdm', 'python-dateutil']
)

# development mode (DOS command):
#     python setup.py develop
#     python setup.py develop --uninstall

# build mode：
#     python setup.py build --build-base=D:/test/python/build

# distribution mode:
#     python setup.py sdist             # create source tar.gz file in /dist
#     python setup.py bdist_wheel       # create wheel binary in /dist
