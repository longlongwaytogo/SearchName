#!usr/bin/env python
# coding: utf-8
from __future__ import(print_function,unicode_literals)
from Pinyin2Hanzi import (DefaultDagParams,dag)
import user_setting
import sys
from xpinyin import Pinyin 
from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag

reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append('..')

'''
#file: main.py
#brief: main entry
#date: 2017/07/20
#author: longlongwaytogo
'''

#print("import pinyin module")

def test():
    print("this a pinyin main.")
    main()

 
def pinyin_to_hanzi(pinyin,Topk=5,Log=True):
    '''
    拼音转化为汉字
    汉字存在多意性，所以这里没有一一对应的关系，只能选出概率最高的topk
    '''
    print(pinyin)
    translator=DefaultDagParams()
    result=dag(translator,pinyin,path_num=Topk,log=Log)
    #print(result)

    # for item in result:
    #     socre=item.score # 得分
    #     res=item.path # 转换结果
    #     print(socre, ''.join([one.decode('utf-8') for one in res]))
    return result

 
def main():
    print("this is a main call!")

    if len(user_setting.setting["first_name"]) > 0:
        print("fist_name is not null")
    else:
        print("first_name len:",len(user_setting.setting["first_name"]))
    

    curFile = sys.argv[0]
    pos = curFile.rfind('/')
    curFilePath =curFile[0:30]
    #print("curPath:",curFilePath); 
    pinyinDataFileName = curFilePath +"/dictionaries/pinyin2.txt"
    print(pinyinDataFileName)
    pinyinFile = open(pinyinDataFileName,"r")

    n = 100
    pySet = []
    while n > 0 :
        n = n -1
        line = pinyinFile.readline()
        py = line.strip('\n')
       # print (py) 
        pySet.append(py)
    pinyinFile.close()
    print("read pinyin from pinyin.txt")

    famliy_name = user_setting.setting['famliy_name']

    if len(famliy_name) == 0:
        famliy_name = u"李"
    pinyin_out = curFilePath +"/outputs/pinyin_out.txt"
    pyout = open(pinyin_out,'w+')
    count = 0
    for f in pySet:		
        for s in pySet:
            # count +=1
            # print ("s:",count)
            first_name = f
            second_name = s
            #final_name =[]
            print("name:",f,s)
            final_name = [f,s]
            res = pinyin_to_hanzi(final_name,20,False)
            for r in res:
                count +=1
                score=r.score # 得分
                words=r.path # 转换结果
                print(famliy_name,''.join([one.decode('utf-8') for one in words ]))
                out_name = str(count) + ":" + str(score) + ":" + famliy_name + ''.join([one.decode('utf-8') for one in words ])  + "\n"
                pyout.writelines(out_name)
                #print(socre, ''.join([one.decode('utf-8') for one in words]))
            if count > 3000 :
                break
        else : # else 和 for s 平级，当执行完一次for s 则跳到此处
            print ("else")
            continue # continue导致for f 代码不继续执行，跳到下一循环
        break # 当for s 执行break时，else不被执行，无法调用continue，这执行到break，跳出for f

    pyout.close()

    print("pinyin output over!")
if __name__ == "__main__":
    test()