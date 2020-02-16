#!/usr/bin/python
# -*- coding: UTF-8 -*-

from lib.core.argument_parser import argument_parser

def main():
    options = argument_parser()
    if options.nginx == True:
        exit()
    elif options.apache == True:
        exit()
    else:
        exit()


if __name__ == "__main__":
    main()