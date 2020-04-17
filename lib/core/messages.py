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
        print(self.color.green('[*] INFO: Start to analyzer : ' + vulnerability_type)) 
    
    def info_vulnerability_not_find(self, vulnerability_type = ''):
        print(self.color.yellow('[*] INFO: There is no ' + vulnerability_type + ' find in this log file.'))

    def vulnerability_find(self, vulnerability_type = '', line_number = 0, log_string = ''):
        print(self.color.red('[!] VULNERABILITY: Type: ' + vulnerability_type + ' Find vulnerability in line ' + str(line_number)))
        print(self.color.red('[!] VULNERABILITY: original log: ' + log_string))
    
