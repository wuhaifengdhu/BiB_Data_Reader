#!/usr/bin/python
# -*- coding: utf-8 -*-
from date_helper import DateHelper
from system_helper import SystemHelper


class BibReader(object):
    def __init__(self, data_directory, append_to_file):
        self.directory = data_directory
        self.last_read_date = None
        self.new_data = None
        self.append_to_file = append_to_file

    @staticmethod
    def get_today_folder():
        pass

    def is_date_change(self):
        now_date = DateHelper.get_current_date()
        if self.last_read_date is not None and self.last_read_date != now_date:
            return True
        return False

    def read_last_date_file(self):
        pass

    def read_new_data(self):
        if self.is_date_change():
            self.read_last_date_file()
        self.read_data()
        SystemHelper.append_to_file(self.new_data, self.append_to_file)

    def read_data(self):
        pass

    @staticmethod
    def clean_folder_after_read(folder_name):
        pass

