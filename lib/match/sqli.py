#!/usr/bin/python
# -*- coding: UTF-8 -*-

def sqli(log_string):
    sqli_list = ['\'', '"' , '%27', '(', ')','select', 'SELECT', 'xp_cmdshell', 'update', 'UPDATE',
    'limit', 'LIMIT', 'order by', 'ORDER BY', 'sleep', 'SLEEP', 'union','UNION','where', 'WHERE', 'waitfor',
    'WAITFOR', 'like', 'LIKE', 'from', 'FROM']
    for keyword in sqli_list:
        if keyword in log_string:
            return True
    return False
