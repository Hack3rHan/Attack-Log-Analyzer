#!/usr/bin/python
# -*- coding: UTF-8 -*-

from colorama import  init, Fore, Back, Style

init(autoreset=True)


class Colored(object):

    def red(self, s):
        return Fore.RED + s + Fore.RESET

    def green(self, s):
        return Fore.GREEN + s + Fore.RESET

    def yellow(self, s):
        return Fore.YELLOW + s + Fore.RESET


class Messages():
    color = Colored()

    def info_start_to_analyze(self, vulnerability_type = ''):
        print(self.color.green('[*] INFO: Start to analyzer : {}'.format(vulnerability_type))) 
    
    def info_vulnerability_not_find(self, vulnerability_type = ''):
        print(self.color.yellow('[*] INFO: There is no {} find in this log file.'.format(vulnerability_type)))

    def vulnerability_find(self, vulnerability_type = '', line_number = 0, log_string = ''):
        print(self.color.red('[!] INFO: Type: {}. Find vulnerability in line {}'.format(vulnerability_type, str(line_number))))
        print(self.color.red('[!] INFO: original string: {}\n'.format(log_string)))

    
