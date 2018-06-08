# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-09 01:14:54
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-09 01:19:49


def user_make_album():
    singer = input("Singer: ")
    if not singer:
    	return 
    album = input("Album: ")
    if not album:
    	return 
    return {singer: album}


if __name__ == '__main__':
    albums = []
    while 1:
        album = user_make_album()
        if not album:
            break
        albums.append(album)

    import pprint

    pprint.pprint(albums)
