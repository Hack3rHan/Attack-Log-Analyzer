#!/usr/bin/python
# -*- coding: UTF-8 -*-

from lib.argument_parser import argument_parser
from lib.Analyzer import ApacheAnalyzer
from lib.Analyzer import NginxAnalyzer
from lib.Analyzer import IISAnalyzer

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