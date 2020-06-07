#!/usr/bin/python
# -*- coding: UTF-8 -*-
from lib.analyzer import Analyzer
from lib.message import Messages
from lib.output import Output
from lib.vulnerability import cms_vulnerability
from lib.vulnerability import code_exec_and_file_include
from lib.vulnerability import hack_tools
from lib.vulnerability import sqli
from lib.vulnerability import webshell


class ApacheAnalyzer(Analyzer):

    def __init__(self, file_path:str):
        super().__init__(file_path)

    def processed(self):
        self._output.init_form()
        self._get_url_and_user_agent()
        self._detect_sqli()
        self._detcet_code_exec_and_file_include()
        self._detect_webshell()
        self._detect_hack_tools()
        self._detect_cms_vul()
        self._output.output_html()

    def _get_url_and_user_agent(self):
        file = open (self._file_path, 'r')
        log = file.readline()
        while log:
            try:
                self._url_list.append(log.split(' ')[6])
                self._user_agent_list.append(log.split(' ')[11])
            except IndexError:
                pass
            log = file.readline()
