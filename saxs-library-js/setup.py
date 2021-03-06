#!/usr/bin/env python
import os
from distutils.core import setup

def get_files(directory, install_base):
    file_list = []
    files=os.listdir(directory)
    found_files = []
    for file in files:
        if ( os.path.isdir(directory + "/" + file) ):
            if ( not file == ".svn"):
                file_list += get_files(directory + "/" + file, install_base)
        else:
            found_files.append(directory + "/" + file)
            
    if ( len(found_files) > 0 ):
        file_list.append((install_base + "/" + directory, found_files))
    return file_list

media_files = get_files("media", "share/saxs/")

setup(
    name='saxs-library-js',
    version='0.0.1',
    packages=['saxs_library_js'],
    package_data={'saxs_library_js': ['templates/*']},
    data_files = media_files,
)
