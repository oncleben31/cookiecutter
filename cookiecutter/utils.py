#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
cookiecutter.utils
------------------

Helper functions used throughout Cookiecutter.
"""

import errno
import os
import sys
import contextlib


PY3 = sys.version > '3'
if PY3:
    pass
else:
    import codecs


def make_sure_path_exists(path):
    """
    Ensures that a directory exists.
    :param path: A directory path.
    """
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            return False
    return True


def unicode_open(filename, *args, **kwargs):
    """
    Opens a file as usual on Python 3, and with UTF-8 encoding on Python 2.
    :param filename: Name of file to open.
    """
    kwargs['encoding'] = "utf-8"
    if PY3:
        return open(filename, *args, **kwargs)
    return codecs.open(filename, *args, **kwargs)


@contextlib.contextmanager
def work_in(dirname=None):
  curdir = os.getcwd()
  try:
    if dirname is not None:
      os.chdir(dirname)
    yield
  finally:
    os.chdir(curdir)
