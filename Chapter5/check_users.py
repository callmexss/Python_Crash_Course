# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-02 00:47:17
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-02 00:50:27

users = ['admin', 'tom', 'bell', 'jerry', 'alice']
users2 = ['admin', 'john', 'bell', 'eve', 'alice']

users2lower = [user.lower() for user in users2]

for user in users:
	if user.lower() in users2lower:
		print('user name has been used')
	else:
		print(user, 'is available')




