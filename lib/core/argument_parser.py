#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse

def argument_parser():
    parse = argparse.ArgumentParser()
    parse.add_argument('-a', '--apache', help = 'Analyzer Apache Log', action = 'store_true')
    parse.add_argument('-n', '--nginx', help = 'Analyzer Nginx Log', action = 'store_true')
    parse.add_argument('-i', '--iis', help = 'Analyzer IIS Log', action = 'store_true')
    parse.add_argument('File_Path', help = 'The path of the log file', action = 'store')
    args = parse.parse_args()
    return args