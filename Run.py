#!/usr/bin/python
# -*- coding: UTF-8 -*-

from lib.core.argument_parser import argument_parser
from lib.analyzer import *

def main():
    options = argument_parser()
    if options.nginx == True:
        nginx(options.File_Path)
    elif options.apache == True:
        apache(options.File_Path)
    elif options.iis == True:
        iis(options.File_Path)
    else:
        exit()

if __name__ == "__main__":
    main()