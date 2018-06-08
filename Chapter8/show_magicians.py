# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-09 01:20:50
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-09 01:30:52

magicians = ['tom', 'bell', 'alice']


def show_magicians(li):
    for each in li:
        print(each)


show_magicians(magicians)


def make_great(li):
    for i in range(len(li)):
    	li[i] = "The Great " + li[i]
    return li

li = make_great(magicians[:]) # pass an argument as a copy

print(magicians)
print(li)
