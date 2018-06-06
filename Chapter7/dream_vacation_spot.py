# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-07 00:22:51
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-07 00:24:54

places = []

while 1:
    place = input(
        'if you could visit one place in the world, where would you go? ')
    if place == 'quit':
    	break
    places.append(place)


print(places)
