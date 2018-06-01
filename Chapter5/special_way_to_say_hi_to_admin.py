# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-02 00:44:23
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-02 00:46:52

users = ['admin', '', '', 'tom', 'bell', 'jerry', 'alice']


for user in users:
	if not user:
		print('user not give')
		continue

	if user == 'admin':
		print('for admin')
	else:
		print('for user')