#!/usr/bin/python
# -*- coding: UTF-8 -*-

from lib.core import Messages
from lib.vulnerability import sqli
from lib.vulnerability import code_exec_and_file_include
from lib.vulnerability import webshell
from lib.vulnerability import hack_tools
from lib.cms_vulnerability import cms_vulnerability


class ApacheAnalyzer():
    file_path = ''
    log = ''
    url_list = []
    user_agent_list = []
    message = Messages()

    def __init__(self, file_path):
        self.file_path = file_path
        super().__init__()

    def processed(self):
        self.get_url_and_user_agent()
        self.detect_sqli()
        self.detcet_code_exec_and_file_include()
        self.detect_webshell()
        self.detect_hack_tools()
        self.detect_cms()

    def get_url_and_user_agent(self):
        file = open (self.file_path, 'r')
        log = file.readline()
        while log:
            try:
                self.url_list.append(log.split(' ')[6])
                self.user_agent_list.append(log.split(' ')[11])
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
                self.message.vulnerability_find('SQL Injection', line, url)
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
                self.message.vulnerability_find('Code Execution or File Inlcude', line, url)
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
                self.message.vulnerability_find('Web Shell', line, url)
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
                self.message.vulnerability_find('Hack Tools', line, user_agent)
            line = line + 1
        if hack_tools_exist  == False:
            self.message.info_vulnerability_not_find('Hack Tools')
    
    def detect_cms(self):
        self.message.info_start_to_analyze('CMS Vulnerability')
        cms_vulnerability_exist = False
        for url in self.url_list:
            if cms_vulnerability(url) == True:
                cms_vulnerability_exist = True
        if cms_vulnerability_exist  == False:
            self.message.info_vulnerability_not_find('CMS Vulnerability')
