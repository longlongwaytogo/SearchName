# conding: utf-8
from __future__ import(print_function,unicode_literals)
from Pinyin2Hanzi import (DefaultDagParams,dag)
import user_setting

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
 
def main():
    print("this is a main call!")

    if len(user_setting.setting["first_name"]) > 0:
        print("fist_name is not null")
    else:
        print("first_name len:",len(user_setting.setting["first_name"]))
    
    pinyinFile = open("./dictionarys/pinyin.txt",'r')
    n = 100
    while n > 0 :
        n = n -1
        py = pinyinFile.readline()
        print (py) 

    py.close()

if __name__ == "__main__":
    test()