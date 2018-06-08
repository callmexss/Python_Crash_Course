# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-09 01:35:31
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-09 01:39:00


def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for k, v in user_info.items():
        profile[k] = v
    return profile


tom_bell = build_profile('tom', 'bell', hobby="piano", age="20", country="USA")
print(tom_bell)
