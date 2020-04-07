#!/usr/bin/python
# -*- coding: UTF-8 -*-


from lib.core import Messages
from lib.vulnerability import sqli
from lib.vulnerability import code_exec
from lib.vulnerability import webshell


class IISAnalyzer():
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
        self.detcet_code_exec()
        self.detect_webshell()

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
        line = 1
        for user_agent in self.user_agent_list:
            if 'sqlmap' in user_agent:
                sqli_exist = True
                self.message.vulnerability_find('SQL Injection', line, user_agent)
            line = line + 1
        if sqli_exist == False:
            self.message.info_vulnerability_not_find('SQL Injection')
    
    def detcet_code_exec(self):
        self.message.info_start_to_analyze('Code Execution or Command Execution')
        line = 1
        code_exec_exist = False
        for url in self.url_list:
            if code_exec(url) == True:
                code_exec_exist = True
                self.message.vulnerability_find('Code Execution or Command Execution', line, url)
            line = line + 1
        if code_exec_exist == False:
            self.message.info_vulnerability_not_find('Code Execution or Command Execution')

    def detect_webshell(self):
        self.message.info_start_to_analyze('Web Shell')
        line = 1
        webshell_exist = False
        for url in self.url_list:
            if webshell(url) == True:
                webshell_exist = True
                self.message.vulnerability_find('Web Shell', line, url)
            line = line + 1
        if webshell_exist == False:
            self.message.info_vulnerability_not_find('Web Shell')