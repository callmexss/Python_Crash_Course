# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-06 00:16:57
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-06 00:21:45

pets = []


lily = {'name': 'lily', 'type': 'dog', 'master': 'bob'}
huahua = {'name': 'huahua', 'type': 'cat', 'master': 'alice'}
xiaohei = {'name': 'xiaohei', 'type': 'pig', 'master': 'turing'}

pets.append(lily)
pets.append(huahua)
pets.append(xiaohei)

for pet in pets:
    print(pet['name'], 'is a', pet['type'], 'its master is', pet['master'])
