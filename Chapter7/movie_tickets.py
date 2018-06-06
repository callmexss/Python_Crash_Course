# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-07 00:05:16
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-07 00:12:11

age = input('how old are you: ')

age = int(age)

while 0 < age < 150:
    if age < 3:
        print('free')
    if 3 <= age <= 12:
        print(10)
    if age > 12:
        print(15)
    age = int(input('how old are you: '))
