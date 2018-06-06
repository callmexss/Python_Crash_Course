# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-06 00:26:50
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-06 00:32:40


cities = {}

cities['beijing'] = {'country': 'china',
                     'population': 'large', 'fact': 'capital of china'}
cities['new york'] = {'country': 'USA',
                      'population': 'large', 'fact': 'paradise of art'}
cities['naning'] = {'country': 'china',
                    'population': 'large', 'fact': 'beautiful'}


for city in cities.items():
    print(city[0], 'is in', city[1]['country'],
          'has', city[1]['population'], 'population', 'and it is', 
          city[1]['fact'])
