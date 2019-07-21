#!usr/bin/env python
#coding: utf-8

from xpinyin import Pinyin

p = Pinyin()
# default splitter is '-'
print p.get_pinyin(u"上海")

# show tone marks 
print p.get_pinyin(u"上海",tone_marks="marks") # 使用拼音声调符号
print p.get_pinyin(u"上海",tone_marks="numbers") # 使用拼音声调数字表示

# remove splitter
print p.get_pinyin(u"上海",'') # 没有分隔符
 
# set splitter as whitespace
print p.get_pinyin(u"上海", ' ') # 以空格分隔

# 显示单个汉字首字母大写
print p.get_initial(u"上") 

#显示多个汉字首字母大写，用‘-’链接
print p.get_initials(u"上海")

# 取消连接符
print p.get_initials(u"上海", u'')
 
# 使用空格链接
print p.get_initials(u"上海", u' ')
 
