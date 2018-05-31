# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-01 00:05:40
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-01 00:09:50

player = ['star', 'yellow', 'surgar', 'rather']


print(sorted(player))
player.reverse()
print(player)


print("There are", len(player), "songs")
last_song = player.pop()
print('last song:', last_song)
