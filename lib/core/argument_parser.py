#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse

def argument_parser():
    parse = argparse.ArgumentParser()
    parse.add_argument('-a', '--apache', help = '分析Apache日志', action = 'store_true')
    parse.add_argument('-n', '--nginx', help = '分析Nginx日志', action = 'store_true')
    args = parse.parse_args()
    return args