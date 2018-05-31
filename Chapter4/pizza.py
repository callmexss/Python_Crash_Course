# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-01 00:13:54
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-01 00:35:56

pizzas = ['fruit pizza', 'meet pizza', 'sea food pizza']

for pizza in pizzas:
	print(pizza)

for pizza in pizzas:
	print('i like',pizza)


friend_pizzas = pizzas[:]

pizzas.append('vegetable pizza')
friend_pizzas.append('milk pizza')

print('my pizzas:', pizzas)
print('my friend\'s pizza:', friend_pizzas)