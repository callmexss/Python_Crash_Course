# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-02 00:54:16
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-02 01:05:38

player = 'Shan'


player_attr = [10, 5, 3] # hp, atk, def

enemy_attr = [9, 4, 2] # hp, atk, def


nums = [x for x in range(1, 10)]


for num in nums:
	turn = ''
	if num == 1:
		turn = str(num) + 'st'
	elif num == 2:
		turn = str(num) + 'nd'
	elif num == 3:
		turn = str(num) + 'rd'
	else:
		turn = str(num) + 'th'

	print (turn, 'turn...')
	if player_attr[0] > 0 and enemy_attr[0] > 0:
		print('fight')
		player_attr[0] -= enemy_attr[1] - player_attr[2]
		enemy_attr[0] -= player_attr[1] - enemy_attr[2]

	elif player_attr[0] <= 0:
		print('game over')
		break
	else:
		print('you win')
		break


