#!/usr/bin/python
# -*- coding: UTF-8 -*-

from lib.message import Messages
from lib.output import Output
from lib.vulnerability import sqli
from lib.vulnerability import code_exec_and_file_include
from lib.vulnerability import webshell
from lib.vulnerability import hack_tools
from lib.vulnerability import cms_vulnerability

class Analyzer():
    _file_path = ''
    _url_list = []
    _user_agent_list = []
    _message = Messages()
    _output = Output()

    def __init__(self, file_path:str):
        self._file_path = file_path

    def _detect_sqli(self):
        self._message.info_start_to_analyze('SQL Injection')
        line = 1
        sqli_exist = False
        for url in self._url_list:
            if sqli(url) == True:
                sqli_exist = True
                self._message.vulnerability_find('SQL Injection', line, url.rstrip()[0:190])
                self._output.add_data('SQL Injection', str(line), url.rstrip()[0:190])
            line = line + 1
        if sqli_exist == False:
            self._message.info_vulnerability_not_find('SQL Injection')
    
    def _detcet_code_exec_and_file_include(self):
        self._message.info_start_to_analyze('Code Execution or File Inlcude')
        line = 1
        code_exec_and_file_include_exist = False
        for url in self._url_list:
            if code_exec_and_file_include(url) == True:
                code_exec_and_file_include_exist = True
                self._message.vulnerability_find('Code Execution or File Inlcude', line, url.rstrip()[0:190])
                self._output.add_data('Code Execution or File Inlcude', str(line), url.rstrip()[0:190])
            line = line + 1
        if code_exec_and_file_include_exist == False:
            self._message.info_vulnerability_not_find('Code Execution or File Inlcude')

    def _detect_webshell(self):
        self._message.info_start_to_analyze('Web Shell')
        line = 1
        webshell_exist = False
        file = open (self._file_path, 'r')
        log = file.readline()
        for url in self._url_list:
            if webshell(url) == True and log.split(' ')[8] == '200':
                webshell_exist = True
                self._message.vulnerability_find('Web Shell', line, url.rstrip()[0:190])
                self._output.add_data('Web Shell', str(line), url.rstrip()[0:190])
            line = line + 1
            log = file.readline()
        if webshell_exist == False:
            self._message.info_vulnerability_not_find('Web Shell')
            
    def _detect_hack_tools(self):
        self._message.info_start_to_analyze('Hack Tools')
        line = 1
        hack_tools_exist = False
        for user_agent in self._user_agent_list:
            if hack_tools(user_agent) == True:
                hack_tools_exist = True
                self._message.vulnerability_find('Hack Tools', line, user_agent.rstrip()[0:190])
                self._output.add_data('Hack Tools', str(line), user_agent.rstrip()[0:190])
            line = line + 1
        if hack_tools_exist  == False:
            self._message.info_vulnerability_not_find('Hack Tools')
    
    def _detect_cms_vul(self):
        self._message.info_start_to_analyze('CMS Vulnerability')
        line = 1
        cms_vulnerability_exist = False
        for url in self._url_list:
            vul = cms_vulnerability(url)
            if vul:
                cms_vulnerability_exist = True
                self._message.vulnerability_find(vul, line, url.rstrip()[0:190])
                self._output.add_data(vul, str(line), url.rstrip()[0:190])
            line = line + 1
        if cms_vulnerability_exist  == False:
            self._message.info_vulnerability_not_find('CMS Vulnerability')
