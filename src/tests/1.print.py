#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test.py
# https://blog.csdn.net/joyfixing/article/details/79971667 中文字符乱码问题

'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""
print "this is a test!"
print u"这是一个测试" # 将中文保存为unicode
s = "这是一个unicode --utf8--gbk转换测试"
#print "utf-8:",s
g = s.decode('utf8')
print g
u = g.encode('gbk')
print u

#raw_input("按下enter 键退出，其他任意键显示...\n")
raw_input(u"entry key天空!".encode('gbk')) # 将unicode转换为gbk编码显示


s = "中文"
u = s.decode('utf-8')
print u
print type(u)
print repr(u)
