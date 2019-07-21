# coding: utf-8
from __future__ import (print_function, unicode_literals)
from Pinyin2Hanzi import all_pinyin
# 枚举所有类型的规范拼音
#for py in all_pinyin():
#        print(py)

# 列举所有“规范”的拼音，写入文件：
#pyFile = open("pyDict.txt",'w+')
#for py in all_pinyin():
#     pyFile.write(py + "\n")
#pyFile.close()

#print("out put file over!")


#将拼音转换为“规范”的拼音：

from Pinyin2Hanzi import simplify_pinyin

print(simplify_pinyin('lue'))
# 输出：'lve'

print(simplify_pinyin('lüè'))
# 输出：'lve'

# 判断是否是“规范”的拼音：
from Pinyin2Hanzi import is_pinyin
print(is_pinyin('lue'))
# 输出：False
print(is_pinyin('lüè'))
# 输出：False
print(is_pinyin('lvee'))
# 输出：False
print(is_pinyin('lve'))
# 输出：True