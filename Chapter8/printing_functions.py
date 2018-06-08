# -*- coding: utf-8 -*-
# @Author: callmexss
# @Date:   2018-06-09 01:43:26
# @Last Modified by:   callmexss
# @Last Modified time: 2018-06-09 01:50:08

def import1():
	import printing_models
	printing_models.print_mod()


def import2():
	from printing_models import print_mod
	print_mod()


# this will cause a exception
# def import3():
# 	from printing_models import *
# 	print_mod()

def import4():
	import printing_models as pm
	pm.print_mod()

import1()
import2()
# import3()
import4()

from printing_models import *
print_mod()