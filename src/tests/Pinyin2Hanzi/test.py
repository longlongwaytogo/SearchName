#!usr/bin/env python
# coding: utf-8

#from Pinyin2Hanzi import DefaultDagParams
#from Pinyin2Hanzi import dag


from __future__ import (print_function, unicode_literals)

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append('..')

def pinyin_2_hanzi(pinyinList):
    from Pinyin2Hanzi import DefaultDagParams
    from Pinyin2Hanzi import dag
    dagParams = DefaultDagParams()
    result = dag(dagParams, pinyinList, path_num=10, log=True) # 10 代表后选值个数
    for item in result:
        socre = item.score
        res = item.path # 转换结果
        print(socre,''.join(res))


if __name__ == '__main__':
    lists1 = ['zhong','xin']
    pinyin_2_hanzi(lists1)