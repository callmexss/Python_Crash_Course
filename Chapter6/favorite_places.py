# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-06 00:22:23
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-06 00:26:21


favorite_places = {}


favorite_places['tom'] = 'beijing, shanghai, suzhou'
favorite_places['bob'] = 'shanghai, wuhan, chengdu'
favorite_places['alice'] = 'chongqing, qingdao, suzhou'


for each in favorite_places.items():
	print(each[0] + "'s favorite places are", each[1])
