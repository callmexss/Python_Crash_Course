# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-09 01:39:23
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-09 01:42:02


def car(made, the_type, **kwargs):
	car_info = {}
	car_info['made'] = made
	car_info['type'] = the_type 
	for k, v in kwargs.items():
		car_info[k] = v

	return car_info


print(car('china', 'changan', size="big", price='500000'))
