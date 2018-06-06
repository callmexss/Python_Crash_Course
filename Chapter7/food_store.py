# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-07 00:12:33
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-07 00:15:04

sandwich_ordes = ['fruit', 'meat', 'vegetable']
finished_sandwiches = []

while sandwich_ordes:
    finished = sandwich_ordes.pop()
    print('I made your', finished, 'sandwich.')
    finished_sandwiches.append(finished)


print(finished_sandwiches)
