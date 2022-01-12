"""Lib loader"""
__version__ = "0.0.1"

import sys

import cppyy


__all__ = ("std",)


def __getattr__(name):
    gbl = __import__(f"cppyy.gbl", fromlist=[""])
    mod = getattr(gbl, name)
    return mod