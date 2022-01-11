import os

import cppyy


LIB_PATH = os.environ.get("CPPYY_LIB_PATH")
INCLUDE_PATH = os.environ.get("CPPYY_INCLUDE_PATH")

if not LIB_PATH:
    raise RuntimeError(
        "Environment variable CPPYY_LIB_PATH not set!"
        "Please specify the location of the library you want to load."
    )

if not INCLUDE_PATH:
    raise RuntimeError(
        "Environment variable CPPYY_INCLUDE_PATH not set!"
        "Please specify the location of the header files you want to load."
    )
