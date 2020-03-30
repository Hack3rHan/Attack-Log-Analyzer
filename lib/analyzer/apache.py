#!/usr/bin/python
# -*- coding: UTF-8 -*-

from lib.match import sqli
from lib.core import Messages


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
        pass

    def detect_webshell(self):
        pass

        
