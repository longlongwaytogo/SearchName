#!usr/bin/env python
#encoding:utf-8
from __future__ import division
 
 
'''
__Author__:沂水寒城
功能：汉字与拼音的转化
'''
 
 
import sys
from xpinyin import Pinyin 
from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag
 
reload(sys)
sys.setdefaultencoding("utf-8")
 
 
 
def hanzi_to_pinyin(one_str,flag=''):
    '''
    将汉字转化为对应的拼音
    '''
    translator=Pinyin()
    info = one_str.decode('utf-8')
    one_kw_pinyin=translator.get_pinyin(unicode(one_str), flag).strip()
    #print '{0} Pinyin is: {1}'.format(one_str.decode('utf-8'),one_kw_pinyin)
    #print '{0} Pinyin is: {1}'.format(info,one_kw_pinyin)
    print info
    print "Pinyin is:{0}".format(one_kw_pinyin)
    return one_kw_pinyin
    
 
def pinyin_to_hanzi(pinyin,Topk=5):
    '''
    拼音转化为汉字
    汉字存在多意性，所以这里没有一一对应的关系，只能选出概率最高的topk
    '''
    translator=DefaultDagParams()
    result=dag(translator,pinyin,path_num=Topk,log=True)
    for item in result:
        socre=item.score # 得分
        res=item.path # 转换结果
        print socre, ''.join([one.decode('utf-8') for one in res])

 
if __name__ == '__main__':
    one_str="今天我们从哈尔滨工业大学毕业了"
    one_pinyin=hanzi_to_pinyin(one_str,flag='')
 
    
    one_pinyin_list=['jin','tian','wo','men','bi','ye','le']
    pinyin_to_hanzi(one_pinyin_list,Topk=5)
 
    one_pinyin_list=['jin','tian','wo','men','cong','ha','gong','da','bi','ye','le']
    pinyin_to_hanzi(one_pinyin_list,Topk=5)
#--------------------- 
#作者：Together_CZ 
#来源：CSDN 
#原文：https://blog.csdn.net/Together_CZ/article/details/81878654 
#版权声明：本文为博主原创文章，转载请附上博文链接！