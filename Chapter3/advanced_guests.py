# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-05-31 00:25:32
# @Last Modified by:   callmexss
# @Last Modified time: 2018-05-31 02:49:20

distinguished_guest = ['grandma', 'a yu', 'me']

can_not_come = distinguished_guest.pop()

distinguished_guest.append('han fang')


print(can_not_come, 'can not come')

print('i wanna have dinner with', distinguished_guest[0])
print('i wanna have dinner with', distinguished_guest[1])
print('i wanna have dinner with', distinguished_guest[2])

print('A bigger table!')


distinguished_guest.insert(0, 'wang tao')
distinguished_guest.insert(len(distinguished_guest) // 2, 'father')
distinguished_guest.insert(-1, 'mother')

print('i wanna have dinner with', distinguished_guest[0])
print('i wanna have dinner with', distinguished_guest[1])
print('i wanna have dinner with', distinguished_guest[2])
print('i wanna have dinner with', distinguished_guest[3])
print('i wanna have dinner with', distinguished_guest[4])
print('i wanna have dinner with', distinguished_guest[5])


print('i can only invite two people')

print('sorry i can not invite you,', distinguished_guest.pop())
print('sorry i can not invite you,', distinguished_guest.pop())
print('sorry i can not invite you,', distinguished_guest.pop())
print('sorry i can not invite you,', distinguished_guest.pop())

print('i wanna have dinner with', distinguished_guest[0])
print('i wanna have dinner with', distinguished_guest[1])

del distinguished_guest[0]
del distinguished_guest[0]

print(distinguished_guest)
