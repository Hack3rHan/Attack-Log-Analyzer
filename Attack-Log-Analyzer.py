#!/usr/bin/python
# -*- coding: UTF-8 -*-

from lib.core import argument_parser
from lib.analyzer import ApacheAnalyzer
from lib.analyzer import NginxAnalyzer
from lib.analyzer import IISAnalyzer

def main():
    options = argument_parser()
    if options.nginx == True:
        analyzer_nginx = NginxAnalyzer(options.File_Path)
        analyzer_nginx.processed()
    elif options.apache == True:
        analyzer_apache = ApacheAnalyzer(options.File_Path)
        analyzer_apache.processed()
    elif options.iis == True:
        analyzer_iis = IISAnalyzer(options.File_Path)
        analyzer_iis.processed()
    else:
        exit()

if __name__ == "__main__":
    main()