#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, isdir, join


class SystemHelper(object):
    @staticmethod
    def list_files_in_directory(directory, escape_hidden_file=False):
        files = [f for f in listdir(directory) if isfile(join(directory, f))]
        if escape_hidden_file:
            files = [f for f in files if not f.startswith('.')]
        return [join(directory, f) for f in files]

    @staticmethod
    def list_dirs_in_directory(directory, escape_hidden_dir=False):
        dirs = [_dir for _dir in listdir(directory) if isdir(join(directory, _dir))]
        if escape_hidden_dir:
            dirs = [_dir for _dir in dirs if not _dir.startswith('.')]
        return [join(directory, _dir) for _dir in dirs]

    @staticmethod
    def move(source, target):
        pass

    @staticmethod
    def make_dir(dir_name):
        pass

    @staticmethod
    def unzip_gz_file(gz_file, unzip_file_to_folder='.'):
        pass

    @staticmethod
    def append_to_file(file_name, lines):
        pass


if __name__ == '__main__':
    _directory = ''
    print (SystemHelper.list_files_in_directory('/Users/hfwu/Desktop/bib/BIB29/data/2017_04_25', True))
