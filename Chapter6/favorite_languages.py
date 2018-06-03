# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-04 00:11:05
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-04 00:23:56

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

people = ['jen', 'phil', 'tom', 'alice']
for each in people:
    if each in favorite_languages.keys():
        print(each + "'s favorite language is " + favorite_languages[each])
