#!/usr/bin/python
# -*- coding: UTF-8 -*-

from lib.argument_parser import argument_parser
from lib.analyzer import ApacheAnalyzer
from lib.analyzer import IISAnalyzer
from lib.analyzer import NginxAnalyzer


if __name__ == "__main__":
    options = argument_parser()
    if options.nginx:
        analyzer = NginxAnalyzer(options.File_Path)
        analyzer.processed()
    elif options.apache:
        analyzer = ApacheAnalyzer(options.File_Path)
        analyzer.processed()
    elif options.iis:
        analyzer = IISAnalyzer(options.File_Path)
        analyzer.processed()