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
    name='saxs-app-analysis',
    version='0.0.1',
    packages=['saxs_app_analysis'],
    package_data={'saxs_app_analysis': ['templates/*', 'templatetags/*']},
    data_files = media_files,
)
