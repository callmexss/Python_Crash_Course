# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-09 01:12:00
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-09 01:14:27

def make_album(singer, album):
	return {singer:album}

albums = []
albums.append(make_album('jay', '双截棍'))
albums.append(make_album('林俊杰', '编号89757'))
albums.append(make_album('阿桑', '一直很安静'))

from pprint import pprint
pprint(albums)
