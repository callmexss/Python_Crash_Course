# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-06 23:57:41
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-07 00:04:35

material = ''

while 1:
    material = input('What kind of ingredient do you want: ')
    if material == 'quit':
        break
    print('we will add', material, 'to pizza')
