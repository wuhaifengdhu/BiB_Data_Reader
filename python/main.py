#!/usr/bin/python
# -*- coding: utf-8 -*-
from lib.bib_reader import BibReader
from lib.system_helper import SystemHelper
from lib.http_helper import HttpHelper
import time
import os
import json


class Main(object):
    @staticmethod
    def run_script(data_directory, data_store_file, read_frequency=15, server_url=None):
        reader = BibReader(data_directory)
        print ("Start service reading bib device records!")
        while True:
            new_data = reader.read_new_data()
            print ("READING....NEW...DATA<<<<")
            print (os.linesep.join(new_data))
            print ("Finished reading!")
            SystemHelper.append_to_file(data_store_file, os.linesep.join(new_data))
            # send data to server back-end
            if server_url is not None:
                HttpHelper.post(server_url, json.dumps(new_data))
            time.sleep(read_frequency)


if __name__ == '__main__':
    # step 1. configure parameter
    bib_data_folder = './resource/data'
    new_data_file = 'data/console.dat'
    _server_url = 'http://127.0.0.1:5000/api/v1/sensor/data'

    # step 2. Start service to read
    main = Main()
    try:
        main.run_script(bib_data_folder, new_data_file, server_url=_server_url)
    except KeyboardInterrupt:
        print ("Service stopped as user interrupt from user command!")
