#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Messages():

    def info_start_to_analyze(self, vulnerability_type = ''):
        print('\033[5;32;2m' + '[*] INFO: Start to analyzer : ' + vulnerability_type + '\033[0m') 
    
    def info_vulnerability_not_find(self, vulnerability_type = ''):
        print('\033[5;33;2m' + '[*] INFO: There is no ' + vulnerability_type + ' find in this log file.' + '\033[0m')

    def vulnerability_find(self, vulnerability_type = '', line_number = 0, log_string = ''):
        print('\033[5;31;2m' + '[!] VULNERABILITY: Type: ' + vulnerability_type + ' Find vulnerability in line ' + str(line_number) + '\033[0m')
        print('\033[5;31;2m' + '[!] VULNERABILITY: original log: ' + log_string + '\033[0m')
    
