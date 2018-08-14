#!/usr/bin/env python
"""alternative build script for python documentation.

This script runs the sphix documentation build.

Example:
    $> make.py

In python for python.
"""

#TODO adds blurb support

import sys
import os.path
import textwrap
import argparse


# dependencies
try:
    import sphinx
except ImportError:
    print("""
The 'sphinx-build' command was not found. Make sure you have Sphinx
installed, then set the SPHINXBUILD environment variable to point
to the full path of the 'sphinx-build' executable. Alternatively you
may add the Sphinx directory to PATH.

If you don't have Sphinx installed, grab it from
  http://sphinx-doc.org/
"""
)
    sys.exit(1)

failed = []
for n in [ 'blurb', 'python_docs_theme', ]: 
    try:
        __import__(n)
    except ImportError:
        failed.append(n)

if failed:
    print("""
The [{p}] package(s) were not found. 
Installing with 
  {e} -m pip install {i}

""".format(e=sys.executable, p=','.join(failed), i=' '.join(failed))
)
    sys.exit(1)


# The script begins here!!

import sphinx.cmdline


def npath(*parts):
    if sys.platform != 'win32':
        parts = [ a.replace('\\', os.path.sep) for a in parts ]
    x = os.path.join(*parts)
    x = os.path.expanduser(x)
    x = os.path.normpath(x)
    return x


def split_doc(txt):
    if not txt:
        return '', ''
    descr, _, epi = txt.lstrip().partition('\n')
    epi = textwrap.dedent(epi)
    return descr, epi.strip()


def main(o):

    # building the sphinx command line 
    cmd = [] 
    cmd += [ '-b', 'html', ]

    if o.force:
        cmd += [ '-a', ]
    if not o.color:
        cmd += [ '--no-color', ]
    if o.doctreedir:
        cmd += [ '-d', o.doctreedir, ]

    overrides = {}
    #overrides['version'] = '1.2.3'
    #overrides['release'] = '4'
    for k, v in overrides.items():
        cmd += [ '-D', '{0}={1}'.format(k, v), ]

    cmd += [ o.sourcedir, o.outputdir, ]
    cmd.extend(o.filenames)

    sphinx.cmdline.main(cmd)

                
def parse_args(args=None):
    description, epilog = split_doc(__doc__)
    class StandardFormatter(argparse.ArgumentDefaultsHelpFormatter,
                            argparse.RawDescriptionHelpFormatter):
        pass
    parser = argparse.ArgumentParser(formatter_class=StandardFormatter,
                                     description=description, epilog=epilog)

    workdir = npath(__file__, '..')
    parser.add_argument('-c', '--color', action='store_true', default=False,
                            help='use colors')
    parser.add_argument('-f', '--force', action='store_true', default=False,
                            help='force all nodes rebuild')
    parser.add_argument('-d', '--doctrees', dest='doctreedir', metavar='<OUTPUTDIR>', nargs='?',
                            default=npath(os.getcwd(), 'build', 'doctrees'),
                            help='output build directory')
    parser.add_argument('-o', '--output', dest='outputdir', metavar='<OUTPUTDIR>',
                            default=npath(os.getcwd(), 'build', 'html'),
                            help='output build directory')
    parser.add_argument('-i', '--sourcedir', metavar='<SOURCEDIR>',
                            default=npath(workdir),
                            help='input dource dir')

    parser.add_argument('filenames', nargs='*')

    options = parser.parse_args(args)

    # sphinx directory containing the config file
    options.confdir = workdir

    filenames = []
    for f in options.filenames or []:
        filenames.append(npath(f, 'index') if os.path.isdir(f) else f)
    options.filenames = filenames
    return options
        

if __name__ == '__main__':
    sys.exit(main(parse_args()) or 0)
