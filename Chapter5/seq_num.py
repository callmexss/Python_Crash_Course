# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-02 00:51:18
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-03 23:58:19

nums = [x for x in range(1, 10)]


for num in nums:
    if num == 1:
        print(str(num), 'st')
    elif num == 2:
        print(str(num), 'ed')
    elif num == 3:
        print(str(num), 'nd')
    else:
        print(str(num), 'th')
