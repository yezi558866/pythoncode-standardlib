#!/usr/bin/python
# -*- coding: utf-8 -*-
import glob, os

modules = []

for module_file in glob.glob("*-plugin.py"):
	try:
		(module_name, ext) = os.path.splitext(os.path.basename(module_file))
		#os.path.splitext():分离文件名与扩展名，默认返回(fname, fextension)元组
		#os.path.basename()：去掉目录路径，返回文件名
		module = __import__(module_name)
		modules.append(module)
	except ImportError:
		pass #ignore broken modules

# say hello to all modules
for module in modules:
	module.hello()