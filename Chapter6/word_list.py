# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-04 00:00:20
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-04 00:07:07


word_list = {
    'function': 'a block of code to do some specific things',
    'operation': 'do something',
    'compile': 'change code to machine code',
    'link': 'add the object together',
    'debug': 'find the bug in a program',
    'list': 'a container contains something',
    'tuple': 'a list can\'t be changed',
    'map': 'key-value pairs',
    'lambda': 'a function without a name',
    'pip': 'package management'
}

for item in word_list.items():
    print(item[0], ':', item[1])
