# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-07 00:15:34
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-07 00:21:20

sandwich_ordes = ['fruit', 'pastrami', 'meat',
                  'pastrami', 'vegetable', 'pastrami']
finished_sandwiches = []

print('pastrami has been sold out.')

i = 0
while i < len(sandwich_ordes):
    if sandwich_ordes[i] == 'pastrami':
        sandwich_ordes.pop(i)
    i += 1

while sandwich_ordes:
    finished = sandwich_ordes.pop()
    print('I made your', finished, 'sandwich.')
    finished_sandwiches.append(finished)


print(finished_sandwiches)
