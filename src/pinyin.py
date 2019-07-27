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

 
def pinyin_to_hanzi(pinyin,Topk=5):
    '''
    拼音转化为汉字
    汉字存在多意性，所以这里没有一一对应的关系，只能选出概率最高的topk
    '''
    print(pinyin)
    translator=DefaultDagParams()
    result=dag(translator,pinyin,path_num=Topk,log=True)
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



    #for data in pySet:
    #    print(data)

    famliy_name = user_setting.setting['famliy_name']
    # py1 =["tian"]
    # rlt = pinyin_to_hanzi(py1)
    # print(rlt)

    if len(famliy_name) == 0:
        famliy_name = u"李"

    count = 0
    for f in pySet:		
        # if count > 2:
		# 	print(" this is count:",count)
		# 	break
        for s in pySet:
            count +=1
            print ("s:",count)
            
            first_name = f
            second_name = s
            #final_name =[]
            print("name:",f,s)
            final_name = [f,s]
            res = pinyin_to_hanzi(final_name)
            # for r in res :
            #     #print(r)
            #     print(famliy_name,''.join([one.decode('utf-8') for one in r]))
            for r in res:
                socre=r.score # 得分
                words=r.path # 转换结果
                print(famliy_name,''.join([one.decode('utf-8') for one in words ]))
                #print(socre, ''.join([one.decode('utf-8') for one in words]))
            if count > 3 :
                break
        else :
            print ("else")
            continue
        break

            # first_name = f
            # second_name = s
            # final_name =[]
            # print(f,s)
            # final_name.append(f)
            # final_name.append(s)
            # res = pinyin_to_hanzi(final_name)
            # print(res)
            #for r in res:
            #    print(famliy_name + r)
            #count +=1
            #print("count:",count)
            #if count == 3:
            #    break
		#else:
        #    print("a")
        #else: # else 和 for s 平级，当执行完一次for s 则跳到此处
        #    continue # continue导致for f 代码不继续执行，跳到下一循环
        #break # 当for s 执行break时，else不被执行，无法调用continue，这执行到break，跳出for f


if __name__ == "__main__":
    test()