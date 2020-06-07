#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
from HTMLTable import HTMLTable


class Output():
    table = HTMLTable(caption='')
    now = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time())) 

    def __init__(self):
        super().__init__()

    def init_form(self):
        self.table.append_header_rows((
            ('Vulnerability Type', 'Line', 'Original Log String'),
        ))
        self.table.caption.set_style({
            'font-size': '15px',
        })
        self.table.set_style({
            'border-collapse': 'collapse',
            'word-break': 'keep-all',
            'white-space': 'nowrap',
            'font-size': '14px',
        })
        self.table.set_cell_style({
            'border-color': '#000',
            'border-width': '1px',
            'border-style': 'solid',
            'padding': '5px',
        })
        self.table.set_header_row_style({
            'color': '#fff',
            'background-color': '#48a6fb',
            'font-size': '18px',
        })
        self.table.set_header_cell_style({
            'padding': '15px',
        })

    def add_data(self, vulnerability_type, line, original_log_string):
        self.table.append_data_rows((
            (vulnerability_type, line, original_log_string),
        ))

    def output_html(self):
        html = self.table.to_html()
        file = open('output/Result_'+self.now+'.html','a+')
        file.write(html)
        file.close
