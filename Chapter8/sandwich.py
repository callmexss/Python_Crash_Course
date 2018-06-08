# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-09 01:31:50
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-09 01:34:28

def sandwich(**kwargs):
	for each in kwargs.items():
		print(each[0], ':', each[1])


sandwich(meat="meat", fruit="orange")
sandwich(meat="beef", fruit="apple")
sandwich(meat="chicken", fruit="pear")
