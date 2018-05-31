# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-01 00:29:41
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-01 00:33:49


li = [x for x in range(10)]


li1 = li[:] # create a new list
li2 = li # point to the same list as li

li.pop()
print(li)
print(li1)
print(li2)

print('the first three items in list are:')
for i in li[:3]:
	print(i)

print('three items from the middle of the list are:')
for i in li[len(li) // 2:len(li) // 2 +3]:
	print(i)

print('the last three items in the list are:')
for i in li[-3:]:
	print(i)