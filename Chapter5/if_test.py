# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-02 00:32:13
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-02 00:36:03


if 1 == 2:
	print("impossible!")


name = "Tom"

if name:
	print("hello", name)


a = 'apple'
b = 'apple'

if a == b:
	print(a, '=', b)

if a is b:
	print(a, 'is', b)


if a.upper() == "APPLE":
	print(a.upper())


print(id(a) == id(b))