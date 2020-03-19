#!/usr/bin/python
# -*- coding: UTF-8 -*-

def sqli(log_string):
    sqli_list = ['\'', '"' , '%27', '(', ')','select', 'SELECT', 'xp_cmdshell', 'update', 'UPDATE',
    'limit', 'LIMIT', 'order', 'ORDER', 'sleep', 'SLEEP', 'and', 'AND', 'or', 'OR', 'union','UNION',
    'where', 'WHERE', 'waitfor', 'WAITFOR', 'if', 'IF', 'like', 'LIKE', 'from', 'FROM']
    for keyword in sqli_list:
        if keyword in log_string:
            return True
    return False
