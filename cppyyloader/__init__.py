"""Lib loader"""
__version__ = "0.0.1"

import sys


__all__ = ("std",)


def __getattr__(name):
    from cppyy import gbl

    mod = getattr(gbl, name)
    return mod