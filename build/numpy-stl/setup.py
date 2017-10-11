from __future__ import print_function

import os
import sys
import warnings
from setuptools import setup, extension
from setuptools.command.build_ext import build_ext

setup_kwargs = {}

try:
    import numpy
    from Cython import Build

    setup_kwargs['ext_modules'] = Build.cythonize([
        extension.Extension(
            'stl._speedups',
            ['stl/_speedups.pyx'],
            include_dirs=[numpy.get_include()],
        ),
    ])
except ImportError:
    print('WARNING', file=sys.stderr)
    print('Cython and Numpy is required for building extension.',
          file=sys.stderr)
    print('Falling back to pure Python implementation.', file=sys.stderr)

# To prevent importing about and thereby breaking the coverage info we use this
# exec hack
about = {}
with open('stl/__about__.py') as fp:
    exec(fp.read(), about)


if os.path.isfile('README.rst'):
    long_description = open('README.rst').read()
else:
    long_description = 'See http://pypi.python.org/pypi/%s/' % (
        about['__package_name__'])

install_requires = [
    'numpy',
    'nine',
    'python-utils>=1.6.2',
]

try:
    import enum
    assert enum
except ImportError:
    install_requires.append('enum34')


if os.environ.get('PYTEST_RUNNER', '').lower() == 'false':
    tests_require = []
    setup_requires = []
else:
    tests_require = ['pytest']
    setup_requires = ['pytest-runner']


class BuildExt(build_ext):

    def run(self):
        try:
            build_ext.run(self)
        except Exception as e:
            warnings.warn('''
            Unable to build speedups module, defaulting to pure Python. Note
            that the pure Python version is more than fast enough in most cases
            %r
            ''' % e)


if __name__ == '__main__':
    setup(
        name=about['__package_name__'],
        version=about['__version__'],
        author=about['__author__'],
        author_email=about['__author_email__'],
        description=about['__description__'],
        url=about['__url__'],
        license='BSD',
        packages=['stl'],
        long_description=long_description,
        tests_require=tests_require,
        setup_requires=setup_requires,
        entry_points={
            'console_scripts': [
                'stl = %s.main:main' % about['__import_name__'],
                'stl2ascii = %s.main:to_ascii' % about['__import_name__'],
                'stl2bin = %s.main:to_binary' % about['__import_name__'],
            ],
        },
        classifiers=['License :: OSI Approved :: BSD License'],
        install_requires=install_requires,
        cmdclass=dict(
            build_ext=BuildExt,
        ),
        **setup_kwargs
    )

