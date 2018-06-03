# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-04 00:08:02
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-04 00:10:19

rivers = {
    'changjiang': 'China',
    'huanghe': 'China',
    'eerqisihe': 'China',
}

for river in rivers.keys():
    print(river)

for each in rivers.items():
    print(each[0], ':', each[1])
