#!/usr/bin/python
# -*- coding: UTF-8 -*-

from lib.Message import Messages
from lib.Output import Output
from lib.vulnerability import sqli
from lib.vulnerability import code_exec_and_file_include
from lib.vulnerability import webshell
from lib.vulnerability import hack_tools
from lib.vulnerability import cms_vulnerability

class IISAnalyzer():
    file_path = ''
    log = ''
    url_list = []
    user_agent_list = []
    message = Messages()
    output = Output()

    def __init__(self, file_path):
        self.file_path = file_path
        super().__init__()

    def processed(self):
        self.output.init_form()
        self.get_url_and_user_agent()
        self.detect_sqli()
        self.detcet_code_exec_and_file_include()
        self.detect_webshell()
        self.detect_hack_tools()
        self.detect_cms()
        self.output.output_html()

    def get_url_and_user_agent(self):
        file = open (self.file_path, 'r')
        log = file.readline()
        while log:
            if log[0] == '#':
                log = file.readline()
                continue
            else:
                try:
                    self.url_list.append(log.split(' ')[4] + log.split(' ')[5])
                    self.user_agent_list.append(log.split(' ')[9])
                except IndexError:
                    pass
            log = file.readline()

    def detect_sqli(self):
        self.message.info_start_to_analyze('SQL Injection')
        line = 1
        sqli_exist = False
        for url in self.url_list:
            if sqli(url) == True:
                sqli_exist = True
                self.message.vulnerability_find('SQL Injection', line, url.rstrip()[0:190])
                self.output.add_data('SQL Injection', str(line), url.rstrip()[0:190])
            line = line + 1
        if sqli_exist == False:
            self.message.info_vulnerability_not_find('SQL Injection')
    
    def detcet_code_exec_and_file_include(self):
        self.message.info_start_to_analyze('Code Execution or File Inlcude')
        line = 1
        code_exec_and_file_include_exist = False
        for url in self.url_list:
            if code_exec_and_file_include(url) == True:
                code_exec_and_file_include_exist = True
                self.message.vulnerability_find('Code Execution or File Inlcude', line, url.rstrip()[0:190])
                self.output.add_data('Code Execution or File Inlcude', str(line), url.rstrip()[0:190])
            line = line + 1
        if code_exec_and_file_include_exist == False:
            self.message.info_vulnerability_not_find('Code Execution or File Inlcude')

    def detect_webshell(self):
        self.message.info_start_to_analyze('Web Shell')
        line = 1
        webshell_exist = False
        file = open (self.file_path, 'r')
        log = file.readline()
        for url in self.url_list:
            if webshell(url) == True and log.split(' ')[8] == '200':
                webshell_exist = True
                self.message.vulnerability_find('Web Shell', line, url.rstrip()[0:190])
                self.output.add_data('Web Shell', str(line), url.rstrip()[0:190])
            line = line + 1
            log = file.readline()
        if webshell_exist == False:
            self.message.info_vulnerability_not_find('Web Shell')
            
    def detect_hack_tools(self):
        self.message.info_start_to_analyze('Hack Tools')
        line = 1
        hack_tools_exist = False
        for user_agent in self.user_agent_list:
            if hack_tools(user_agent) == True:
                hack_tools_exist = True
                self.message.vulnerability_find('Hack Tools', line, user_agent.rstrip()[0:190])
                self.output.add_data('Hack Tools', str(line), user_agent.rstrip()[0:190])
            line = line + 1
        if hack_tools_exist  == False:
            self.message.info_vulnerability_not_find('Hack Tools')
    
    def detect_cms(self):
        self.message.info_start_to_analyze('CMS Vulnerability')
        line = 1
        cms_vulnerability_exist = False
        for url in self.url_list:
            vul = cms_vulnerability(url)
            if vul != False:
                cms_vulnerability_exist = True
                self.message.vulnerability_find(vul, line, url.rstrip()[0:190])
                self.output.add_data(vul, str(line), url.rstrip()[0:190])
            line = line + 1
        if cms_vulnerability_exist  == False:
            self.message.info_vulnerability_not_find('CMS Vulnerability')