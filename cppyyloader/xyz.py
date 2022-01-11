import cppyy

from cppyyloader.lib_info import INCLUDE_PATH, LIBRARY_PATH

cppyy.add_include_path(INCLUDE_PATH)
cppyy.add_library_path(LIBRARY_PATH)


for header in []:
    cppyy.include(header)

# from cppyy.gbl import ...