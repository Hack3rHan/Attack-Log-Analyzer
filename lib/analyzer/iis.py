#!/usr/bin/python
# -*- coding: UTF-8 -*-

class IISAnalyzer():
    file_path = ''
    log = ''

    def __init__(self, file_path):
        self.file_path = file_path
        super().__init__()