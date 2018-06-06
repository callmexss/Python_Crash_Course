# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-06 00:11:07
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-06 00:16:32

three_people = []

tom = {'name': 'tom', 'age':18}
alice = {'name': 'alice', 'age':15}
john = {'name': 'john', 'age':21}

three_people.append(tom)
three_people.append(alice)
three_people.append(john)


for people in three_people:
	print (people['name'], 'is', people["age"], 'old')
