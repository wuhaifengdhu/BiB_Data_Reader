#!/usr/bin/python
# -*- coding: utf-8 -*-
from lib.bib_reader import BibReader
import time


class Main(object):
    @staticmethod
    def run_script(data_directory, data_store_file, read_frequency=5):
        reader = BibReader(data_directory, data_store_file)
        print ("Start service reading bib device records!")
        while True:
            time.sleep(read_frequency)
            reader.read_new_data()


if __name__ == '__main__':
    # step 1. configure parameter
    bib_data_folder = ''
    new_data_file = ''
    read_frequency = 5

    # step 2. Start service to read
    main = Main()
    try:
        main.run_script(bib_data_folder, new_data_file, read_frequency)
    except KeyboardInterrupt:
        print ("Service stopped as user interrupt from user command!")
