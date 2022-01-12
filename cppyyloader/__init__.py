"""Lib loader"""
__version__ = "0.0.1"

import sys
from types import ModuleType

import cppyy


class LocalModule(ModuleType):
    """Pseudo module"""

    __all__ = ()
    __package__ = __name__
    __path__ = []
    __file__ = __file__

    def __init__(self, name, doc):
        super().__init__(name, doc)
        _, self.submodule_name = name.split(".")

    def __getattr__(self, name):
        mod = __import__(f"cppyy.gbl.{self.submodule_name}", fromlist=[""])
        return getattr(mod, name)


def __getattr__(name):
    mod = LocalModule(f"{__name__}.{name}", LocalModule.__doc__)
    sys.modules[mod.__name__] = mod
    return mod